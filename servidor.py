import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7777))
server.listen(1)
print("[ESCUTANDO] Servidor esta esperando algum cliente.")
client_socket, address = server.accept()
print('Conectado a:', str(address))
name_file = client_socket.recv(1024).decode() 

print(f"Nome do arquivo solicidado: ({name_file}) foi recebido pelo servidor")

try:
    with open(name_file, 'rb') as file:
        for data in file.readlines():
            client_socket.send(data)

            print("Arquivo enviado!")

except Exception as e:
    print("Falha ao enviar arquivo!")

finally:
    client_socket.close()


