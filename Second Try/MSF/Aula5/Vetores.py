# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:22:52 2022

@author: draki
"""
import numpy as np

def produto_escalar(vetor1, vetor2):
    return (vetor1[0]*vetor2[0]+vetor1[1]*vetor2[1])

def intesidade(vetor):
    return (np.sqrt(vetor[0]**2 + vetor[1]**2))

def vetorunit(vetor):
    comprimento = intesidade(vetor)
    unitvec = [vetor[0]/comprimento, vetor[1]/comprimento]
    print("intesidade do vetor unitario", intesidade(unitvec))
    if round(intesidade(unitvec)) == 1:
        print("Comprimento =", comprimento, "e o vetor unitario é", unitvec)
    else:
        print("something went wrong")

def getangle(vetor1, vetor2):
    intesitivec1 = intesidade(vetor1)
    intesitivec2 = intesidade(vetor2)
    escalar = produto_escalar(vetor1, vetor2)
    angle = np.arccos(escalar/(intesitivec1*intesitivec2))
    print("intesidade vetor1", vetor1, "=", intesitivec1)
    print("intesidade vetor2", vetor2, "=", intesitivec2)
    print("produto escalar = ", escalar)
    print("angulo =", angle*(180/np.pi), "º (", angle, "radians )")

    
#---------------------------------------------------------------------------------------------------------------#


#1
#vec = np.array([3,4])
#print(intesidade(vec))
#vetorunit(vec)
#vec2 = 2*vec
#print(intesidade(vec2))
#---------------------------------------------------------------------------------------------------------------#


#2
#vec1 = np.array([1,2])
#vec2 = np.array([-2,3])
#getangle(vec1,vec2)


#---------------------------------------------------------------------------------------------------------------#



#3
#vec1 = np.array([1,2])
#vec2 = np.array([-2,1])
#getangle(vec1,vec2)


#---------------------------------------------------------------------------------------------------------------#


#4
#vec = np.array([3,4]) 
#vec2 = np.array([-4,3])  
#print(produto_escalar(vec,vec2))


#---------------------------------------------------------------------------------------------------------------#


#5
#vec = np.array([2,1.2]) 
#vec2 = np.array([-3,5.1])  
#vec3 = vec+vec2
#print(vec3)
#print(intesidade(vec3))


#---------------------------------------------------------------------------------------------------------------#


#6
#vecy = np.sqrt(6**2-2**2)
#vec = np.array([2,vecy])
#print(intesidade(vec))
#print(vecy)

#---------------------------------------------------------------------------------------------------------------#

    
#7
#vec2 = [2,2*np.sqrt(3)]
#vec = [2,0]
#getangle(vec, vec2)   
     