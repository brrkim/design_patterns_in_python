from abc import ABC
import cmath
import math

class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b**2-4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        dis = b**2-4*a*c
        if dis < 0:
            return float('nan')
        return dis


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        dis = complex(self.strategy.calculate_discriminant(a,b,c),0)
        
        if dis in [0, float('nan')]:
            return float('nan'), float('nan')
        
        return (-b+cmath.sqrt(dis))/(2*a), (-b-cmath.sqrt(dis))/(2*a)