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

# price = 5
# print(price > 10 or price < 30)
# print(price > 10 and price < 30)
# print (price > 10)
# print(not price > 10)

# temperature = 15
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")

# weight = float(input("Weight: "))
# unit = input("K(g) or L(bs): ")
# if unit.lower() == "k":
#     print("Weight in lbs:" + str(weight * 2.2))
# elif unit.lower() == "l":
#     print("Weight in kg: " + str(weight / 2.2))
# else:
#     print("Wrong unit entered")

# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1

# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = "Jon"
# print(names[0:3])

# nums = [1,2,3,4,5]
# nums.append(6)
# print(1 in nums)
# print(nums)
# print(len(nums))
# nums.insert(0, -1)
# nums.remove(3)
# nums.clear()
# print(nums)

# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# numbers = range(5, 10, 2)
# for num in numbers:
#     print(num)

# PART 2

# first = "Ariel"
# last = "Baez"
# msg = f'{first} [{last}] is a coder'
# print(msg)
#
# numbers = [5,2,5,2,2]
# for i in range(len(numbers)):
#     string = ""
#     for j in range(numbers[i]):
#         string += "x"
#     print(string)

# nums_map = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output = ""
# for code in input("Phone Number? "):
#     output += f"{nums_map[code]} "
# print(output)

# emoji_map = {
#     ":)": "😀",
#     ":(": "😞"
# }
#
# message = input(">")
# words = message.split(" ")
# message = ""
# for word in words:
#     message += emoji_map.get(word,word) + " "
# print(message)

def greet_user(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")
print("Finish")