import urllib
import urllib.request

try:
    site = urllib.request.urlopen(('http://www.pudim.com.br'))
except urllib.error.URLError:
    print('O site pudim \033[31mNÃO\033[m está acessivel no momento.!')
else:
    print('O site puim \033[32mEstá\033[m acessível!')
    #print(site.read())