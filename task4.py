"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
###########################################################################################################################
v_dir = {'romanov' : 'parol1', 'lenin' : 'parol2', 'stalin' : 'parol3', 'hrushov' : 'parol4', 'brezhnev' : 'parol5',
         'andropov' : 'parol6', 'chernenko' : 'parol7', 'gorbachev' : 'parol8', 'elcin' : 'parol9'}

complete = False
while not complete:
    username = input("What is the username?")
    password = input("What is the password?")
    conf_username = input("Repeat the username?")
    conf_password = input("Repeat the password?")

    if username != conf_username or password != conf_password:
        print("username or password does not match")
        continue
    if not username in v_dir:
        print("Input username again!")
        continue
    if password == v_dir[username]:
        print("User has been identified, Welcome",username)
        complete = True
    else:
        print("Input password again")
######################################################################################################################
import time
complete = False
user = [['romanov','parol1'],['lenin','parol2'],['stalin','parol3'],['hrushov','parol4'],['brezhnev','parol5'],
        ['andropov','parol6'],['chernenko','parol7'],['gorbachev','parol8'],['elcin','parol9']]

while not complete:
    username = input("What is the username?")
    password = input("What is the password?")
    for n in len(user):
         if username == user[n][0]:
              print("Good!")
              if password == user[n][1]:
                   print("User has been identified, Welcome",username)
                   complete = True
              else:
                   break
                   print("Input password again")
    if not complete:
        print("Input username again!")
##########################################################################################################################
user_pass = {'romanov' : 'parol1', 'lenin' : 'parol2', 'stalin' : 'parol3', 'hrushov' : 'parol4', 'brezhnev' : 'parol5',
         'andropov' : 'parol6', 'chernenko' : 'parol7', 'gorbachev' : 'parol8', 'elcin' : 'parol9'}

while True:
    user = input("Your name")
    pwd = input("Your password")

    if user in user_pass and pwd == user_pass[user]:
        print("Welcome", user)
        break
    else:
        user_pass[user]=pwd
        print("registration completed,please login")