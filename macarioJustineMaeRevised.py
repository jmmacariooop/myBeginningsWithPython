''' Programmed by: Macario, Justine Mae B.
    Program Title: labActOne
    Program Date: September 7 - September 11, 2023'''
equalSign = "================================="

#a. Pounds to Kilograms Converter
pounds = float(input("Enter your weight in pounds(lb): ")) 
anso= (pounds * 0.453592) 
print("Weight in Pounds (lbs): " + str(pounds)) 
print("Weight in Kilograms (kg): " + str(anso))
print(equalSign)

#b. Miles to Kilometers Converter
miles = float(input("Enter your length in miles(mi): "))
anst = (miles * 1.60934)
print("Length in Miles(mi): " + str(miles) )
print("Length in Kilometers(km): " + str(anst))
print(equalSign)

#c. Fahrenheit to Celsius Converter**
temp = float(input("Enter your temperature in Fahrenheit(F): "))
ansth = (temp-32)*5/9
print("Temperature in Fahrenheit(F): " + str(temp))
print(f"Temperature in Celsius(°C): " + str(ansth))
print(equalSign)

#new addition 
ageStu1 = int(input("Enter age of Student 1: "))
ageStu2 = int(input("Enter age of Student 2: "))
ageStu3 = int(input("Enter age of Student 3: "))
ageStu4 = int(input("Enter age of Student 4: "))
ageStu5 = int(input("Enter age of Student 5: "))
ageStu6 = int(input("Enter age of Student 6: "))
ageStu7 = int(input("Enter age of Student 7: "))
ageStu8 = int(input("Enter age of Student 8: "))
ageStu9 = int(input("Enter age of Student 9: "))
ageStu10 = int(input("Enter age of Student 10: "))

#d. Average Age of 10 Students
print("Age of Student 1: " + str(ageStu1))
print("Age of Student 2: " + str(ageStu2))
print("Age of Student 3: " + str(ageStu3))
print("Age of Student 4: " + str(ageStu4))
print("Age of Student 5: " + str(ageStu5))
print("Age of Student 6: " + str(ageStu6))
print("Age of Student 7: " + str(ageStu7))
print("Age of Student 8: " + str(ageStu8))
print("Age of Student 9: " + str(ageStu9))
print("Age of Student 10: " + str(ageStu10))

aveAge = (ageStu1 + ageStu1 + ageStu2 + ageStu3 + ageStu4 + ageStu5 + ageStu6 + ageStu7 + ageStu8 + ageStu9 + ageStu10)/10
print("The average age of the students is:" + str(aveAge))
print(equalSign)

#e. Dungeon Meshi!
charNameOne = "Laios" 
charNameTwo = "Marcille" 
charNameThree = "Chilchuck"
charNameFour =  "Izutsumi" 
charNameFive = "Senshi"

dndClassOne = "Knight"
dndClassTwo =  "Elf" 
dndClassThree = "Locksmith" 
dndClassFour = "Beastman" 
dndClassFive = "Dwarf"

# Title Page  

print("My sister is inside the red dragons stomach...")
print("This odd combination now enter the Lunatic Magician's Dungeon with one thing in mind! To rescue his sister Falin and ... to eat monsters?")
print("This party, including " + charNameOne +" the "+dndClassOne +", " + charNameTwo + " the " +  dndClassTwo + ", " + charNameThree + " the "+ dndClassThree +", "+ charNameFour + " the "+ dndClassFour +" and "+ charNameFive + " the "+ dndClassFive)
print(",prepares to venture the deep lore of the dungeons and its monster delicacies! ")

