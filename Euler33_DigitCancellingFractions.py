#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 17:58:37 2017

@author: christophergreen
Digit cancelling fractions
Problem 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import itertools;

def assemble():
    #elems=['0','1','2','3','4','5','6','7','8','9'];
    twos=list(itertools.product('0123456789',repeat=2));
    #print(twos);
    #print("length of twos is",len(twos)); #--> 100
    i=0;
    while i<len(twos):
        twos[i]=(twos[i][0]+twos[i][1]); #change strings into ints
        i+=1
    twos=twos[10:]; #get rid of the single-digit ints
    #print(twos);
    #print("length of twos is",len(twos)); # --> length of twos is 90
    
    fracs=[];
    j=0;
    while j<90:
        k=0;
        while k<90:
            fracs.append(twos[j]+"/"+twos[k]);
            k+=1;
        j+=1;
    #print(fracs);
    #print("length of fracs is",len(fracs)) #--< length of fracs is 8100
    
    newfracs=[];
    m=0;
    while m<8100:
        holder=int(fracs[m][:2])/int(fracs[m][3:]);
        if holder<1:
            newfracs.append([fracs[m],holder]);
        m+=1;
    #print("length of newfracs is",len(newfracs)); #--> length of newfracs is 4005
    return newfracs

    
z=assemble();

def find_digit_cancelling_fractions(x):
    i=0;
    count=0;
    outputs=[];
    while i<4005:
        holder=x[i][0];
        #print("dealing with the frac",x[i][0]);
        intholder=int(holder[:2])/int(holder[3:]);
        #print("the intholder for this fraction is",intholder);
        if holder[4]!='0' and holder[1]==holder[3]: #no division by zero and 'inner' digits equal i.e. 49/98
            a=holder[0]+"/"+holder[4];
            inta=int(a[0])/int(a[2]);
            #print("the a alternative is",a,"and has value",inta);
            if intholder==inta:
                #print(intholder,"is the same as",inta,"from the orig frac",holder);
                outputs.append(holder);
                count+=1;
        i+=1;
    print("count is",count);
    print("the fractions that seem to be cancellable for digits are:",outputs);
    return outputs;

y=find_digit_cancelling_fractions(z); #-->
#the fractions that seem to be cancellable for digits are: ['16/64', '19/95', '26/65', '49/98']
# =(1/4)(1/5)(2/5)(1/2) = 2/200 = 1/100, so answer 100 CORRECT
