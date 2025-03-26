"""
S — Single Responsibility Principle (SRP)— Принцип единственной ответственности.

Один класс решает одну задачу - каждый класс должен выполнять только одну четко определенную функцию. 
Если он решает более одной задачи, это может привести к сложностям в поддержке и расширении кода.
"""



# БЕЗ SRP:
"""
Класс Human_body отвечает за две задачи — ответ на вопрос о возрасте и подсчет индекса массы тела.
"""
class Human_body:    
    def __init__(self, height, weight, age):        
        self.height = height       
        self.weight = weight     
        self.age = age         

    def my_age(self):        
        print(f"Мне {self.age} :)")

    def calculate_body_mass_index(self):         
        body_mass_index = (self.weight/(self.height**2))
        print(f"Мой индекс массы тела: {body_mass_index:.2f}")

        
# С SRP:
"""
Класс Human_body отвечает за простую информацию о теле, а класс Body_mass_index — за подсчёт массы тела для нужного нам человека.
"""
class Human_body:    
    def __init__(self, height, weight, age):        
        self.height = height       
        self.weight = weight     
        self.age = age         \
        
    def my_age(self):        
        print(f"Мне {self.age} :)")

class Body_mass_index:    
    def calculate_body_mass_index(self, human_body):         
        body_mass_index = (human_body.weight/(human_body.height**2))
        print(f"Мой индекс массы тела: {body_mass_index:.2f}")
