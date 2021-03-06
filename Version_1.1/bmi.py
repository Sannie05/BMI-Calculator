restart = 'restart'

def printbmi():
    if BMI < 16:
        print('Strongly underweight')
    elif BMI < 17:
        print('Underweight')
    elif BMI < 18.5:
        print('Slightly underweight')
    elif BMI < 24.5:
        print('Normal weight')
    elif BMI < 27.5:
        print('Slightly overweight')
    elif BMI < 30:
        print('Overweight')
    elif BMI < 35:
        print('Overweight, obesity level 1')
    elif BMI < 40:
        print('Overweight, obesity level 2')
    else:
        print('Overweight, Obesity level 3')

while restart == 'restart':

# Input variables

    BMI_Q = str(input('If you want to calculate your BMI type "bmi" otherwise press enter: '))

    if BMI_Q == 'bmi':
        BMI_UOF = str(input('To use the Metric system type "metric" and to use the Imperial system type "imperial": '))
    else:
        quit()

    if BMI_UOF == 'metric':
        weight_m = float(input('How much do you weight in kilograms? '))
        height_m = float(input('How tall are you in meters? '))
        BMI = weight_m / (height_m ** 2)
    elif BMI_UOF == 'imperial':
        weight_i = float(input('How much do you weight in pounds? '))
        height_i = float(input('How tall are you in inches? '))
        BMI = 703 * weight_i / (height_i ** 2)

    printbmi()

