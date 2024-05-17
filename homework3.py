my_string = input("Введите строку: ")
print("Длина строки ", len(my_string))
print("В верхнем регистре  ", my_string.upper())
print("В нижнем регистре   ", my_string.lower())
print("Без пробелов        ", my_string.replace(" ", ""))
print("Первый символ строки", my_string[0:1])
print("Последний символ    ", my_string[len(my_string)-1:])

