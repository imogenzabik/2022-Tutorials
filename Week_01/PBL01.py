# -*- coding: utf-8 -*-
"""
PBL1 Worksheet
"""
from math import *
import matplotlib.pyplot as plt
import numpy as np 

L = 1E-3 #mm
d = 5E-6 #um
k = 200 #W/mK
h = 1000 #W/m^2K
T_a = 293.15 #K
T_0 = 353.15 #K
T_4 = 343.15 #K

del_x = 0.25E-3 #mm

A = (pi*d*d)/4
P = pi*d
beta2 = (h*P)/(k*A)

print(beta2)

sigma = -2-(beta2*del_x*del_x)
print(sigma)

c1 = array([1,sigma,sigma,sigma,1])
M_cent = np.diag(c1)

c2 = array([1,1,1,0])
M_bot = np.diag(c2, -1)

c3 = array([0,1,1,1])
M_top = np.diag(c3,1)

M = M_cent+M_top+M_bot
print(M)

b = np.array([[(T_0-T_a),0,0,0,(T_4-T_a)]]).T

sol = np.linalg.solve(M,b)
print(sol)

lin_x = np.linspace(0,L,num=5)
plt.plot(lin_x,sol)
plt.title('Temperature vs Distance') # add title
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (K)')


def exact_theta(x):
    print(x)
    exact_sol_vec = []
    for i in x:
        beta = sqrt(beta2)
        theta_L = T_4-T_a
        theta_0 = T_0-T_a
        num = (theta_L * sinh(beta*i))+(theta_0*sinh(beta*(L-i)))
        den = sinh(beta*L)
        sol = num/den
        exact_sol_vec.append(sol)
    return exact_sol_vec

analyt_sol = exact_theta(lin_x)
print(analyt_sol)
plt.plot(lin_x,analyt_sol)

