import socket


class DeviceController:

    def __init__(self, local_url, device_host, device_port):
        self.local_url = local_url
        self.device_host = device_host
        self.device_port = device_port

    def send(self, char):
        sock = socket.socket()
        sock.connect((self.device_host, self.device_port))

        message = bytes(char, 'utf-8')

        sock.send(message)
        data = sock.recv(1024).decode('utf-8')
        sock.close()

        return data

    def read(self):
        return self.send('1')

    def start_power(self):
        return self.send('2')

    def stop_power(self):
        return self.send('3')

    def start_water(self):
        return self.send('4')

    def stop_water(self):
        return self.send('5')
