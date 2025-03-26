"""
I — Interface Segregation Principle (ISP) — Принцип разделения интерфейса.

Cоздавать только небольшие и узконаправленные интерфейсы, не перегруженные ненужными методами.
"""



# Без ISP
class Human_brain:     
    def fantasize(self):         
        pass    
    def count(self):         
        pass     
    def visualize(self):         
        pass

class middle_aged_Brain(Human_brain):    
    def fantasize(self):         
        print("ПРОЦЕСС: ФАНТАЗИЯ")         
    def count(self):         
       print("ПРОЦЕСС: ПОДСЧЁТ")        
    def visualize(self):         
       print("ПРОЦЕСС: ВИЗУАЛИЗАЦИЯ")  

"""
Методы fantasize(), count() и visualize() находятся в одном интерфейсе — Human_brain. Класс middle_aged_Brain реализует этот интерфейс со всеми его методами.
"""


# С ISP
class Fantasizer:     
    def fantasize(self):         
        pass
class Counter:     
    def count(self):         
        pass
class Visualizer:     
    def visualize(self):         
        pass

class kids_Brain(Fantasizer, Visualizer):     
    def fantasize(self):         
        print("ПРОЦЕСС: ФАНТАЗИЯ")      
    def visualize(self):         
       print("ПРОЦЕСС: ВИЗУАЛИЗАЦИЯ")       

class middle_aged_Brain(Counter, Visualizer):            
    def count(self):         
       print("ПРОЦЕСС: ПОДСЧЁТ")        
    def visualize(self):         
       print("ПРОЦЕСС: ВИЗУАЛИЗАЦИЯ")  

"""
Для каждой задачи есть отдельный интерфейс: Fantasizer с методом fantasize(), Counter с методом count() и Visualizer с методом visualize(), при этом каждый интерфейс можно удобно и гибко использовать.
"""