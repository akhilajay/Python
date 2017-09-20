print("Python OOPs Concepts")

class Animal:

    # 2 __ is to represent private variabels
    __name=""
    __height=0
    __weight=0
    __sound=0

    #constructor
    def __init__(self ,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self. __weight = weight
        self.__sound = sound

    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def set_height(self,height):
        self.__height=height

    def get_height(self):
        return self.__height


    def set_weight(self,weight):
        self.__weight=weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kolograms and say {}".format(self.__name,self.__height,self.__weight,self.__sound)

dog =Animal('Jimmy','45','50','bow bow')

print(dog.toString())

#inheritance
class Cat(Animal):
    __owner = ""
    def __init__(self,name,height,weight,sound,owner):
        self.__owner=owner
        super(Cat,self).__init__(name,height,weight,sound)

    def set__owner(self,owner):
        self.__owner=owner
    def get_owner(self):
        return self.__owner
    def toString(self):
        ##return "{} is {} cm tall and {} kilograms and say {} his owner is {}".format(self.__name, self.__height,self.__weight,self.__sound,self.__owner)
        return self.__name

spot = Cat('lilly',35,45,'meow','nick')
print(spot.get_height())
print(spot.get_name())
print(spot.toString())