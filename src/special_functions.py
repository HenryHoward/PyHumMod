# these are imported using eg.: from PyHumMod.special_functions import diffeq

from scipy.optimize import fsolve  # used for solving implicit equations
from scipy.interpolate import CubicHermiteSpline # used for the splines
import numpy as np


def analytic_backwardeuler(f1, f2, delta_t, y0, n=1):
    '''
    the solution to a differential equation dy/dt = ay with initial value y0 is:

        y = y0*e^(a*t)

    all the equations in HUMMOD solved with backwardeuler are of this form, where a is (f1-f2) where f1 and f2 are scalars
    '''
    vals = [y0]
    t = 0
    for iter in range(0, n):
        vals.append(y0*2.718281828459045**((f1-f2)*t))
        t += delta_t
    if n == 1:
        return vals[1]
    else:
        return vals[1:]


def backwardeuler(f1, f2, delta_t, y0):
    '''
    uses the right handed rectangle method to iterate the next value in a differential equation
    f1 and f2 are all that is needed to define the differential equation in HUMMOD. the differential equation is: y = integral((f1-f2)*y)

    causes an error when delta_t*(f1-f2) = 1

    returns a list of subsequent y values
    '''
    
    y1 = y0/(1-delta_t*(f1-f2))
    return y1


def diffeq(dydx, delta_t, y0):
    '''
    euler method for estimating the next value of a differential equation
    f is the gradient function for y: dy/dx

    returns a list of subsequent y values
    '''

    y1 = y0+delta_t*dydx
    return y1


"""def first_order_delay(tau, kappa, change_in_input, output_initial):
    '''proper first-order delay
    returns a lambda function that takes a value of t'''
    e=2.718281828459045
    return lambda t: e^(-t/tau)*output_initial+ (1-e^(-t/tau))*kappa*change_in_input
"""


def delay(K, A, B_pre, delta_t):
    '''
    for a given change in time, B steps closer to A. It moves more the further away it is and the greater K is

    B = K * (A - B_init) * delta_t

    '''
    B_post = K * (A - B_pre) * delta_t
    return B_post


def stablediffeq(f, delta_t, y0, max_delta_t, n=1):
    '''
    currently just a diffeq until I figure out how they're meant to be different
    '''
    return diffeq(f, delta_t, y0, n=1)


def stabledelay(dydx, delta_t, A_init, K, B_init):
    '''
    combination of stable diffeq and delay

    uses the output of the diffeq function as A in the delay function

    The output's initial value B_init shifts according to how far it is from A.
    A is itself the output of the integration of a differential equation.

    inputname is the 

    < name> Equation name
    < outputname> The real name of B
    < initialval> Output's initial value if it has not been previously defined
    < inputname> Input name - the real name of A
    < rateconstname> K - delay rate constant
    < dervname> the name of variable that holds dydx
    < errorlim> Integration error limit
    < dxmaxname> Max step size
    '''
    A = diffeq(dydx, delta_t, A_init)
    B = delay(K, A, B_init, delta_t)
    return B


def impliciteq(yend, f, ystart_init, error_limit):
    '''
    For a given YEnd, finds YStart so that:
        | YEnd - f(YStart) | <= Error Limit
    '''
    def f_equal_0(y):
        return yend-f(y)
    root = fsolve(f_equal_0, ystart_init, xtol=error_limit)
    return root

def cubic_hermite_spline(x, xarray, yarray, slopes):
    '''
    the curves in HUMMOD appear to be Cubic Hermite Splines (curves defined by a set of x,y coords and a slope at each point)

    uses scipy.interpolate.CubicHermiteSpline

    input:
        xarray and yarray and slopes are lists of the same length, they are the x and y coordinates and associated slopes
    '''
    curve = CubicHermiteSpline(xarray, yarray, slopes)
    return curve(x)

timervars = {}

def set_timervar(name, val, state):
    if val == "unchanged":
        if name in timervars:
            val = timervars[name][0]
        else:
            val = None
    if state == "unchanged":
        if name in timervars:
            state = timervars[name][1]
        else:
            state = None
    timervars[name] = [val, state]
