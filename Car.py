#!/usr/bin/env python3
__version__ = '0.1'


class Car:
	
	def __init__(self, color, model, odom):
		self.color = color
		self.model = model
		self.odom = odom

	def __str__(self):
		return f'The {self.color} {self.model} has driven {self.odom:,} miles'
	
	def noise(self):
		return f'vroom vroom?'
	
if __name__ == '__main__':
	bmw = Car("Red","540i", 203000)
	honda = Car("Black","Pilot", 189099)
	print(bmw)
	print(honda)
	