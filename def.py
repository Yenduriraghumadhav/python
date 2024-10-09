try: 
  num1=(input("enter the number : "))
  num2=(input("enter big  number than num1 : "))

  def addition(num1,num2):
      Total = num1 +num2
  print(f"addition of given numbers : {Total}")
  def subtration(num1,num2):
    if num1>num2:
      print("subtration in if : ",num1-num2)
    # elif num1<num2:
    elif num1==num2:
       print("both numbers are same try different numbers : ")
    else:
        print("subtration in else :",num2-num1)    
  def multiplication(num1,num2):
    print("multiplicaton : ",num1*num2)
  def divion(num1,num2):
    print("divion : ",num1/num2)

    addition(num1,num2)
    subtration(num1,num2)
    multiplication(num1,num2)
    divion(num1,num2)            
except ValueError:
  print(enter the valid number)

    