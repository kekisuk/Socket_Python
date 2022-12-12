import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('conectado ao servidor!\n')

def solicitar_arquivo():
    nameFile = str(input('Digite o nome do arquivo solicitado --> '))

    client.send(nameFile.encode())

    with open(nameFile, 'wb') as file:
        while 1:
            data = client.recv(10000000)
            if not data:
                break
            file.write(data)

    print(f'\n{nameFile} recebido!\n')

def menu():
    print("\n--------Bem vindo------\n\n")
    print("Escolha a funcionalidade\n")
    print("1 - Solicitar arquivo\n")
    print("0 - Sair do sistema")

oneBool = True
while oneBool != False:

    menu()
    opcao = int(input('\nDigite o numero da funcionalidade: '))

    if opcao == 0:
        oneBool = False
        print("Encerrando conexão com o servidor...")
        client.close()
    
    if opcao == 1:
        solicitar_arquivo()
        
    

