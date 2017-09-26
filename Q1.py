#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:14:36 2017

@author: admin
"""

from pylab import*

def Q1():
    
    t = linspace(0, 4, 1000)
    
    dt = 0.01
    
    def x(t):
        return t**4 - 4*t**3 + 2*t**2 + 3*t + 6
    
    def v(t):
        return 4*t**3 - 12*t**2 + 4*t + 3
    
    def a(t):
        return 12*t**2 - 24*t + 4
        
    def jerk(t):
        return 24*t - 24
        
    fx = x(t)
    fv = v(t)
    fa = a(t)
    fj = jerk(t)
    def Q1Figure():
        
        figure('Question 1')
        clf()
        subplot(411)
        plot(t, fx)
        grid()
        ylabel('x(t)')
        xlabel('t')
        
        subplot(412)
        plot(t, fv)
        grid()
        ylabel('v(t)')
        xlabel('t')
        
        subplot(413)
        plot(t, fa)
        grid()
        ylabel('a(t)')
        xlabel('t')
        
        subplot(414)
        plot(t, fj)
        grid()
        ylabel('jerk(t)')
        xlabel('t')
        
        return True
    
    Q1Figure()

    return True

Q1()
