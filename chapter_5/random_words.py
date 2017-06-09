# Создайте программу, которая будет выводить список слов в случайном порядке.
# На экране должны печататься без повторений все слова из представленного списка

import random
list_of_words = ['wake', 'up', 'Neo']
random.shuffle(list_of_words)
print(list_of_words)
