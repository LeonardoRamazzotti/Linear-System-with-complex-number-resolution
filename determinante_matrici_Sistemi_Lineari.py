#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:18:36 2021

@author: leonardo
"""
# Task: Devo fare ub programma che mi calcoli il determinante di una matrice complessa

controllo=input('Devi fare operazioni? (si/no) \n ')

while controllo =='si':

    n_R=int(input('Quante righe ha la matrice? '))
    n_C=int(input('Quante colonne ha la matrice? '))

    n_it= n_R*n_C # moltiplico per trovare il numero di elementi della matrice

    lista=[] 

    index=0

    while index< n_it:
        z=complex(input('Inserisci un numero (anche complesso): (R+Ij)\n\n'))
        lista.append(z)  # Aggiungo il numero a una lista per poi manipolarlo
        index +=1
        continue

    matrice=[]

    import numpy as np

    x=np.array(lista) # prendo la lista di numeri e la trasformo in un vettore
    m=np.reshape(x,[n_R,n_C]) # trasformo il vettore in una matrice 
                
    print('Matrice da manipolare: \n\n ',m,'\n\n')



    det=np.linalg.det(m) # libreria numpy determinante

    print('Determinante: \n\n',det)

    quest=input('Devi risolvere una equazione lineare? ')

    if quest=='si':
    
        ter_noti=[] 

        index=0

        while index< n_R:
            t=complex(input('Inserisci un numero (anche complesso): (R+Ij)\n\n'))
            ter_noti.append(t)  # Aggiungo il numero a una lista per poi manipolarlo
            index +=1
            continue
    
        b=np.array(ter_noti)  
        m_t=np.reshape(b,[n_R,1]) # trasformo il vettore in una matrice
    
        i=np.linalg.inv(m).dot(m_t)
    
        print('La soluzione del sistema lineare : \n\n',i)
    
        import cmath
        import math
   
        indice=0
        print('Le soluzioni in fasori del sistema lineare sono: \n')
        for element in i:
            element=i[indice][0]
            i_f=cmath.polar(element)
            tetha=math.degrees(i_f[1]) # definisco l'angolo in gradi
            indice+=1
            print(i_f[0],',',tetha)

    controllo=input('Devi fare operazioni? (si/no) \n ')
    
    if controllo=='si':
    
        mem_m=input('Vuoi riutilizzare la stessa matrice? (si/no) \n')
    
        while mem_m=='si':
            print('La matrice risulta essere: \n \n ',m)
        
            ter_noti=[] 

            index=0

            while index< n_R:
                t=complex(input('Inserisci un numero (anche complesso): (R+Ij)\n\n'))
                ter_noti.append(t)  # Aggiungo il numero a una lista per poi manipolarlo
                index +=1
                continue
    
            b=np.array(ter_noti)  
            m_t=np.reshape(b,[n_R,1]) # trasformo il vettore in una matrice
    
            i=np.linalg.inv(m).dot(m_t)
    
            print('La soluzione del sistema lineare : \n\n',i)
    
            import cmath
            import math
   
            indice=0
            print('Le soluzioni in fasori del sistema lineare sono: \n')
            for element in i:
                element=i[indice][0]
                i_f=cmath.polar(element)
                tetha=math.degrees(i_f[1]) # definisco l'angolo in gradi
                indice+=1
                print(i_f[0],',',tetha)
            
            controllo=input('Devi fare operazioni? (si/no) \n ')
            mem_m=input('Vuoi riutilizzare la stessa matrice? (si/no) \n')
        
    
            
    
input('Press any button to quit.')



