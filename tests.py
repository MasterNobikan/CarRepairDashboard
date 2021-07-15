#!/usr/bin/env python3
#tests.py for Car.py

from unittest import TestCase
from unittest.mock import patch

from Car import *

class CarResponse:
	Car("Grey","Toyota",300000)
	text = "The Grey Toyota has driven 300,000 miles"
	
class TestCar(TestCase):
	
#	@patch(TODO)
	def test_CarReturn(self, mock_get):
		mock_get.return_value = CarResponse()
		
		test = Car('Grey', 'Toyota', 300000)
#		print(CarResponse())
		mock_get.assert_(test)

if __name__ == '__main__':
	from unittest import main
	main()
		
