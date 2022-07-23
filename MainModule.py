from OOPClassModule import Car   # from the FILE NAME import Cass

# create object with an unique name 'car_1'
car_1= Car ('Chevy','Corvette',2021,'blue') # assigning values to the object car_1
                                            # in class car with attributes ('make','model',...etc)
                                            # note that you do not have to pass in self
# print specfic attributes of car_1
print (car_1.make)
print (car_1.model)
print (car_1.year)
print (car_1.color)

# can also call methods

car_1.drive ()          # its like car1_.drive (self) but dont need to pass in the self so ()
car_1.stop ()

# create another object of class car with the same attributes
# need to enter arguments to create an object
car_2 = Car ('Lol', 'lolzers',2022,'lel' )



car_2.drive()
car_2.stop ()