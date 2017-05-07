# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
    if (b*b-4*a*c)>=0:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1,x2
    else:
        return 'error'