"""
O — Open/Closed Principle (OCP) — Принцип открытости/закрытости.

Программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
"""



# Без OCP
"""
Логика по разным задачам нашего рта находится в одном классе Mouth.
"""
class Mouth:     
    def work_mouth(self, task):         
        if task == "speak":             
            print("~Говорит~")
        elif task == "eat":             
            print("~Ест~")
        elif task == "сlosed":             
            print("~Закрыт~")


# С OCP
"""
Work_mouth является интерфейсом (Который по дефолту - закрывает рот). 
Этот интерфейс реализуют классы для каждой из задач рта: Speak_Work_mouth, Eat_Work_mouth и Closed_Work_mouth.
"""
class Work_mouth:     
    def work_mouth(self):         
        print("~Закрыт~")

class Speak_Work_mouth(Work_mouth):     
    def work_mouth(self):         
        print("~Говорит~")

class Eat_Work_mouth(Work_mouth):     
    def work_mouth(self):         
        print("~Ест~")

class Closed_Work_mouth(Work_mouth):     
    def work_mouth(self):         
        print("~Закрыт~")
