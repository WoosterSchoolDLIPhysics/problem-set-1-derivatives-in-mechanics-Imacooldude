#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:30:25 2017

@author: admin
"""

from pylab import *

from pylab import *



#def x(t):
#   x=3*sin(2*pi*t)
#   return x

#def y(t):
#   y=2*cos(2*pi*t)
#   return y

#dt=.01

#t=arange(0,1+dt,dt)    
    
#clf()
#plot(x(t),y(t),'r')


t = linspace(0,1,100)

x= 3*sin(2*pi*t)
y =2* cos(2*pi*t)
vx= 6*pi*cos(2*pi*t)/5
vy=-4*pi*sin(2*pi*t)/5
ax= -12*pi*pi*sin(2*pi*t)/5
ay=-8*pi*pi*cos(2*pi*t)/5


figure(1)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y)
    plot([0,x[it]],[0,y[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)
   
    
    
    plot(vx,vy)
    plot([0,vx[it]],[0,vy[it]],'r-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*vx[it],1.2*vy[it],r'$\vec{x}$',color='red',size=15)
   
    
    
    plot(ax,ay)
    plot([0,ax[it]],[0,ay[it]],'g-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*ax[it],1.2*ay[it],r'$\vec{x}$',color='green',size=15)

   
    #savefig('frame_%03d.png' % it)
    grid()
    pause(.001)