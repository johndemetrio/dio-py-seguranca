import hashlib

arquivo1 = 'Segurança da informação\hashteste.txt'
arquivo2 = 'Segurança da informação\hashteste2.txt'

hash1 = hashlib.new('md4') #parametro de qual modelo hash iremos usar

hash1.update(open(arquivo1, 'rb')).read()

hash2 = hashlib.new('md4')

hash2.update(open(arquivo2, 'rb')).read()

if hash1.digest() != hash2.digest():
    print(f'O arquivo 1: {arquivo1}, é diferente do arquivo 2: {arquivo2}')
else:
    print(f'O arquivo 1: {arquivo1}, é igual ao arquivo 2: {arquivo2}')