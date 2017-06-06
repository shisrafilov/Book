import random

print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\tЯ загадал натуральное число из диапазона от 1 до 100.")
print("\tУ вас есть 3 попытки.\n")

# начальные значения
the_number = random.randint(1, 100)
print(the_number)
guess = int(input("Ваше предположение: "))
tries = 1
# цикл отгадывания
while tries < 3:
    if guess == the_number:
        print("Baм удалось отгадать число! Зто в самом деле", the_number)
        break

    elif guess < the_number:
        print("Больше.")
        guess = int(input("Ваше предположение: "))

    elif guess > the_number:
        print("Меньше.")
        guess = int(input("Ваше предположение: "))

    tries += 1

if guess != the_number:
    print("Вам не удалось отгадать число за 3 попытки")

input("\n\nНажмите Enter чтобы выйти.")
