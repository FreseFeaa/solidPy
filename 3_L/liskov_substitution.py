"""
L — Liskov Substitution Principle (LSP) — Принцип подстановки Барбары Лисков.

Объекты родительских классов должны быть заменяемы объектами дочерних классов без изменения ожидаемого поведения программы.
"""




# Без LSP:
class Eye_condition:     
    def state(self):         
        print("Со зрением всё отлично!")

class Right_Eye_condition(Eye_condition):     
    def __init__(self, diopter):         
        self.diopter = diopter              
    def state(self):         
        print(f"Правый глаз - {self.diopter} диоптрии")
    
class Left_Eye_condition(Eye_condition):     
    def __init__(self, diopter):         
        self.diopter = diopter              
    def state(self):         
        print(f"Левый глаз - {self.diopter} диоптрии")

"""
Нарушение принципа LSP происходит в классе Eye_condition. В нем реализован метод state(), который просто говорит, что со зрением всё в порядке.  
Такая реализация нарушает ожидаемое поведение, поэтому объекты Right_Eye_condition и Left_Eye_condition не могут быть замененой 
объекту базового класса Eye_condition без нарушения функциональности.
"""


# С LSP:
from abc import ABC, abstractmethod  
class Eye_condition(ABC):    
    @abstractmethod   
    def state(self):         
        pass

class Right_Eye_condition(Eye_condition):     
    def __init__(self, diopter):         
        self.diopter = diopter              
    def state(self):         
        print(f"Правый глаз - {self.diopter} диоптрии")
    
class Left_Eye_condition(Eye_condition):     
    def __init__(self, diopter):         
        self.diopter = diopter              
    def state(self):         
        print(f"Левый глаз - {self.diopter} диоптрии")

"""
Метод state() определен как абстрактный в базовом классе Eye_condition, гарантируя, что все производные классы должны его реализовать. 
Тогда объекты производных от Eye_condition классов можно использовать вместо него в любом месте кода.
"""
