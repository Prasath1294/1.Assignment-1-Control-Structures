class multipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:\nMachine Learning\nNeural Network\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
        
    def OddEven():
        num=int(input("Enter a number: "))
        if ((num%2)==0):
            print(num,"is Even Number")
            message="Even Number"
        else:
            print(num,"is Odd Number")
            message="Odd Number"
        return message
    
    def Elegible(Gender=input("Your Gender:"),Age=int(input("Your Age:"))):
        if (Gender=="Male" or Gender=="Female" and Age>21):
            print("Elegible")
            result="Elegible"
        else:
            print("Not Eligible")
            result="Not Elegible"
        return result
    
    def percentage():
        s1=(int(input("Subject1= ")))
        s2=(int(input("Subject2= ")))
        s3=(int(input("Subject3= ")))
        s4=(int(input("Subject4= ")))
        s5=(int(input("Subject5= ")))
        total=s1+s2+s3+s4+s5
        print("Total : ", total)
        percent=total/5
        print("Percentage : ", percent)
        
    def triangle(Height,Breadth):
        Area_of_triangle=(Height*Breadth)/2
        print("Area of Triangle:", Area_of_triangle)
        return Area_of_triangle
    
    def triangle1(Height1,Height2,Breadth):
        perimeter=(Height1+Height2+Breadth)
        print("Perimeter of Triangle:", perimeter)
        return perimeter

        
        
        
        
        
        
        
        
        