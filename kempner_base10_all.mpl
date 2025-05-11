# Maple input file
# run on the command line: "maple kempner_base10_all.mpl"
#
# Originally done in January 2012, minimally adapted (translated)
# in February 2024.  NO CHECK WAS DONE whether coding was
# reasonably efficient: the authors is NO expert of Maple data
# types and uses it only occasionally.
#
# It was only checked compilation still works as expected.
#
# Copyright (c) Jean-François Burnol 2012, 2024
# License: CC BY-SA https://creativecommons.org/licenses/by-sa/4.0/
#
# This computes all 1021 Kempner like sums for base b=10, with 100
# digits Of all 1024 subsets A of {0,1,...,9}, the empty set, the
# singleton {0} and the full set are excluded, hence 1021.
#
# The computations are done with Maple configured to use 110
# decimal digits.  Only 100 fractional digits are printed in the
# end.
#
# The computing procedure is called kempner(A, lev, Mmax), it is a
# direct implementation of the main formula, and has three
# arguments
#
# A is our set of allowed digits lev is the l in the main theorem
# Mmax is the maximal m-1 used, see below for the shift by 1.  It
# means that Mmax-1 terms of the alternating series are used
# starting with u_1, which here will be coeffsu[2]
#
# All arrays are indexed from 1 to Mmax which is set by the caller
#
# The procedure theucoeffs[m], m at least 1, corresponds to
# u_{m-1} in the paper.  The array entries are filled by call to a
# recursive procedure "ucoeff" using "remember"
#
# thegammasums[j] corresponds to gamma_{j-1} in the paper
# attention to the shift! Only gamma_1, etc... are used so j at
# least 2 in the recursion formula theucoeff
#
# betasum(K) is a procedure which returns the inverse power sums
# beta_{l,K} from the paper
#
# partialsum(K) is a recursive procedure alos using "remember" and
# which for K=1 computes the initial contribution from digits of
# length up to the level, then starting with K=2 adds the
# alternating series contributions (thus starting at m=1 and going
# to m=Mmax-1)
#
# thing(L) is a procedure which replaces each entry x in L by the
# 10*x+j for j the admissible digits The admissible digits are the
# elements from a global variable L0 which is set at start of
# kempner to be its first argument A

# kempner() starts by declaring global variables L1, L2, L3, L4
# which are floating point representations of the integers at
# levels 1, 2, 3, 4
#
# Then it computes the array of gammasum's matching A (which now,
# apart from 0, gave L1)
#
# Then it fills up the ucoeff[] array using calls to the
# "theucoeff" recursive with memory procedure
#
# Then it computes the partialsum(K) in a way keeping the last 4
# of them in an array
# A test is made that the 100 fractional digits of these last 4
# partial sums are identical.
# If test is positive the result is printed.
# If test is negative the last sum is printed as well as the last
# 3 digits of of the 3 preceding sums and we word "doubt" is
# printed
#
# This is it for kempner()
#
# The second execution block is a loop generating all possible A's
# and executing kempner(A, 2 or 3, Mmax = 110, respectively 55)
#
# Some timing data is also gathered and printed.
#
# Enjoy!
#
# Attention that N, L0, L1, L2, L3 and level are defined as global
# variables to avoid passing arguments in sub-functions which is
# bad style
#
#
# THIS BLOCK DEFINES THE kempner() PROCEDURE AND AUXILIARIES
# ATTENTION THAT GLOBAL VARIABLES ARE USED BY kempner()
#
#
restart; with(combinat,choose):
ucoeff := proc(k)
    option remember;
    if k = 1 then
        10/(10-N)
    else
        add(binomial(k-1,u-1)*thegammasums[k-u+1]*ucoeff(u),u=1..k-1)/(10^k - N)
    end if
end proc:

betasum := proc(K)
    add(1/b^K,b=L||level)
end:

partialsum := proc(K)
    option remember;
    if K = 1 then
        add(add(1/n,n=L||j),j=1..level-1) + 10/(10-N)*add(1/n,n=L||level)
    else
        partialsum(K-1) + (-1)^(K-1)*theucoeffs[K]*betasum(K)
    end if
end:

thing := proc(list)
    map(x->seq(10*x+j,j = L0),list)
end:

kempner := proc(A,lev,Mmax)
    local test,lastpartialsums;
    global L0,L1,L2,L3,L4,N,level,thegammasums,theucoeffs;
    level := lev;
    N := nops(A);
    L0 := A; L1 := A;
    if 0 in A then L1 := subsop(1=NULL,L1) end if;
    L1 := map(x->1.*x,L1);
    L2 := map(thing,L1);
    if level = 3 then L3 := map(thing,L2) end if;
    # if level = 4 then L3 := map(thing,L2); L4 := map(thing,L3) end if;
    thegammasums := array(1..Mmax,[seq(add(a^(m-1),a=L1), m=1..Mmax)]);
    thegammasums[1] := N;
    forget(ucoeff);
    theucoeffs := [seq(ucoeff(k),k=1..Mmax)];
    forget(partialsum);
    lastpartialsums := array(Mmax-3..Mmax,[seq(partialsum(K),K=Mmax-3..Mmax)]);
    test := add(abs(trunc(10^nbdigits*lastpartialsums[Mmax+j])-trunc(10^nbdigits*lastpartialsums[Mmax+j-1])),j=-2..0):    
    if (test=0) then
        return [A,lastpartialsums[Mmax],test];
    else
        return [A,lastpartialsums[Mmax],test,[seq(10^3*frac(trunc(10^nbdigits*lastpartialsums[Mmax+j])/10^3),j=-3..0)]];        
    end if;
end:

# THIS BLOCK LAUNCHES THE COMPUTATIONS
# TIMINGS ARE SHOWN AND RESULTS PRINTED ONLY AT END
# 
# 
Digits := 110: nbdigits := 100:
printf("Digits=%d, \nOutput truncated to %d fractional digits\n\n", Digits, nbdigits);
starttime := time():
for k from 1 to 9 do
    subduration[k] := time():
    mega := choose([0,1,2,3,4,5,6,7,8,9],k):
    if k=1 then mega := subsop(1=NULL, mega): end if: 
    if k<8 then
        printf("Computing with level 3 for all A's of cardinality %d... (will be displayed later)",k);print();
        thekempnersums[k] := seq(kempner(L,3,55),L=mega):
    else
        printf("Computing with level 2 for all A's of cardinality %d...",k);print();
        thekempnersums[k] := seq(kempner(L,2,105),L=mega):
    end:
    subduration[k] := time() - subduration[k]:
    printf("        done in %7.4f seconds for %d Kempner sums (%.6f seconds per sum)\n", 
           subduration[k], nops(mega), subduration[k]/nops(mega));print();
end do: print();
endtime := time():
for k from 1 to 9 do
    for result in thekempnersums[k] do
        printf("%a -> %.*f",result[1],nbdigits,trunc(10^nbdigits*result[2])/10^nbdigits):
        if (result[3]=0) then
            printf("\n"):
        else
            printf("\nWARNING sum for %a may have been computed with too few terms (",result[1]):
            for x in result[4] do printf(" %d", x): end do:
            printf(" )\n"):
        end if;
    end do:
end do:
printf("Total computing time: %07.4f seconds\n",endtime-starttime);
for k from 1 to 9 do
    printf("k=%d: %7.4f seconds (%.6f seconds per sum)\n",k,subduration[k],subduration[k]/nops([thekempnersums[k]])):
end do:
# 
# 
# 
# 
