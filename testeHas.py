import hashlib

texto = 'teste'
hash = hashlib.md5(b'teste')
print(hash.hexdigest())