from turtle import *

def e(matka):
    forward(matka)

def o(kulma):
    right(kulma)

def v(kulma):
    left(kulma)

def mk(koko, kulmat):
    for i in range(kulmat):
        e(koko)
        v(360/kulmat)
