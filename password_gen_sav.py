# -*- coding: utf-8 -*-
"""password_gen_sav.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cz2lIo-ZEVh0xRlGUjRRknJcenh9irCf
"""

! pip install simple-crypt

from simplecrypt import encrypt, decrypt

import hashlib
users = []

#m = hashlib.sha256()
def generate(password):
  return str(hashlib.sha224(str.encode(password)).hexdigest())

def hash_block(dic):
  x = str.encode(str(dic))
  enc = encrypt(password, message)
  enc = str(hashlib.sha224(x).hexdigest())
  users.append(enc)
  return '{}: at block {}'.format(enc, dic['id'])

def add_user(name, password, password2):
  password_enc = generate(password)
  user_dic = {
      'id': len(users) + 1,
      'name': name,
      'password': password_enc,
      'second password': password2  
  }
  tran = hash_block(user_dic)
  print(tran)
  #users.append(user_dic)

add_user('Lincoln', 'Littlemac678', 'I lived in Manhatton')

print(users)

dic = {'id': 12, 'name': 'Yah, bitch', 'password': 'bruh'}
x = hash_block(dic)
print(x)

dic = {'name': 'Lincoln', 'password': 'The shit'}
x = str.encode(str(dic))
enc = str(hashlib.sha224(x).hexdigest())
print(enc)