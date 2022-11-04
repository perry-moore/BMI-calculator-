Weight = float(input("Enter your weight:"))
# Weight is in pound(Ib)
Height = float(input("Enter your height:"))
# Height is in inches(in)
BMI = float((Weight/(Height * Height))* 703)
if BMI < 18.5:
    print("Underweight")
elif 18.5<=BMI<24.9:
    print("Normal weight")
elif 25<=BMI<29.9:
    print("Overweight")
else:
    print("Obesity")