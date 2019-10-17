fullName= input("Ingrese su nombre completo: ")

birthDay= int(input("Ingrese el dia de nacimiento: "))
birthMonth= int(input("Ingrese el mes de nacimiento: "))
birthYear= int(input("Ingrese el año de nacimiento: "))

currentDay= int(input("Ingrese el dia actual: "))
currentMonth= int(input("Ingrese el mes actual: "))
currentYear= int(input("Ingrese el año actual: "))

age = (currentYear - birthYear) - 1

if currentMonth >= birthMonth and currentDay >= birthDay:
    age = age + 1

# edad=(currentDate-daysAge)//365
print(f"Usted tiene {age}")