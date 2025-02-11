# -*- coding: utf-8 -*-
"""Copy of password_gen_sav.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wYA5KPtgx5fWyif4TLTGq1tCffspAEBw
"""

dict_word_enc = {}
dict_word_dec = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def set_converter():
  x = 123
  for i in letters:
    dict_word_enc[i] = x
    dict_word_dec[x] = i
    x += 111

set_converter()

def encode(password):
  hashed = ""
  lower_password = password.lower()
  x = 0
  for i in lower_password:
    if not x <= 0:
      word = ',' + str(dict_word_enc[i])
    else:
      word = str(dict_word_enc[i])
    hashed += word
    x += 1
  return hashed

hashed = encode('Lincoln')
print(hashed)

def decode(hashed_word):
  h_word = hashed_word.split(',')
  word = ''
  for i in h_word:
    word += dict_word_dec[int(i)]
  print(word)
  #print(letters[35])
  '''length = len(str(hashed))
  for i in str(hashed):
    print(letters[length])
    length -= 1'''

decode(hashed)

users = {}
def add_user(name, password, password2):
  password_enc = encode(password)
  password2_enc = encode(password2)
  user_dic = {
      'id': len(users) + 1,
      'name': name,
      'password': password_enc,
      'second password': password2_enc 
  }
  users[user_dic['name']] = user_dic
  print('completed')

def seperate(words):
  x = words.split(' ')
  return x

def program():
  x = True
  
  while x:
    print('Welcome to the password generater and saver')
    p = input("Would you like to continue yes or no")
    if p.lower() == 'yes':
      print('Please enter name, password, and second password in case you forget your orginal password')
      new_input = input()
      x = seperate(new_input)
      add_user(x[0], x[1], x[2])
    inp = input('would you like to check your password yes or no')
    if inp.lower() == 'yes':
      name = input('what is your name')
      print(decode(users[name]['password']))
    else:
      x = False

program()

add_user('Lincoln', 'Littlemac06', 'cool')
print(decode(users['Lincoln']['password']), decode(users['Lincoln']['second password']))

print(users)







