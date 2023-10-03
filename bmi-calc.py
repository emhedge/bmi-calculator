name = input("Enter your name: ")

weight = int(input("Enter your weight in kilograms: "))

height = int(input("Enter your height in centimeters: "))

# formula from https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html
BMI = ((weight / (height * height)) * 10000)

print("Your BMI is: " + str(BMI))


# info from https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations
if BMI>0:
    if BMI < 18.5:
        print('You are in the underweight group. Please consider supplementing your diet with a greater amount of healthy food options.') #https://www.healthdirect.gov.au/what-to-do-if-you-are-underweight
    elif BMI <= 24.9:
        print(name + ', you are in the normal weight group. Nice job and keep up the good work.') 
    elif BMI <= 29.9:
        print('You are in the pre-obesity group. Please consider limiting your food intake so that you do not increase your health risks.') 
    elif BMI <= 34.9:
        print('You are in the obesity class I group. It is time to consider approaches to lower your weight.')
    elif BMI <= 39.9:
        print('You are in the obesity class II group. Please reduce your food portions and increase regular physical activity.') 
    elif BMI > 40:
        print('You are in the obesity class III group. To avoid serious health risks, please reduce caloric intake considerably and increase regular physical activity.') 
else:
    print('Please input valid data, silly.')