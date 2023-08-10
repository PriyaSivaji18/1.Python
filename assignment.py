class SubfieldsinAI():
    
    def Subfields():
        lists=["Subfields in AI are :","Machine Learning","Nural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in lists:
            print(temp)    
    
    
    def OddEven():
        num=int(input("Enter The Number : "))
        if((num%2)==0):
            message="Even Number"
        else:
            message="Odd Number"
        if(message=="Even Number"):
            print("The Given Number Is Even Number")
        else:
            print("The Given Number Is Odd Number")
            return message
    
    
    def Eligible():
        criteria=input("Your Gender : ")
        age=int(input("Your Age : "))
        if(age>=18):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")

    
    def percentage():
        S1 = int(input("Subject1= "))
        S2 = int(input("Subject2= "))
        S3 = int(input("Subject3= "))
        S4 = int(input("Subject4= "))
        S5 = int(input("Subject5= "))
        Total = S1 + S2 + S3 + S4 + S5
        print("Total : ",Total)
        Percentage = (Total/500)*100
        print("Percentage :",Percentage)
        return
    
   
    def triangle():
        h1 = int(input("Height:"))
        b1 = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        A1 = (h1 * b1)/2
        print("Area of Triangle:", A1)
        H1 = int(input("Height1:"))
        H2 = int(input("Height2:"))
        B1 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        A2 = H1 + H2 + B1
        print("Perimeter of Triangle:", A2)
        return
    
