import os
import socket
import tqdm


def main():
    try:
        port = 9999
        host = ""
        filename = "levis.txt"
        s = socket.socket()
        s.bind((host, port))
        s.listen(5)
        print("Server is listening ....")
        filesize = os.path.getsize(filename)
        while True:
            conn, address = s.accept()
            # print("Connected.")
            # data = conn.recv(1024)
            # print("Server has recieved ", repr(data))
            progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

            f = open(filename, "rb")
            l = f.read(1024)
            while l:
                conn.send(l)
                progress.update(len(l))
                print("Sent ", repr(l))
                l = f.read(1024)
            f.close()
            print("Finished sending data.")
            # msg = "Thank you for connecting."
            # conn.send(str.encode(msg))
            conn.close()
            print("Connection closed")
            s.close()
            print("Socket closed")
    except socket.error as e:
        print(f"Error {e} has occurred!")


main()
