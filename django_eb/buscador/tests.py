from django.test import TestCase

# Create your tests here.
def squares(number):
	print("please enter your number here: ")
	squares = number ** 2
	print("this is your number squared: " + squares)