class SubfieldsinAI():  
    def Subfields():
        lists=["Subfields in AI are :","Machine Learning","Nural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for temp in lists:
            print(temp)
    Subfields()        
    
    
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
    message=OddEven()
    
    
    def Eligible():
        criteria=input("Your Gender : ")
        age=int(input("Your Age : "))
        if(age>=18):
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
    Eligible()

    
    sub1=int(input("Subject 1 : "))
    sub2=int(input("Subject 2 : "))
    sub3=int(input("Subject 3 : "))
    sub4=int(input("Subject 4 : "))
    sub5=int(input("Subject 5 : "))
    def addition(sub1,sub2,sub3,sub4,sub5):
            total=sub1+sub2+sub3+sub4+sub5
            print("Total:",total)
    addition(23,45,34,23,23)
    def percentage(total):
            total=(total/500)*100
            print("Percentage:",total)
    percentage(148)
    
   
    height=int(input("Height:"))
    breadth=int(input("Breadth:"))
    def areaoftriangle(height,breadth):
        area=(height*breadth)/2
        print("Area Of Triangle:",area)
    areaoftriangle(3,4)
    height1=int(input("Height1:"))
    height2=int(input("Height2:"))
    breadth=int(input("Breadth:"))
    def perimeteroftriangle(height1,height2,breadth):
        perimeter=height1+height2+breadth
        print("Perimeter Of Triangle:",perimeter)
    perimeteroftriangle(3,4,45)
    
