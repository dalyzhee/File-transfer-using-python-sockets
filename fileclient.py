import socket


def main():
    try:
        port = 9999
        host = "127.0.0.1"
        s = socket.socket()
        s.connect((host, port))
        # s.send("Hello server", "utf-8")
        with open('filename.txt', "wb") as f:
            print("File is opened.")
            while True:
                print("Recieving data ...")
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                f.write(data)
        f.close()
        print("Succefully recieved the file.")
        s.close()
        print("Connection closed.")
    except socket.error as e:
        print(f"Error {e} has occured")


main()
