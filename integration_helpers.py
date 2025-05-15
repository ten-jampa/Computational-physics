## This python file contains the script and the helper functions for doing numerical integration

#packages needed
import numpy as np

def trapezoidal_rule_continous(function, N, a, b):
    x = np.linspace(a,b,N)
    h = x[1] - x[0]
    f = function(x)
    sum = 0.5*h*(f[0] + f[-1] + 2*np.sum(f[1:N]))
    return sum

def trapezoidal_rule_discrete(x, y):
    h = x[1] - x[0]
    N = len(y)
    sum = 0.5 * h *(y[0] + y[-1] + 2*np.sum(y[1:N]))
    return sum

def simpsons_rule_continous(function, N, a, b):
    x = np.linspace(a,b,N)
    y = function(x)
    h = x[1] - x[0]
    sum = (h/3)*(y[0] + y[-1] + 4*np.sum(y[1:N:2]) + 2*np.sum(y[2:N:2]))
    return sum

def simpsons_rule_discrete(x, y):
    h = x[1] - x[0]
    sum = (h/3)*(y[0] + y[-1] + 4*np.sum(y[1:N:2]) + 2*np.sum(y[2:N:2]))
    return sum


def adaptive_trapezoidal_rule(function, N0, a, b, e = 1e-6):
    I = [] #placeholder for integrations with different N
    N = N0
    I.append(trapezoidal_rule_continous(function, N, a, b)) #for i = 0
    N = 2*N0
    I.append(trapezoidal_rule_continous(function, N, a,b)) #for i = 1
    err = (1/3)*abs(I[-1] - I[-2]) #error estimation
    #conditional logic starts here
    while err > e:
        N = 2*N
        x = np.linspace(a,b,N)
        y = function(x)
        h_i = x[1] - x[0]
        sum = h_i * np.sum(y[1:N:2])
        I_i = 0.5*I[-1] + sum
        I.append(I_i)
        err = (1/3)*abs(I[-1] - I[-2])

    return I[-1], N, err

def adaptive_simpsons_rule(function, N0, a, b, e = 1e-6):
    I = [] #placeholder for integrations with different N
    N = N0
    I.append(simpsons_rule_continous(function, N, a, b)) #for i = 0
    N = 2*N0
    I.append(simpsons_rule_continous(function, N, a,b)) #for i = 1
    err = (1/15)*abs(I[-1] - I[-2]) #error estimation
    #conditional logic starts here
    while err > e:
        N = 2*N
        x = np.linspace(a,b,N)
        y = function(x)
        h_i = x[1] - x[0]
        S_i = (1/3)*(y[0] + y[-1] + 2*np.sum(y[2:N:2]))
        T_i = (2/3)*np.sum(y[1:N:2])
        I_i = h_i*(S_i + 2*T_i)
        I.append(I_i)
        err = (1/15)*abs(I[-1] - I[-2])

    return I[-1], N, err

def interpolating_polynomial(k, x, x_m):
    x_m_copy = x_m[:]
    xk = x_m_copy[k - 1]
    x_m_copy = np.delete(x_m_copy, k-1)
    result = []
    for x_val in x:
        result.append(np.prod((x_val-x_m_copy)/(xk - x_m_copy)))
    return np.array(result)

def get_wk(x_s, a, b, k):
    N = len(x_s) #x_s is the array of sample points
    x = np.linspace(-1, 1, N) 
    h = x[1] - x[0]
    y = interpolating_polynomial(k, x, x_s) 
    wk = (h/2)*(y[0] + y[-1] + 2*np.sum(y[1:N:2]))
    wkprime = 0.5*(b-a) *wk
    return wkprime