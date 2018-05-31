
class BikeRental:
    # Initialize Basic person Info
    def __init__(self):
        self.name = None
        self.lastName = None
        self.isFamily = False


    # Create new Data to User
    def newData(self,name,lastName,isFamily,rentType,numberBikes = 1):
        self.name = name
        self.lastName = lastName
        self.isFamily = isFamily
        self.numberBikes = numberBikes
        self.rentType = rentType

    # Get data
    def printData(self):
        return [self.name, self.lastName, self.isFamily, self.numberBikes, self.rentType]

    # rentalClass: Definews the object by the type of time to pay
    # a. By Hour b. By Day c. By Week
    class RentalByHour:

        def __init__(self,data):
            self.data = data
            self.price = 5
            self.discount = 0.7

        def __call__(self):
            pass

    # Check Family rental to use discount
        def setDiscount(self):

            self.price = self.price*self.discount if self.data.isFamily else self.price
            return self.price

    # Check number of bikes
        def getNumberBikes(self):
            self.numberBikes = 1 if not self.data.isFamily else self.numberBikes
            return self.numberBikes

        def getPrice(self,time):
            return self.price*time


    class RentalByDay(RentalByHour):
        def __init__(self,data):
            self.data = data
            self.price = 20
            self.discount = 0.7


    class RentalByWeek(RentalByHour):
        def __init__(self,data):
            self.data = data
            self.price = 60
            self.discount = 0.7

    #Creates an instance of the Rental object
    class RentalServer():
        def __init__(self,rentalClass,data):
            self.rentalClass = rentalClass(data)


if __name__ == "__main__":

    bikeRentalA = BikeRental()
    bikeRentalA.newData('Alan','Rojas',True,BikeRental.RentalByWeek,3)
    rentalA = BikeRental.RentalServer(BikeRental.RentalByDay,bikeRentalA)
    print rentalA.rentalClass.getPrice(3)
    print rentalA.rentalClass.setDicount()
    print rentalA.rentalClass.getPrice(3)

