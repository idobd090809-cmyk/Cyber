import socket
import  os
import struct

HOST = "0.0.0.0"
PORT = 12345

File_Send = r""

def send_file():

    file_name = os.path.basename(File_Send).encode("utf-8")
    file_size = os.path.getsize(File_Send)

    print(f"Sending file: {file_name.decode()}")
    print(f"File size: {file_size} bytes")
    print(f"Sending to {HOST}:{PORT}")


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        client_socket.sendall(struct.pack("!I", len(file_name)))
        client_socket.sendall(struct.pack("!Q", file_size))
        client_socket.sendall(file_name)

        with open(File_Send,"rb") as file:
            while chunk:=file.read(4096):
                client_socket.sendall(chunk)

    print("File sent successfully")


if __name__ == "__main__":
        send_file()

