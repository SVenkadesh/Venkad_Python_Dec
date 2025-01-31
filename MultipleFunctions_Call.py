#OOPS Class-3

class multiplefunctions():
    def Agecategory():
        for Age in lists:
            if(Age<18):
                print('Childern');
            elif(Age<35):
                print('Adult');
            elif(Age<59):
                print('Citizen');
            else:
                print('Senior Citizen');

    def OddEven():
        A = int(input('Enter any value:'));
        if((A%2)==0):
                print('It is EVEN number')
                Message=('It is EVEN number')
        else:
                print('It is ODD number')
                Message=('It is ODD number')
    def BMI_Value():
        BMI_Value= int(input('Enter the BMI Index:'))
        if(BMI_Value<18.5):
            print('Underweight');
            Message='Underweight'
        elif(BMI_Value<24.9):
            print('Normal Range');
            Message='Normal Range'
        elif(BMI_Value<29.9):
            print('Overweight');
            Message='Overweight'
        else:
            print('Very Overweight')
            Message='Very Overweight'
        return Message