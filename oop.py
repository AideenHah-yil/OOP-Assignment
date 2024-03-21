class Person:
    def _init_(self):
        self.name = ''
        self.age = 0
        self.gender = ''

introduce =  f"{self.__class__.__name__} {self.__class__.__age__} {self.__class__.gender}"  

introduce(Person)