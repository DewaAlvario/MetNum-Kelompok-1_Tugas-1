# -*- coding: utf-8 -*-
"""Kelompok 1_Akar_PersNLinier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmLzqQUevAov6PPLhERlwyRTJK6XIquD

## **Akar Persamaan Non-Linier**
Berikut ini merupakan fungsi dasar dari metode yang dapat digunakan untuk mencari akar Persamaan non-Linier

**Pencarian Akar dengan Library**

Contoh Fungsi: f(x) = cos(x)-x
"""

import numpy as np
from scipy import optimize
f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -2)
print("r =",r)
# Verify the solution is a root
result = f(r)
print("result=", result)

"""**Metode Bagi Dua**"""

import numpy as np #panggil library
def my_bisection(f, a, b, e):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b')
  m = (a + b)/2
  if np.abs(f(m)) < e:
    return m
  elif np.sign(f(a)) == np.sign(f(m)):
    return my_bisection(f, m, b, e)
  elif np.sign(f(b)) == np.sign(f(m)):
    return my_bisection(f, a, m, e)

"""**Contoh Pencarian Akar dengan Metode Bagi Dua**

f(x)=x^2 - 2
"""

import numpy as np #panggil library
f = lambda x: x**2-2

r1 = my_bisection(f, 0, 2, 0.1)
print("r1 =", r1)
print("f(r1) =", f(r1))

r01 = my_bisection(f, 0, 2, 0.01)
print("r01 =", r01)
print("f(r01) =", f(r01))

import numpy as np #panggil library
f = lambda x: x**2-2
my_bisection(f, 2, 4, 0.01)

"""**Metode Newton-Raphson**"""

import numpy as np #panggil library
def my_newton(f, df, x0, e):
# output is an estimation of the root of f
# using the Newton-Raphson method
# recursive implementation
  if abs(f(x0)) < e:
    return x0
  else:
    return my_newton(f, df, x0 - f(x0)/df(x0), e)

"""**Contoh Pencarian Akar dengan Metode Bagi Dua**

f(x)=x^2 - 2
"""

f = lambda x: x**2-2
f_prime = lambda x: 2*x
estimate = my_newton(f, f_prime, 1.5, 1e-6)
print("estimate =", estimate)
print("sqrt(2) =",np.sqrt(2))

"""# **Latihan**

**No.1 **
Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua maupun Newton Raphson ketika 

a. f(x) = x^3 - 2x + 1

b. f(x) = e^x - x

**No 2**

Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n baik untuk Bagi Dua maupun Newton Raphson

Metode Bagi Dua:
"""

import numpy as np #panggil library
a = 0
b = 1.0
fa = a**3-2*a+1
fb = b**3-2*b+1

#kondisi jika tidak memiliki akar
if fa*fb>0:
    print ('persamaan tidak memiliki akar')
    exit
    
for i in range (1,101):
    x = (a+b)/2
    fx = x**3-2*x+1
    fa = a**3-2*a+1
    if abs(fa) < 1.0e-6:
        break
    elif fa*fx < 0:
        b=x
    else:
        a=x
        
print ('Akar: %.3f' %a)

import numpy as np #panggil library
e = 2.71828 
a = 100
b = -10
fa = e**a-a
fb = e**b-b

#kondisi jika tidak memiliki akar
if fa*fb>0:
    print ('persamaan tidak memiliki akar')
    exit
else:
  for i in range (1,101):
    x = (a+b)/2
    fx = e**x-x
    if abs(fa) < 1.0e-6:
        break
    elif fa*fx < 0:
        b=x
    else:
        a=x
    print ('Akar:%.3f' %a)

"""Metode Newton Raphson"""

from sympy import symbols, diff

x = symbols("x")
 
f = x**3-2*x+1  
x0 = -2

for i in range(n):
    x0 = x0 - float(f.subs(x, x0) / diff(f, x).subs(x, x0))
 
print("Akar: %.3f " %x0)

from math import e
from sympy import symbols, diff
x = symbols("x")
e = 2.71828   

f = e**x-x 
x0 = 0
n = 10
 
for i in range(n):
    x0 = x0 - float(f.subs(x, x0) / diff(f, x).subs(x, x0))
 
print("Akar: %.3f " %x0)

"""contoh lain"""

import numpy as np
#import matplotlib.pyplot as plt

pers = input("Masukkan persamaan fungsi x : ")
a = float(input("Masukkan nilai a : "))
b = float(input("Masukkan nilai b : "))
e = 1e-5 #error

print("Akar persamaan adalah ", a, " dan ", b)

def f(x) :
  return eval(pers) 

if f(a)*f(b)>0:
  print("persamaan tidak memiliki akar")
else :
  print("n \t   a  \t\t b \t\t  xn  \t\t  f(a)  \t  f(b)  \t f(xn)")
  for i in range(10):
    x = (a+b)/2
    print (i+1, "\t", format(a, ".5f"), "\t", format(b, ".5f"), "\t", format(x, ".5f"), "\t", format(f(a), ".5f"), "\t", format(f(b), ".5f"), "\t", format(f(x), ".5f"))
    if abs (f(x))<=e:
      break;
    elif f(a)*f(x)<=0 :
      b = x
    else :
      a=x

print ("Akar persamaannya adalah = ", a, " dan ", b)