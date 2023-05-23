import os

ip_ou_host = input("Digite o ip ou host para ser verificado: ")

os.system('ping -n 6 {}'.format(ip_ou_host)) ##chamando system da biblioteca os | comando -n (numero de pacotes)