# Input Variables
weight_unit = str(input('Pounds or Kilosgrams? (write "pounds" or "kilograms") '))
length_unit = str(input('Centimeters or inches? (write "cm" or "in") '))
weight = float(input('How much do you weight? '))
length = float(input('How tall are you? '))

# Variables
bmi_1 = (weight / (length ** 2))
bmi_2 = bmi_1 * 10000
bmi_a = (weight / (length ** 2))
bmi_b = bmi_a * 703

# A function that prints out what your bmi says about you(kilograms)
def bmi_kilograms():
   if bmi_2 < 16:
      print('You are severely underweight')
   elif bmi_2 < 16.99 > 16:
      print('You are underweight')
   elif bmi_2 < 18.49 > 16.99:
      print('You are a little bit underweight')
   elif bmi_2 < 24.99 > 18.49:
      print('Your weight is normal')
   elif bmi_2 < 27.49 > 24.99:
      print('You are a little overweight')
   elif bmi_2 < 29.99 > 27.49:
      print('You are overweight')
   elif bmi_2 < 34.99 > 29.99:
      print('Overweight, obesity class 1')
   elif bmi_2 < 39.99 > 34.99:
      print('Overweight, obesity class 2')
   elif bmi_2 > 39.99:
      print('Overweight, obisity class 3')

# A function that prints out what your bmi says about you(pounds)
def bmi_pounds():
   if bmi_b < 16:
      print('You are severely underweight')
   elif bmi_b < 16.99 > 16:
      print('You are underweight')
   elif bmi_b < 18.49 > 16.99:
      print('You are a little bit underweight')
   elif bmi_b < 24.99 > 18.49:
      print('Your weight is normal')
   elif bmi_b < 27.49 > 24.99:
      print('You are a little overweight')
   elif bmi_b < 29.99 > 27.49:
      print('You are overweight')
   elif bmi_b < 34.99 > 29.99:
      print('Overweight, obesity class 1')
   elif bmi_b < 39.99 > 34.99:
      print('Overweight, obesity class 2')
   elif bmi_b > 39.99:
      print('Overweight, obisity class 3')

# Function calling
if weight_unit == 'kilograms' and length_unit == 'cm':
   bmi_kilograms()
elif weight_unit == 'pounds' and length_unit == 'in':
   bmi_pounds()
else:
   print('You need to enter kilograms with cm and reverse, note that your spelling also need to be correct.')

# Final input for closing the program in the python terminal   
input('Press enter to close the program: ')