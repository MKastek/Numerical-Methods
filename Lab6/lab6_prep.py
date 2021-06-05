import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation

u0 = [np.pi/2,0,np.pi/2,0]

tmax = 1000
N = 2000
t = np.linspace(0,tmax,N)
gamma = 0.1


def pendulum0(u, t):
    du = np.zeros(4)
    du[0] = u[1]
    du[1] = (-3*np.sin(u[0])-np.sin(u[0]-2*u[2])-2*np.sin(u[0]-u[2])*(u[3]**2+u[1]**2*np.cos(u[0]-u[2])))/(3-np.cos(2*u[0]-2*u[2]))
    du[2] = u[3]
    du[3] = (2*np.sin(u[0]-u[2])*(2*u[1]**2+2*np.cos(u[0])+u[3]**2*np.cos(u[0]-u[2])))/(3-np.cos(2*u[0]-2*u[2]))
    return du

wynik0 = odeint(pendulum0, u0, t)
theta0 = wynik0[:,0]
theta1 = wynik0[:,2]
print(wynik0)
x1 = np.sin(theta0)
y1 = -np.cos(theta0)
x2 = x1 + np.sin(theta1)
y2 = y1 - np.cos(theta1)

fig = plt.figure()

def update(i):
    plt.clf()
    plt.axis([-2,2,-2,2])
    plt.plot([0,x1[i]],[0,y1[i]])
    plt.plot([x1[i]],[y1[i]],'or')
    plt.plot([x1[i], x2[i]], [y1[i], y2[i]])
    plt.plot([x2[i]], [y2[i]], 'or')
anim = animation.FuncAnimation(fig, update, frames = N, interval = 20)
plt.show()
