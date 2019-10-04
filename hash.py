#   File: hash.py
#   By: Oliver Calder, 31 December 2018

import sys
import os
import subprocess

difficulty = sys.argv[1]
data_list = sys.argv[2:]
data = data_list[0]

i = 1
items = len(data_list)
while i < items:
    data = data + ' ' + item_list[i]

orig_data = data
print(orig_data)

new_hash = subprocess.check_output('echo -n '+data+' | sha256sum', shell=True)
hash = new_hash.split()[0]
#new_hash = new_hash[0]
print(hash)

hash = hash.split("'")[1]
print('hash:', hash)
nonce = 0
while new_hash[:difficulty] != '0'*difficulty:
    nonce =+ 1
    new_hash = subprocess.check_output('echo -n '+data+nonce+' | sha256sum', shell=True)
    new_hash.split(' ')
    hash = new_hash[0]

print(nonce)
print(hash)
