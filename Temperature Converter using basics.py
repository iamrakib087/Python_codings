print("Hello! This is a temperature converter \nYou can convert temperature from Celsius to Fahrenheit or Fahrenheit to Celcius")
t=float(input("Enter 1 for \"Convert Celsius to Fahrenheit\" \nEnter 2 for \"Fahrenheit to Celcius\" \nWhat kind of convertion you want? : "))
if t==1:
    print("\n.........Celcius To Fahrenheit Converter........\n")
    c=float(input("Enter temperature in Celcius: "))
    f=(c*9/5)+32
    f=round(f,2)
    print("In fahrenheit the temparature is:",f)
if t==2:
    print("\n.........Fahrenheit To Celcius Converter........\n")
    f=float(input("Enter temperature in Fahrenheit: "))
    c=(f-32)*5/9
    c=round(c,2)
    print("In Celcius the temparature is:",c)