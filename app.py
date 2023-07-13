# age = 20
# price = 19.95
# first_name = "Mosh"
# is_online = True
# print(age)
#
# name = input("What is your name? ")
# print("Hello " + name)
#
# birth_year = input("Enter your birth year: ")
# age = 2023 - int(birth_year)
# print(age)
# int()
# float()
# bool()
# str()
#
# input_1 = float(input("First: "))
# input_2 = float(input("Second: "))
# sum = input_1 + input_2
# print("Sum: " + str(sum))

# course = "Python for Beginners"
# print(course.upper())
# print(course.find("y"))
# print(course.find("Y"))
# print(course.replace("for", "4"))
# print("Python" in course)
# print(course)

# print(10 / 3)  # Returns float
# print(10 // 3)  # Returns integer
# print(10 ** 3)  # Exponent

price = 5
print(price > 10 or price < 30)
print(price > 10 and price < 30)
print (price > 10)
print(not price > 10)

temperature = 15
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

weight = float(input("Weight: "))
unit = input("K(g) or L(bs): ")
if unit.lower() == "k":
    print("Weight in lbs:" + str(weight * 2.2))
elif unit.lower() == "l":
    print("Weight in kg: " + str(weight / 2.2))
else:
    print("Wrong unit entered")