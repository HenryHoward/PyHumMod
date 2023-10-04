from scipy.optimize import fsolve  # used for solving implicit equations
from scipy.interpolate import CubicHermiteSpline # used for the splines
import numpy as np

def backwardeuler(f1, f2, delta_t, y0):
    '''
    uses the right handed rectangle method to iterate the next value in a differential equation
    f1 and f2 are all that is needed to define the differential equation in HUMMOD. the differential equation is: y = integral(f1-f2*y)

    returns:
    the next y value
    '''

    #NOTE: this is almost certainly an incorrect, nonsense implementation
    
    y1 = y0/(1-delta_t*(f1-f2)) #???
    return y1

def diffeq(dydx, delta_t, y0):
    '''
    euler method for estimating the next value of a differential equation
    f is the gradient function for y: dy/dx

    returns a list of subsequent y values
    '''

    y1 = y0+delta_t*dydx
    return y1

def delay(K, A, B_pre, delta_t):
    '''
    for a given change in time, B steps closer to A. It moves more the further away it is and the greater K is

    B = K * (A - B_init) * delta_t

    '''
    B_post = B_pre + K * (A - B_pre) * delta_t
    return B_post

def stablediffeq(f, delta_t, y0, max_delta_t, n=1):
    '''
    currently just a diffeq until I figure out how they're meant to be different
    '''
    return diffeq(f, delta_t, y0, n=1)

def impliciteq(f, y_start_estimate, error_limit):
    '''
    Finds x so that
        | x - f(x) | <= Error Limit
    '''
    def f_equal_0(y):
        return y-f(y)
    root = fsolve(f_equal_0, y_start_estimate, xtol=error_limit)
    if len(root) == 1:
        return root[0]
    else:
        raise Exception("multiple roots:", root)

def cubic_hermite_spline(x, xarray, yarray, slopes):
    '''
    the curves in HumMod appear to be Cubic Hermite Splines (curves defined by a set of x,y coords and a slope at each point)

    uses scipy.interpolate.CubicHermiteSpline

    input:
        xarray and yarray and slopes are lists of the same length, they are the x and y coordinates and associated slopes
    '''
    if x<=xarray[0]:
        return(yarray[0])
    if x>=xarray[-1]:
        return(yarray[-1])
    else:
        curve = CubicHermiteSpline(xarray, yarray, slopes)
        return curve(x)

