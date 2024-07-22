class EuropeanSocketInterface:
    def voltage(self):
        return 230
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def earth(self):
        return 0
    
class AmericanSocketInterface:
    def voltage(self):
        return 120
    
    def live(self):
        return 1
    
    def neutral(self):
        return 0
    
class EuropeanToAmericanAdapter(AmericanSocketInterface):
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        return 120
    
    def live(self):
        return self.european_socket.live()
    
    def neutral(self):
        return self.european_socket.earth()
    
if __name__ == '__main__':
    european_socket = EuropeanSocketInterface()
    adapter = EuropeanToAmericanAdapter(european_socket)

    print(f"voltage: {adapter.voltage()}")
    print(f"live: {adapter.live()}")
    print(f"neutral: {adapter.neutral()}")