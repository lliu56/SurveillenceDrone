#create a representation of real life objects
# Attributes: what an object is
# Methods: what an object can do
# class: blue print of disctinct attricbutes and methods that an object will have
    # can be in main module or separete class file

class Car:   # create class object: car



    #need a special __init__ method to construct object for us
    def __init__(self,make,model, year, color):   # setting up parameters in the bracket
                                                  # when arguments are received you can assign
                                                  # value to each of the attributes
        # Attributes.. put under __init__ to assign them to the object
                                                  # to receive the argument need to add self.
                                                  # the assignment need to be equal to the arguments input above
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    #methods within a class--> indented
    def drive (self): # self refers the object used in this method
        print ('This' + self.model +'is driving')      # can replace 'car' with the model of the car ur driving
                                                       # self is replacing the object e.g.
                                                       # if car_1 is using the drive method then it iwill
                                                       # show the model of car 1 etc.

    def stop (self):
        print ('This'+ self.model + ' is stopped')