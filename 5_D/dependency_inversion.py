"""
D — Dependency Inversion Principle (DIP) — Принцип инверсии зависимостей.

Модули верхнего уровня не должны зависеть от модулей нижнего уровня. 
Оба типа модулей должны зависеть от абстракций. 
Абстракции не должны зависеть от деталей, но детали должны зависеть от абстракций.
"""


# БЕЗ DIP
class Human_visual_memory:     
    def save(self, knowledgeImg):         
        print(f"Вы увидели что-то новое! ({knowledgeImg})")

    def findByImage(self, Image):         
        print(f"Поиск в визуальной памяти по изображению - {Image}")
    
class Human_memory:     
    def __init__(self):           
        self.memory = Human_visual_memory()

    def newKnowledge(self, knowledge):             
        self.memory.save(knowledge)

    def find_Knowledge(self, Knowledge):         
        self.memory.findByImage(Knowledge)

"""
Зависимость Human_memory от Human_visual_memory определена внутри класса. 
И если мы захотим использовать какой-то другой вид памяти человека, нужно будет лезть внутрь класса
"""


# С DIP
class Human_visual_memory:     
    def save(self, knowledgeImg):         
        print(f"Вы увидели что-то новое! ({knowledgeImg})")

    def findByImage(self, Image):         
        print(f"Поиск в визуальной памяти по изображению - {Image}")

class Human_memory:     
    def __init__(self, memory):              
        self.memory = memory

    def newKnowledge(self, knowledge):             
        self.memory.save(knowledge)

    def find_Knowledge(self, Knowledge):         
        self.memory.findByImage(Knowledge)

"""
Зависимость Human_visual_memory передается в Human_memory через конструктор.  
Интерфейс Human_visual_memory позволяет избежать конкретного вида памяти (например, визуального) в классе Human_memory. 
И если мы захотим поработать с другим видом памяти, нам не нужно будет переписывать код Human_memory,
Вместо этого реализацию нового вида памяти можно сделать в новом классе Human_emotional_memory, обьект которого, мы также сможем передать в наш общий класс памяти
"""