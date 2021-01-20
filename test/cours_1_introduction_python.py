# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:56:00 2021

@author: guillaume
"""

#F5 to run the entire script

#F9 to run only a selected part of the script or the current lign

print(1+2)

a=[1,2,3]

print(a)

slice1=a[0:2]

print(slice1)


2+2

a=2+2

a

2==8

2+2

dict1={"a":1,"b":2,"c":3}

print(dict1["c"])

print(dict1["b"])



print("a" in dict1)

print(type(dict1)==dict)

import numpy as np #on importe le package numpy et l'on définit que on l'appelera par l'abréviation "np"


 
a1 = [1,2,3,4]

np.std(a1)


#diff types of variables in python : float / int / bool / str / complex ... 

#Vectors and Matrices 

#Dans Python l'élément principal est la liste et non pas le vecteur comme dans R

b=["a","b","c","d","e"]


b[0] # = 1
b[1] # = 2 ...

b[:5]
 

#modify lists

list(zip(a,b))


#zip permet de regrouper des éléments par paires 

#append permet d'ajouter un élément à une liste par exemple une variable
#extend permet de rajouter une extension définie à une liste : 
    
b.extend(["A","B","C"])

b.append(a1)

#une liste ajoutée dans une autre correspond à un seul élément


print(b)

del(b[-4])

del(b[-1])

#b.insert( position , [... ])

b.insert(3,"lettre c")

b

#possibilité de retiré des éléments au sein d'une liste en les mentionnant par leur nom ou leur indexe

b.remove("lettre c")

#une liste peut contenir toute sorte de varaibles et même des listes à part entière

#savoir à quelle position dans une liste se trouve un élément précis : 
    
b.index("c") #return 2

b[2] #return "c"

i = 1 

i += 6 #on ajoute 6 à i et la variable i n'est plus égale à 1 mais est maintenant égale à 7  

print(i)

# simplement écrire i + 6 renvoie 7 mais la variable i en tant que telle prend toujours la valeur 1 

#autre opérateurs : -= // /= // *= // %=




A = {"a": 10 , "b" : 20 , "c": 30 , "d" : 40 , "e" : 50 }

type(A)


A.keys()

A.values()

A.items()

A["a"] = 10.5 #modifier la val associée à la clé a dans le dictionnaire A

A.setdefault("DEF" , 100 )

B={"GHI" : 101 }

A.update(B)

A

set1 = {1,2,3,2,4}

set1 # le deuxieme 2 a "disparu"

#COURSE_1_PART_4 : CONTROL FLOW 

n = 3.3

#test nombre entier pair ou impair

if n != int(n): 
  print('n is not a integer')
elif  n%2 == 0 :
  print('n is an even number')
else:
  print('n is a odd number')
  

import random #importation du module random : create a random number generator 

total = 0

#écriture de la boucle 

while total < 10:   #condition : tant que "total" inférieur à 
  rnd = random.gauss(mu = 0, sigma = 1)    #random.gauss : on génère un nb aléatoire généré selon une distri gausienne ( loi normale )
  if rnd < 0:
    pass #si rnd < 0 : on génère un autre nombre aléatoire 
  else:
    total += rnd #si rnd est > 0 : on ajoute rnd à la valeur total , la valeur total est modifiée ( += )

total


