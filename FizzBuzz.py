# Program: FizzBuzz
# Created by Oscar Cairoli
# Prints the numbers from 1 to 100.
# For multiples of three, print "Fizz"
# For multiples of five, print "Buzz"
# For numbers which are multiples of both three and five, print "FizzBuzz"

def fizzBuzz():
	for num in range(1, 100 + 1):
		if ((num % 3 == 0) and (num % 5 == 0)):
			print("Num: {}   FizzBuzz".format(num))
		elif (num % 5 == 0 and num % 3 != 0):
			print("Num: {}   Buzz".format(num))
		elif (num % 3 == 0 and num % 5 != 0):
			print("Num: {}   Fizz".format(num)) 
		else:
			print("Num: {}  ".format(num))
		
def main():
	fizzBuzz()

if __name__ == '__main__':
	main()