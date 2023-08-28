# class Creature:
#     def __init__(self):
#         self.str = 10
#         self.agil = 10
#         self.int = 10
        
#     @property
#     def sum_of_stats(self):
#         return self.str + self.agil + self.int
    
#     @property
#     def max_stat(self):
#         return max(
#             self.str, self.agil, self.int
#         )
    
#     @property
#     def avg_stat(self):
#         return self.sum_of_stats / 3.0
    
class Creature:
    _str = 0
    _agil = 1
    _int = 2
    
    def __init__(self):
        self.stat = [10,10,10]
    
    @property
    def str(self):
        return self.stat[Creature._str]

    @str.setter
    def str(self, val):
        self.stat[Creature._str] = val

    @property
    def agil(self):
        return self.stat[Creature._agil]

    @agil.setter
    def agil(self, val):
        self.stat[Creature._agil] = val

    @property
    def int(self):
        return self.stat[Creature._int]

    @int.setter
    def int(self, val):
        self.stat[Creature._int] = val

    @property
    def sum_of_stats(self):
        return sum(self.stat)
    
    @property
    def max_stat(self):
        return max(self.stat)
    
    @property
    def avg_stat(self):
        return float(self.sum_of_stats / len(self.stat))