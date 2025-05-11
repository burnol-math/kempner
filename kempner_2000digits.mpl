# Maple input file
# run on the command line: "maple kempner_2000digits.mpl"
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
#
# This computes the classic Kempner sum with 2000 fractional digits The
# kempner() procedure in the first execution block is a variation regarding
# user interface from kempner_base10_all.mw, it prints computation time for
# some sub-processing.  It has a new argument its "nbkeptsums" which tells it
# how many partial sums to return
#
# Then the calling block prints out their last 7+3 digits to check if enough
# partial sums were computed and if output looks reasonable (perhaps we should
# have more guard digits)
#
#######################################################
# For explanatory comments see kempner_base10_all.mpl #
#######################################################
#
#
# The second execution block launches the computation
# 
# Enjoy!
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

kempner := proc(A,lev,Mmax,nbkeptsums)
    local x,starttime,endtime;
    global L0,L1,L2,L3,L4,N,level,thegammasums,theucoeffs;
    level := lev;
    N := nops(A);
    L0 := A; L1 := A;
    if 0 in A then L1 := subsop(1=NULL,L1) end if;
    L1 := map(x->1.*x,L1);
    L2 := map(thing,L1);
    if level = 3 then L3 := map(thing,L2) end if;
    # if level = 4 then L3 := map(thing,L2); L4 := map(thing,L3) end if;
    printf("%d gamma sums computed in... ",Mmax);  print();
    starttime := time();
        thegammasums := array(1..Mmax,[seq(add(a^(m-1),a=L1), m=1..Mmax)]);
    endtime := time();
    printf("%8.4f seconds", endtime-starttime); print();
    thegammasums[1] := N;
    forget(ucoeff);
    printf("%d moments computed in... ",Mmax);  print();
    starttime := time();
        theucoeffs := [seq(ucoeff(k),k=1..Mmax)];
    endtime := time();
    printf("%8.4f seconds", endtime-starttime); print();
    forget(partialsum);
    printf("%d partial sums computed in... ",Mmax);  print();
    starttime := time();
        x := seq(partialsum(K),K=Mmax-nbkeptsums+1..Mmax);
    endtime := time();
    printf("%8.4f seconds", endtime-starttime); print();
    return x;
end:

# THIS BLOCK LAUNCHES THE COMPUTATIONS
# 
# 
# 
Digits := 2005; nbdigits := 2000; Mmax:= 1000; nbkeptsums:=50;
starttime := time():
result := kempner([0,1,2,3,4,5,6,7,8],3,Mmax,nbkeptsums):
endtime := time():
printf("Last 7+3 digits of the last (truncated to %d+3 fractional digits) %d partial sums:\n", nbdigits, nbkeptsums);
seq(printf("%a -> %.3f\n",Mmax-nbkeptsums+j,
		frac(trunc(10^(nbdigits+3)*result[j])/10^10)*10^7), j=1..nbkeptsums);
print();
printf("Total computing time: %8.4f secondes\n",endtime-starttime); print();
printf("(nota bene: output next is truncated not rounded)\n");
print();
printf("K = %.*f\n",nbdigits,trunc(10^nbdigits*result[nbkeptsums])/10^nbdigits);	



# 
# 
# 
# 
