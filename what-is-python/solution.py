"""
Problem: What is Python?
URL: https://neetcode.io/problems/python-what-is-python/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from decimal import Decimal, getcontextfrom decimal import Decimal, getcontext

def calculate_pi(n):def calculate_pi(n):
    getcontext().prec = n + 2  # Set precision higher than needed for accuracy    getcontext().prec = n + 2  # Set precision higher than needed for accuracy
        
    C = 426880 * Decimal(10005).sqrt()    C = 426880 * Decimal(10005).sqrt()
    K = 6    K = 6
    M = 1    M = 1
    X = 1    X = 1
    L = 13591409    L = 13591409
    S = L    S = L
        
    for i in range(1, n):    for i in range(1, n):
        M = (K ** 3 - 16 * K) * M // i ** 3        M = (K ** 3 - 16 * K) * M // i ** 3
        L += 545140134        L += 545140134
        X *= -262537412640768000        X *= -262537412640768000
        S += Decimal(M * L) / X        S += Decimal(M * L) / X
        K += 12        K += 12