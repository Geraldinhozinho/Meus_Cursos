import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except:
    print('\033[1;31mO site Pudim não esta acessivel no momento\033[m')
else:
    print('\033[1;32mO site Pudim esta acessivel no momento\033[m')