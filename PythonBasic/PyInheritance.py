class Car:
    __wheels=4
    __color= ""
    __doors=4
    __car_name=""

    def __init__(self,color,carname):
        self.__color=color
        self.__car_name=carname


    def set_wheels(self,wheels):
        self.__wheels = wheels
    def get_wheels(self):
        return self.__wheels
    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
    def set_doors(self,doors):
        self.__doors=doors
    def get_doors(self):
        return self.__doors
    def set_carname(self,carname):
        self.__car_name=carname
    def get_carname(self):
        return self.__car_name
    def toString(self):
        return "the name is {} and color is {}".format(self.__car_name,self.__color)
    def gettype(self):
        return "Car"



hundai = Car('red','i20')

print(hundai.toString())

class AutomaticCar(Car):
    __gear=0

    def __init__(self,gear,carname,color):
        self.__gear=gear
        ##super().__init__('white','city')
        super().__init__(color, carname)

    def set_gear(self,noOfGear):
        self.__gear=noOfGear
    def get_gear(self):
        return self.__gear
    def toString(self):
        return "the sedan car {} with color {} has {} gears".format(self.get_carname(),self.get_color(),self.get_gear())
    def gettype(self):
        return "Automatic"


honda = AutomaticCar(6,'maruthi','red')
print(honda.toString())


class CarTest:
    def get_Type(self,type):
        return type.gettype()

testcar= CarTest()
print(testcar.get_Type(honda))
print(testcar.get_Type(hundai))