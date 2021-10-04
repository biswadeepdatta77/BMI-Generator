height = float(input("Enter your height in metres "))
weight = float(input("Enter your weight in kg "))
BMI = weight/(height*height)
BMI = round(BMI, 2)
if BMI<18.5:
    print("Under weight")
elif BMI>18.5 and BMI<=25:
    print("You have a normal weight")
elif BMI>25 and BMI<=30:
    print("You are overweight")
elif BMI>30 and BMI<=35:
    print("Obese")
else:
    print("Clinically obese")

