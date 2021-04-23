#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:18:36 2021

@author: leonardo
"""
# Task: Devo fare ub programma che mi calcoli il determinante di una matrice complessa

controllo=input('You have to do something? (y/n) \n ')

while controllo =='y':

    n_R=int(input('How many rows does the matrix have? '))
    n_C=int(input('How many columns does the matrix have? '))

    n_it= n_R*n_C # moltiplico per trovare il numero di elementi della matrice

    lista=[]

    index=0

    while index< n_it:
        z=complex(input('Enter a value (even copmlex): (R+Ij)\n\n'))
        lista.append(z)  # Aggiungo il numero a una lista per poi manipolarlo
        index +=1
        continue

    matrice=[]

    import numpy as np

    x=np.array(lista) # prendo la lista di numeri e la trasformo in un vettore
    m=np.reshape(x,[n_R,n_C]) # trasformo il vettore in una matrice

    print('Matrix to manipulate: \n\n ',m,'\n\n')



    det=np.linalg.det(m) # libreria numpy determinante

    print('Determinant: \n\n',det)

    quest=input('You have to solve a linear system? (y/n) ')

    if quest=='y':

        ter_noti=[]

        index=0

        while index< n_R:
            t=complex(input('Enter a value (even complessalex): (R+Ij)\n\n'))
            ter_noti.append(t)  # Aggiungo il numero a una lista per poi manipolarlo
            index +=1
            continue

        b=np.array(ter_noti)
        m_t=np.reshape(b,[n_R,1]) # trasformo il vettore in una matrice

        i=np.linalg.inv(m).dot(m_t)

        print('Solution of the linear system : \n\n',i)

        import cmath
        import math

        indice=0
        print('Solution of the linear system in phasors: \n')
        for element in i:
            element=i[indice][0]
            i_f=cmath.polar(element)
            tetha=math.degrees(i_f[1]) # definisco l'angolo in gradi
            indice+=1
            print(i_f[0],',',tetha)

    controllo=input('You have to do something? (y/n) \n ')

    if controllo=='y':

        mem_m=input('Do you want to reuse the same matrix? (y/n) \n')

        while mem_m=='y':
            print('Matrix : \n \n ',m)

            ter_noti=[]

            index=0

            while index< n_R:
                t=complex(input('Enter a value (even complessalex): (R+Ij)\n\n'))
                ter_noti.append(t)  # Aggiungo il numero a una lista per poi manipolarlo
                index +=1
                continue

            b=np.array(ter_noti)
            m_t=np.reshape(b,[n_R,1]) # trasformo il vettore in una matrice

            i=np.linalg.inv(m).dot(m_t)

            print('Solution of the linear system : \n\n',i)

            import cmath
            import math

            indice=0
            print('Solution of the linear system in phasors: \n')
            for element in i:
                element=i[indice][0]
                i_f=cmath.polar(element)
                tetha=math.degrees(i_f[1]) # definisco l'angolo in gradi
                indice+=1
                print(i_f[0],',',tetha)

            controllo=input('You have to do something? (y/n) \n ')
            mem_m=input('Do you want to reuse the same matrix? (y/n) \n')




input('Press any button to quit.')
