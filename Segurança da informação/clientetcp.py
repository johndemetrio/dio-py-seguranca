import sys
import os
import socket

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A conexão falhou.")
        print("Erro: {}".format(error))
        sys.exit()
    
    print("Socket criado com sucesso")
    
    HostAlvo = input("Digite o host ou o ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP conectado com sucesso no host: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as error:
        print("A conexão falhou")
        print("Erro: {}".format(error))
        sys.exit()

if __name__ == "__main__":
    main()