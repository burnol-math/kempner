"""Compute all 1021 Kempner series for base 10 and possible sets of
admissible digits.

- check kempner() and kempnerpos() give identical results for 105
  significant figures
- truncate fractional part to 100 decimal places and print them
  out to a file so that a simple diff with the 2012/2024 Maple
  produced file 'python_base10_all_out' can check if the results
  are exactly identical.

Author: Jean-François Burnol
Created: April 7, 2026

© Jean-François Burnol, 2026

This script is licensed under the
Creative Commons Attribution-ShareAlike 4.0 International License.
Full license text: https://creativecommons.org/licenses/by-sa/4.0/

ANY RE-USE OR PLAGIARIZING BY AN ARTIFICIAL INTELLIGENCE WITHOUT
PROPER ATTRIBUTION IS STRICTLY FORBIDDEN AND WILL GET PUNISHED

"""

from kempner import *

basetendgts = set(range(10))

f  = open("python_base10_all_out", 'w')

CR = "\n"

# truncate to 100 decimal places
def foo(s: str) -> None:
    L = s.split('.')
    return L[0] + '.' + L[1][:100]
    

# 1 admissible digit
for a in range(1, 10):
    E = basetendgts - {a}
    Kstr = kempner(10, E, 105, silent=True, trunc=True)
    Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
    assert Kstr == Kstrpos, f"Problem with excluded {E}"
    f.write(f"[{a}] -> " + foo(Kstr) + CR)
    print('1', end=' ', flush=True)

# 2 admissible digits
for a in range(10):
    for b in range(a + 1, 10):
        E = basetendgts - {a, b}
        Kstr = kempner(10, E, 105, silent=True, trunc=True)
        Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
        assert Kstr == Kstrpos, f"Problem with excluded {E}"
        f.write(f"[{a}, {b}] -> " + foo(Kstr) + CR)
        print('2', end=' ', flush=True)

# 3 admissible digits
for a1 in range(10):
    for a2 in range(a1 + 1, 10):
        for a3 in range(a2 + 1, 10):
            E = basetendgts - {a1, a2, a3}
            Kstr = kempner(10, E, 105, silent=True, trunc=True)
            Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
            assert Kstr == Kstrpos, f"Problem with excluded {E}"
            f.write(f"[{a1}, {a2}, {a3}] -> " + foo(Kstr) + CR)
            print('3', end=' ', flush=True)

# 4 admissible digits
for a1 in range(10):
    for a2 in range(a1 + 1, 10):
        for a3 in range(a2 + 1, 10):
            for a4 in range(a3 + 1, 10):
                E = basetendgts - {a1, a2, a3, a4}
                Kstr = kempner(10, E, 105, silent=True, trunc=True)
                Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
                assert Kstr == Kstrpos, f"Problem with excluded {E}"
                f.write(f"[{a1}, {a2}, {a3}, {a4}] -> " + foo(Kstr) + CR)
                print('4', end=' ', flush=True)

# 5 admissible digits
for a1 in range(10):
    for a2 in range(a1 + 1, 10):
        for a3 in range(a2 + 1, 10):
            for a4 in range(a3 + 1, 10):
                for a5 in range(a4 + 1, 10):
                    E = basetendgts - {a1, a2, a3, a4, a5}
                    Kstr = kempner(10, E, 105, silent=True, trunc=True)
                    Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
                    assert Kstr == Kstrpos, f"Problem with excluded {E}"
                    f.write(f"[{a1}, {a2}, {a3}, {a4}, {a5}] -> " + foo(Kstr) + CR)
                    print('5', end=' ', flush=True)

# 4 excluded digits = 6 admissible digits
# we organize this so that ordering of the output is done
# as the ordering used above for batches of 1, 2, 3, 4 or 5 
# admissible digits.
for e1 in range(6, -1, -1):
    for e2 in range(7, e1, -1):
        for e3 in range(8, e2, -1):
            for e4 in range(9, e3, -1):
                E = {e1, e2, e3, e4}
                A_sorted = sorted(basetendgts - E)
                Kstr = kempner(10, E, 105, silent=True, trunc=True)
                Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
                assert Kstr == Kstrpos, f"Problem with excluded {E}"
                f.write(f"{A_sorted} -> " + foo(Kstr) + CR)
                print('6', end=' ', flush=True)

# 3 excluded digits
for e1 in range(7, -1, -1):
    for e2 in range(8, e1, -1):
        for e3 in range(9, e2, -1):
            E = {e1, e2, e3}
            A_sorted = sorted(basetendgts - E)
            Kstr = kempner(10, E, 105, silent=True, trunc=True)
            Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
            assert Kstr == Kstrpos, f"Problem with excluded {E}"
            f.write(f"{A_sorted} -> " + foo(Kstr) + CR)
            print('7', end=' ', flush=True)

# 2 excluded digits
for e1 in range(8, -1, -1):
    for e2 in range(9, e1, -1):
        E = {e1, e2}
        A_sorted = sorted(basetendgts - E)
        Kstr = kempner(10, E, 105, silent=True, trunc=True)
        Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
        assert Kstr == Kstrpos, f"Problem with excluded {E}"
        f.write(f"{A_sorted} -> " + foo(Kstr) + CR)
        print('8', end=' ', flush=True)

# 1 excluded digit
for e1 in range(9, -1, -1):
    E = {e1}
    A_sorted = sorted(basetendgts - E)
    Kstr = kempner(10, E, 105, silent=True, trunc=True)
    Kstrpos = kempnerpos(10, E, 105, silent=True, trunc=True)
    assert Kstr == Kstrpos, f"Problem with excluded {E}"
    f.write(f"{A_sorted} -> " + foo(Kstr) + CR)
    print('9', end=' ', flush=True)

print()
print()
print("""\
All 1021 Kempner sums for base 10 computed to 105 rounded decimal
digits have given identical results for kempner() and kemperpos().
See file 'python_base10_all_out for the values, listed according
to the lists of admissible digits.  Use "diff" to compare with
data in file 'kempner_base10_all_out' produced by Maple.
""")

f.close()

