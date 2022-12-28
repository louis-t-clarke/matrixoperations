# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 02:56:41 2022

@author: Louis
"""

def K(n): #creates clique of size n
    K = []
    for i in range(n):
        row = [1]*n
        row[i]=0
        K.append(row)
    return K

def One(a,b):
    K = []
    for i in range(a):
        row = [1]*b
        K.append(row)
    return K

def MatSym(M):
    row = -1
    for i in M:
        row += 1
        col = 0
        for j in i[:row]:
            M[col][row] = M[row][col]
            col += 1