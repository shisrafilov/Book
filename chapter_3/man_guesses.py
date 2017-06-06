# coding=utf-8
 
print("\t\t\tЗдравствуй, игрок!")
print("Тебе предстоить сыграть с компьютером в 'Числа'.")
print("Надо загадать число от 1 до 100, а компьютер попытается отгадать его.")
number = int(input("Введите загаданное число: "))
 
# Задаем начальные значения и задаем первую попытку угадывания, задействуя метод Хартли.
# То есть делим интервал угадывания наполовину, чтобы быстрей добраться до искомого числа.
computer_number = 50
tries = 1
low = 1
high = 100
print(computer_number)
 
# Цикл отгадывания
while computer_number != number:
    if computer_number > number:
        high = computer_number    # Задаем загаданное число верхней границей интервала
        # Продолжаем делить полученный интервал наполовину.
        computer_number = computer_number - ((high-low)//2)
        print(computer_number)
    elif computer_number < number:
        low = computer_number    # Задаем загаданное число нижней границей интервала
        computer_number = computer_number + ((high-low)//2)
        print(computer_number)
    tries += 1
 
print("Компьютер потратил", tries, "попытки(ок) на отгадывание твоего числа.")
input("\n\nНажмите Enter, чтобы выйти из программы...")