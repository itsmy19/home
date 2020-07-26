"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""
############################################################################################
import sys

strings = []
for s in sys.argv[1:]:
    strings += [s]

def palindrome(word):
    if ' ' in word:
       word = "".join(sys.argv).replace(" ","")
    palindrome = reversed(word)
    for letter, rev_letter in zip(word, palindrome):
        if letter != rev_letter:
            return 'Not Palindrome'
    return 'Palindrome'

def printpalindromes(strings):
    for s in strings:
        if is_palindrome(s) == True:
            print(s)

printpalindromes(strings)