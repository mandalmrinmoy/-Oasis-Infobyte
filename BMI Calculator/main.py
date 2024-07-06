def main():
    while True:
        
        print('\n')
        print('*'*42)
        print('BMI Categories:')
        print('Underweight = <18.5 kg/m2')
        print('Normal weight = 18.5 kg/m2–24.9 kg/m2')
        print('Overweight = 25 kg/m2–29.9 kg/m2')
        print('Obesity = BMI of 30 kg/m2 or greater')
        print('*'*42,'\n')
# **********************************************************************
        wight=float(input('Enter Your Weight in Kilograms : '))
        height=float(input('Enter Your Weight in Meters : '))
        bmi_calculator=wight/(height*height)
        print(f"Your BMI: {'%.2f'%bmi_calculator} kg/m2")
# **********************************************************************
        if(bmi_calculator<18.5):
            print('BMI Categories: Underweight')
        elif(bmi_calculator>=18.5 and bmi_calculator<25):
            print('BMI Categories: Normal weight')
        elif(bmi_calculator>=25 and bmi_calculator<30):
            print('BMI Categories: Overweight')
        elif(bmi_calculator>=30):
            print('BMI Categories: Obesity')
# **********************************************************************    
        print('*'*42)


if __name__=="__main__":
    main()