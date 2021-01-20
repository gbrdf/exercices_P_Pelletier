# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:39:25 2021

@author: guillaume
"""

#GROUPE 13 : ZIZIC NIKOLA / JEANNEAU LUCAS / BURDLOFF GUILLAUME

#EXERCICE 1 : MULTIPLES OF 3 OR 5 : 
  

base = 0 

for i in range (1 , 1000 ):
    if i % 3 == 0 or i % 5 == 0:
        
        base +=i                        #on somme tous les i dont la divison par 3 ou 5 donne un reste nul , i se trouvant dans l'intevalle [1;1000]
        
print(base)        

    

#EXERCICE 2 : 10001st PRIME NUMBER : 


def nth_prime(nth):
 primes = list()
 i=1
 while len(primes)<nth:
    i+=1
    is_prime = True
    for j in range(2,(round(i/2)+2)):
        if i/j == round(i/j) and i!=j:
            is_prime = False

        if is_prime == False:
            break
    if is_prime == True : 
        primes.append(i)

 print(primes[nth-1])
 
nth_prime(1)                            #test de la fonction nth_prime définie ci-dessus.

print(nth_prime(10001))



#EXERCICE 3 : Nombre de dimanche tombés le premier du mois pendant le 21e siècle : du 01/01/1901 au 31/12/2000
    

import calendar                         #package calendar pour éviter les problèmes liés au mois de février

base=0

for i in range(1901,2001):              #range exclu la borne supp donc on construit range(1901 , 2001) et non pas range(1901 , 2000)
    for j in range(1,13):               #on fait de même pour les mois : 12 mois dans une année donc range (1 , 13 ) car 13 exclu 
        if calendar.weekday(i,j,1)==6:  #calendar.weekday ( year = i , month = j , day = 1 ) -> return day index with (0) = Monday and (6) = sunday 
            base+=1                     #on somme le nombre de f

print(base)


