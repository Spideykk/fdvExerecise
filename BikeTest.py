from CompanyClass import BikeRental

import unittest


class BikeRentalTest(unittest.TestCase):

    def setUp(self):
        self.bikeRentalTester = BikeRental()
        self.bikeRentalTester.newData('Alan','Rojas',True,BikeRental.RentalByWeek,3)
        self.rentalA = BikeRental.RentalServer(BikeRental.RentalByDay,self.bikeRentalTester)
        self.rentalB = BikeRental.RentalServer(BikeRental.RentalByHour,self.bikeRentalTester)
        self.rentalC = BikeRental.RentalServer(BikeRental.RentalByWeek,self.bikeRentalTester)

    # Check Server Class
    def testClassServer(self):
        self.assertEqual('RentalServer',self.rentalA.__class__.__name__)

    # Check Price
    def testRentalPrice(self):
        self.assertEqual(60,self.rentalA.rentalClass.getPrice(3))

    # Check Rental instances
    def testRentalByHour(self):
        self.assertEqual(5,self.rentalB.rentalClass.price)

    def testRentalByDay(self):
        self.assertEqual(20,self.rentalA.rentalClass.price)

    def testRentalByWeek(self):
        self.assertEqual(60,self.rentalC.rentalClass.price)

    # Check rentalClass methods
    def testDiscount(self):
        self.rentalA.rentalClass.getPrice(3)
        self.rentalA.rentalClass.setDiscount()
        self.assertEqual(42,self.rentalA.rentalClass.getPrice(3))

    # Check data list
    def testBasicData(self):
        self.assertTrue(isinstance(self.bikeRentalTester.printData(),list))

if __name__ == '__main__':
    unittest.main()