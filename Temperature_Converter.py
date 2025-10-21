def celcius_to_fahrenheit(celcius):
    temp = (celcius * 9/5)+32
    return temp

def fahrenheit_to_celcius(fahrenheit):
    temp = (fahrenheit-32) *5/9
    return temp


def kelvin_to_celcius(kelvin):
    temp = kelvin-273.15
    return temp

def celcius_to_kelvin(celcius):
    temp = celcius+273.15
    return temp

def kelvin_to_farenheit(kelvin):
    temp = (kelvin-273.15)*9/5+32
    return temp

def farenheit_to_kelvin(farenheit):
    temp = (farenheit-32)*5/9 + 273.15
    return temp


while True:
 print("Choose your conversion: ")
 print("\n1. farenheit to celcius")
 print("\n2. farenheit to kelvin")
 print("\n3. Kelvin to celcius")
 print("\n4. Kelvin to farenheit")
 print("\n5. celcius to farenheit")
 print(" \n6. celcius to kelvin")
 print("\n7. Exit")


 option = int(input("Choose what to do: "))
 if option == 7:
    print("Exited!")
    break
 try:
  temp = float(input("Enter your temperature: "))
 except ValueError:
    print("Enter a valid value: ")
    continue 
 

 if option == 1:
    result = fahrenheit_to_celcius(temp)
    print(f"{temp} Farenheit = {result} Celcius")
 elif option == 2:
    result = farenheit_to_kelvin(temp)
    print(f"{temp} Farenheit = {result} Kelvin") 
 elif option == 3:
    result = kelvin_to_celcius(temp)
    print(f"{temp} Kelvin = {result} Celcius")  
 elif option == 4:
    result = kelvin_to_farenheit(temp)
    print(f"{temp} kelvin = {result} Farenheit")    
 elif option == 5:
    result = celcius_to_fahrenheit(temp)
    print(f"{temp} Celcius = {result} Farenheit")  
 elif option == 6:
    result = celcius_to_kelvin(temp)
    print(f"{temp} Celcius = {result} Kelvin") 
 else:
    print("Invalid option")            