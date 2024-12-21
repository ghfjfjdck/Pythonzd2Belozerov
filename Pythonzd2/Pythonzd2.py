# -*- coding: utf-8 -*-
import random;

   # """Игра "Угадай число"."""
# secret_number = random.randint(1, 100)  # Загадываем число от 1 до 100
# attempts = 0
# print("Я загадал число от 1 до 100. Попробуй угадать!")

# while True:
#         try:
#             guess = int(input("Ваш вариант: "))
#             attempts += 1
#             if guess == secret_number:
#                 print(f"Поздравляю, вы угадали число {secret_number} за {attempts} попыток!")
#                 break
#             elif guess < secret_number:
#                 print("Загаданное число больше.")
#             else:
#                 print("Загаданное число меньше.")
#         except ValueError:
#             print("Пожалуйста, введите целое число.")



   # """Группировка одинаковых символов в список."""
# input_string = input("Введите строку символов, разделенных пробелами: ")
# symbols = input_string.split()
# grouped_symbols = []
    
# while symbols:
#       current_symbol = symbols[0]
#       group = []
#       i = 0
#       while i < len(symbols):
#         if symbols[i] == current_symbol:
#           group.append(symbols[i])
#           symbols.pop(i)
#         else:
#           i += 1
#       grouped_symbols.append(group)
# print(grouped_symbols)
    



#"""Игра "Очко"."""
# cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4  # Колода карт (4 масти)
# random.shuffle(cards)
# user_points = 0

# while True:
#         choice = input("Будете брать карту? (y/n): ").lower()
#         if choice == 'n':
#             print(f"Ваши очки: {user_points}")
#             break
#         elif choice == 'y':
#             card = cards.pop()
#             user_points += card
#             print(f"Вы вытянули карту {card}. Ваши очки: {user_points}")
#             if user_points > 21:
#                 print("Перебор! Вы проиграли.")
#                 break
#             elif user_points == 21:
#                 print("Поздравляю, вы выиграли!")
#                 break
#         else:print("Пожалуйста, введите 'y' или 'n'.")
