import hashlib

secret = 'bgvyzdsv'

n = 0
while True:
    if hashlib.md5(secret + str(n)).hexdigest().startswith('00000'):
        break
    n += 1
print n