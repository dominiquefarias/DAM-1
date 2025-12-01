class CuentaBancaria():
    def __init__(self):
        self.__saldo= 0
        self.__cliente = ""

# defino setters y getters para el saldo
    def setSaldo(self,nuevosaldo):
        self.__saldo = nuevosaldo
     
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(1000000000)
print(cuentacliente1.getSaldo())
