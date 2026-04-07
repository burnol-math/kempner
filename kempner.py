"""Author: Jean-François Burnol
Created: April 7, 2026

© Jean-François Burnol, 2026

This script is licensed under the
Creative Commons Attribution-ShareAlike 4.0 International License.
Full license text: https://creativecommons.org/licenses/by-sa/4.0/

ANY RE-USE OR PLAGIARIZING BY AN ARTIFICIAL INTELLIGENCE WITHOUT
PROPER ATTRIBUTION IS STRICTLY FORBIDDEN AND WILL GET PUNISHED

Compute Kempner series for multiple excluded digits according to the formulas
of

 1) Moments in the Exact Summation of the Curious Series of Kempner Type,
    The American Mathematical Monthly, 132:10 (2025), 995-1006, 
    https://doi.org/10.1080/00029890.2025.2554555

 2) Measures for the summation of Irwin series,
    Integers 26 (2026), No. A11,
    https://doi.org/10.5281/zenodo.18154150

Reference 1) gives an alternating series and reference 2) also a positive
series (only for the case of a single excluded digits but the generalization
to multiple excluded digits is straightforward and done here).

Contrarily to the irwin_v5.sage script of May 2025 available at

    https://gitlab.com/burnolmath/irwin,

- we do not use SageMath, but mpmath Python library,
- we do not take care of pre-assigned counts of occurrences,
  the code is only for excluding one or more base-b digits,
- **no attempt at parallelization is done**,
  hence the code is much simpler,
- we do not pre-compute power sums nor do we update rows of the
  Pascal triangle, but we compute everything on the fly,
- we do not store the successive constitutive terms of the series
  to add them in the end, starting from the smallest,
- we do not pre-establish how many terms will be computed but
  stop the iteration dynamically once a certain threshold is crossed,
- the mechanism for a decreasing running precision is implement in a
  far simpler way,
- the level ell is not limited to being 2, 3, or 4, it can be
  any integer at least 2. But of course ell in practice
  is limited by the fact that we have to handle
    (N or N-1) times N**(ell-1)
  admissible numbers which augments exponentially in ell.
  So higher values of ell are mainly for small bases, say 
  2, 3 or 4 perhaps.

It seems that the script is roughly 5x slower than irwin_v5.sage
for K(10,9,1002), I have not checked which parts of the code
are involved into this.  But the code here is much simpler and
handles multiple digits which irwin_v5.sage does not.

The present 2026 Python script supersedes the Maple code still
available at the present repository

    https://gitlab.com/burnolmath/kempner,

which was done only for b=10 and would have needed an update
for a general basis b.  It could be done, but the author is now
lacking a Maple license.

"""

__version__ = "1.0.0"
__date__    = "2026-04-06"
__author__  = "Jean-François Burnol"

from typing import List
from math import floor, ceil, log
from mpmath import mp, mpf, nstr

def kempner(b:int,
            E:List[int] | int,
            nboffigures:int = 100,
            ell:int = 3,
            silent:bool = False,
            trunc:bool = False) -> str:
    """Computes Kempner series for excluded digits in arbitrary basis

    Uses the alternating series at level ell from Burnol's AMM paper.

    :param b int: the base
    :param E List[int]: a list of digits in that base (or a single digit)
    :param nboffigures int: (optional, defaults to 100) number of asked-for
                           significant figures
    :param ell int: (optional, defaults to 3) the level ell
    :param silent bool: (optional, defaults to False) whether to print
                        som extra info at the end
    :param trunc bool: (optional, defaults to False) whether to round or
                       truncate
    :rtype: str
    :return: String with nboffigures significant figures (rounded) of the
             decimal expansion of the Kempner sum in base b and excluded
             digits E.
    """

    assert b > 1, f"Basis {b} less than 2"
    assert ell > 1, f"Level {ell} less than 2"
    assert nboffigures > 5, ("Number of asked-for significant figures"
                            f"{nboffigures} less than 6")

    P_target = ceil((nboffigures + 1) * log(10, 2))
    P_eps = P_target + min(ceil(ell * log(b,2)), 10)
    P_max = P_eps + 12

    mp.prec = P_max
    current_prec = P_max
    current_prec_float = float(P_max)

    if type(E) is int:
        E = [ E ]

    # ATTENTION! WITH PYTHON 3.13
    # >>> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - {0, 2, 3, 4, 5, 6, 7, 9}
    # {8, 1}
    # and not {1, 8} which we could hope for!
    # even worse
    # >>> sorted([8,1])
    # [1, 8]
    # >>> set([1,8])
    # {8, 1}
    # >>> set([1,9])
    # {1, 9}
    # One has to be very careful here with dict's.

    # It is is important we control the order for a correct defintion
    # later of prec_delta.  I detected this problem via discrepancies
    # between kempner() and kempnerpos() the first time I tried to
    # reproduce my Maple base 10 ancient computations.  On further
    # examination it was caused by a too large prec_delta.

    bdgts = set(range(b))
    Eset = set(E)
    Elist = sorted(Eset)
    A = sorted(bdgts - Eset)
    A1 = [ a for a in A if a != 0 ]

    N = len(A)
    N1 = len(A1)
    assert N == b - len(Elist), f"{Elist} has entries which are not base {b} digits"
    assert N1 > 0, "There must be some non-zero admissible digits"

    # blocks[l] will be the list of admissible numbers of length l
    # at l==0 the convention is that 0 is admissible because it is
    # represented by the empty word, but this has no incidence anyhow
    # in what follows
    blocks = [[0],]

    # at l==1 we have the admissible non zero digits
    # (in increasing order)
    blocks.append(list(A1))
    newblock = [ b * a1 + a0 for a1 in A1 for a0 in A]
    blocks.append(newblock)
    
    # now fill in all blocks.  This is much easier than in irwin.sage,
    # because there we needed to actually organize *all* numbers
    # according to the number of occurrences of excluded digit d.
    for l in range(3, ell + 1):
        newblock = [ b * n + a for n in newblock for a in A]
        blocks.append(newblock)

    # The series needs to add inverse powers of numbers with ell digits.
    # We will do this from smallest inverse power to largest.
    # ATTENTION it is important here that newblock was originally
    # ordered from smallest to largest.
    level_ell_numbers = newblock[::-1]
    # So now level_all_numbers[-1] is the smallest admissible level ell
    # number.

    # the u_m's are bounded above by b/(b-N). Due to inverse powers
    # we reduce the target precision at each iteration.  For ell=2
    # which is minimal, the minimal admissible number at level 2
    # is b, so prec_delta is at least 1.
    prec_delta = log(level_ell_numbers[-1], 2)

    # this will hold the n**(-m-1) inverse powers of level ell numbers
    # from smallest to largest.  Here m=0.
    level_ell_invpowers = [ mpf(1)/n for n in level_ell_numbers ]
    # initial approximation (under-estimate)
    # blocks[l] contains numbers with l base b digits
    S = sum(mpf(1)/n for l in range(ell-1, 0, -1) for n in blocks[l][::-1])

    # first term (m=0) of the series
    m = 0
    denom = b - N  # in general b**(m+1) - N
    denom_adjust = b * N - N
    ums = [ mpf(b) / denom ]
    cms = [ sum(x for x in level_ell_invpowers) * ums[0] ]

    digits_powers = [1 for n in A1]
    # the gamma_0 does not intervene anyhow in the recurrence
    gammams = [ len(A) ]

    S += cms[-1]
    eps = S * ( mpf(2) ** -P_eps )

    while True:
        m += 1
        denom = b * denom + denom_adjust

        mp.prec = current_prec

        # update inverse powers of level ell admissible numbers
        i = 0
        for n in level_ell_numbers:
            level_ell_invpowers[i] /= n
            i += 1

        # update digits powers
        i = 0
        for n in A1:
            digits_powers[i] *= n
            i += 1

        # extend gamma list
        gammam = sum(n for n in digits_powers)
        gammams.append(gammam)

        # apply recursion formula, computing binomial coefficients
        # as exact integers
        um = 0
        binomj = 1
        for j in range(1, m + 1):
            binomj = binomj * (m + 1 - j) // j
            um += mpf(binomj * gammams[j]) * ums[-j]

        # we need to divide by b**(m+1) - N
        um /= denom
        ums.append(um)

        cm = um * sum(x for x in level_ell_invpowers)
        if cm < eps:
            break

        cms.append(cm)

        mp.prec = P_max

        S += (-1)**m * cm

        current_prec_float = current_prec_float - prec_delta
        current_prec = max(20, ceil(current_prec_float))
        mp.prec = current_prec

    mp.prec = P_max

    if not silent:
        print(f"ell is {ell}")
        print(f"basis is {b}")
        print(f"List of excluded digits is {Elist}")
        print(f"Last used: m = {m-1}, |cm| = {nstr(cms[-1], 4, strip_zeros=False)}")
        print(f" not used: m = {m}, |cm| = {nstr(cm, 4, strip_zeros=False)}")

        # ATTENTION ! nstr supprime trailing zeros par défaut !!
        S_string = nstr(S, nboffigures + 3, strip_zeros=False)
        # print last digits + 3 more
        print(f"Last digits are {S_string[-12:-3]}({S_string[-3:]})")

        print(f"K({b}, {Elist}) rounded to {nboffigures} significant figures is:")

    # return result as a string with a total of nboffigures decimal digits
    if trunc:
        # we hope this gives correct truncation...
        return nstr(S, nboffigures + 6, strip_zeros=False)[:-6]
    else:
        return nstr(S, nboffigures, strip_zeros=False)


def kempnerpos(b:int,
               E:List[int] | int,
               nboffigures:int = 100,
               ell:int = 3,
               silent:bool = False,
               trunc:bool = False) -> str:
    """Computes Kempner series for excluded digits in arbitrary basis

    Uses the positive series at level ell which is give in Burnol's paper
    in the case of a single excluded digit.  I.e. it uses the complementary
    moment v_m, and inverse powers of n+1, where n is admissible of length ell.

    :param b int: the base
    :param E List[int]: a list of digits in that base (or a single digit)
    :param nboffigures int: (optional, defaults to 100) number of asked-for
                           significant figures
    :param ell int: (optional, defaults to 3) the level ell
    :param silent bool: (optional, defaults to False) whether to print
                        som extra info at the end
    :param trunc bool: (optional, defaults to False) whether to round or
                       truncate
    :rtype: str
    :return: String with nboffigures significant figures (rounded) of the
             decimal expansion of the Kempner sum in base b and excluded
             digits E.
    """

    assert b > 1, f"Basis {b} less than 2"
    assert ell > 1, f"Level {ell} less than 2"
    assert nboffigures > 5, ("Number of asked-for significant figures"
                            f"{nboffigures} less than 6")

    P_target = ceil((nboffigures + 1) * log(10, 2))
    P_eps = P_target + min(ceil(ell * log(b,2)), 10)
    P_max = P_eps + 12

    mp.prec = P_max
    current_prec = P_max
    current_prec_float = float(P_max)

    if type(E) is int:
        E = [ E ]

    # see comments in kempner()
    bdgts = set(range(b))
    Eset = set(E)
    Elist = sorted(Eset)
    A = sorted(bdgts - Eset)
    A1 = [ a for a in A if a != 0 ]
    Aprime = [ b - 1 - a for a in A[::-1] ]
    Aprime1 = [ a for a in Aprime if a != 0 ] 

    N = len(A)
    N1 = len(A1)
    assert N == b - len(Elist), f"{Elist} has entries which are not base {b} digits"
    assert N1 > 0, "There must be some non-zero admissible digits"

    blocks = [[0],]

    blocks.append(list(A1))
    newblock = [ b * a1 + a0 for a1 in A1 for a0 in A]
    blocks.append(newblock)
    
    for l in range(3, ell + 1):
        newblock = [ b * n + a for n in newblock for a in A]
        blocks.append(newblock)

    # last newblock has level ell admissible numbers *ordered*
    # level_ell_numbers_plus_one has them from largest to smallest.
    level_ell_numbers_plus_one = [ n + 1 for n in newblock[::-1]]

    # blocks[l] contains numbers with l base b digits
    S = sum(mpf(1)/n for l in range(ell-1, 0, -1) for n in blocks[l][::-1])

    # this will hold the (n+1)**(-m-1) inverse powers of level ell numbers
    # from smallest to largest.  Here m=0.
    level_ell_invpowers = [ mpf(1)/n for n in level_ell_numbers_plus_one ]

    # first term (m=0) of the series
    m = 0
    denom = b - N  # in general b**(m+1) - N
    denom_adjust = b * N - N
    vms = [ mpf(b) / denom ]
    cms = [ sum(x for x in level_ell_invpowers) * vms[0] ]

    codigits_powers = [1 for n in Aprime1]
    # the n=0 term has no influence anyhow on recurrence formula
    cogammams = [ N ]

    # This is first term (m=0) of series
    S += cms[-1]

    prec_delta = log(level_ell_numbers_plus_one[-1], 2)
    eps = S * ( mpf(2) ** -P_eps )

    while True:
        m += 1
        denom = b * denom + denom_adjust  ## b**(m+1) - N

        mp.prec = current_prec

        # update inverse powers of level ell admissible numbers
        i = 0
        for n in level_ell_numbers_plus_one:
            level_ell_invpowers[i] /= n
            i += 1

        # update (complementary) digits powers
        i = 0
        for n in Aprime1:
            codigits_powers[i] *= n
            i += 1

        # extend cogamma list
        cogammam = sum(n for n in codigits_powers)
        cogammams.append(cogammam)

        # apply recursion formula, computing binomial coefficients
        # as exact integers
        vm = 0
        binomj = 1
        for j in range(1, m + 1):
            binomj = binomj * (m + 1 - j) // j
            vm += mpf(binomj * cogammams[j]) * vms[-j]

        # denom is b**(m+1) - N
        vm += denom + N
        vm /= denom
        vms.append(vm)

        cm = vm * sum(x for x in level_ell_invpowers)
        if cm < eps:
            break

        cms.append(cm)

        mp.prec = P_max

        S += cm

        current_prec_float = current_prec_float - prec_delta
        current_prec = max(20, ceil(current_prec_float))
        mp.prec = current_prec

    mp.prec = P_max

    if not silent:
        print(f"ell is {ell}")
        print(f"basis is {b}")
        print(f"List of excluded digits is {Elist}")
        print(f"Last used: m = {m-1}, |cm| = {nstr(cms[-1], 4, strip_zeros=False)}")
        print(f" not used: m = {m}, |cm| = {nstr(cm, 4, strip_zeros=False)}")

        # ATTENTION ! nstr supprime trailing zeros par défaut !!
        S_string = nstr(S, nboffigures + 3, strip_zeros=False)
        # print last digits + 3 more
        print(f"Last digits are {S_string[-12:-3]}({S_string[-3:]})")

        print(f"K({b}, {Elist}) rounded to {nboffigures} significant figures is:")

    # return result as a string with a total of nboffigures decimal digits
    if trunc:
        # we hope this gives correct truncation...
        return nstr(S, nboffigures + 6, strip_zeros=False)[:-6]
    else:
        return nstr(S, nboffigures, strip_zeros=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 4:
        K = kempner(int(sys.argv[1]), list(map(int, sys.argv[2].split(','))),
                    int(sys.argv[3]), int(sys.argv[4]))
        print(K)
    elif len(sys.argv) > 3:
        K = kempner(int(sys.argv[1]), list(map(int, sys.argv[2].split(','))),
                    int(sys.argv[3]))
        print(K)
    elif len(sys.argv) > 2:
        K = kempner(int(sys.argv[1]), list(map(int, sys.argv[2].split(','))))
        print(K)
    else:
        print("""
kempner(b, set of excluded digits[, nboffigures, ell, silent, trunc])
kempnerpos(b, set of excluded digits[, nboffigures, ell, silent, trunc])

They both compute the Kempner series for given excluded digits in base b.
- kempner() uses the alternating series, from AMM paper,
- kempnerpos() the positive series mentioned in Integers 2026 paper in the
  case of a single excluded digit.

The last parameters are optional:
- nboffigures (default 100): number of significant figures
- ell (default 3): the level parameter
- silent (False): whether to print extra info
- trunc (False): whether to truncate or round.

For use on command line: python kempner.py b d1,...,dn [nboffigures [ell]]
This will compute according to the alternating series.  Boolean optional
parameters can not be used.
"""
              )
