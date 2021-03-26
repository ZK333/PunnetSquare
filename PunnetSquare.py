# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 14:22:25 2021

@author: zsrgr
"""
# Zarik Khan
# Enter a dominant trait and a recessive trait, and get the percentages of 
# particular genotype 

print("Please enter 2*2 cross of two genotypes")
print("Enter as cross(ex Tt*tt or Xx*Xx, with no spaces between anything") 
punnet = input()
i =0 # iterates through loop

c1 = punnet[0]+"" #c1, and c2 will form the first cross
c2 = punnet[1] +""
c3 = punnet[3]+"" ## c3 and c4 will form the second cross
c4 = punnet[4]+""

d1 =0 ## stores the amount of dominant alleles in the first cross
d2= 0 ## stores the amount of dominant alleles in the second cross
sum = 0

if c1==c2:
    if c1==c1.lower():
        d1 = 0
    else:
        d1= 2
else:
 d1=1


if c3==c4:
    if c3==c3.lower():
        d2 = 0
    else:
        d2= 2
else:
 d2=1


sum = d1+d2
c1  = c1.replace("  ","")
c2=c2.replace("  ","")

if d1==d2==1:
  print("50% chance the offspring's genotype will be ",c1.upper(),c2.lower())
  print("25% chance the offspring's genotype will be ",c1.upper(),c2.upper())
  print("25% chance the offspring's genotype will be ",c1.lower(),c2.lower())
  
if sum==4:
  print("100% chance the offspring's genotype will be ",c1.upper(),c2.upper())

if sum==0:
      print("100% chance the offspring's genotype will be ",c1.lower(),c2.lower())
      
if abs(d2-d1)==2:
      print("100% chance the offspring's genotype will be ",c1.upper(),c2.lower())
      
if sum==1:
      print("50% chance the offspring's genotype will be ",c1.upper(),c2.lower())
      print("50% chance the offspring's genotype will be ",c1.lower(),c2.lower())
      
if sum==3:
  print("50% chance the offspring's genotype will be ",c1.upper(),c2.upper())
  print("50% chance the offspring's genotype will be ",c1.upper(),c2.lower())
