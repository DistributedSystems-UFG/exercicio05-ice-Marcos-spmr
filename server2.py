import sys, Ice
import Demo

class PrinterI(Demo.Printer):
 
    def __init__(self, t):
        self.t = t
 
    def printString(self, s, current=None):
        print(self.t, s)
 
    def printUpperCase(self, s, current=None):
        print(self.t, s.upper())
 
    def printCount(self, s, current=None):
        print(self.t, f'"{s}" tem {len(s)} caracteres')

class ScannerI(Demo.Scanner):
 
    def __init__(self):
        self._status = "pronto"
 
    def scanDocument(self, filename, current=None):
        print(f"[Scanner] Escaneando: {filename}")
        self._status = f"ultimo escaneamento: {filename}"
        return f"Conteudo simulado de '{filename}': Lorem ipsum..."
 
    def getStatus(self, current=None):
        print(f"[Scanner] Status: {self._status}")
        return self._status
 
    def resetScanner(self, current=None):
        print("[Scanner] Reiniciado.")
        self._status = "pronto"
 
communicator = Ice.initialize(sys.argv)
 
adapter = communicator.createObjectAdapterWithEndpoints(
    "SimpleAdapter", "default -p 11000"
)
 
object1 = PrinterI("Object1 says:")
object2 = PrinterI("Object2 says:")
adapter.add(object1, communicator.stringToIdentity("SimplePrinter1"))
adapter.add(object2, communicator.stringToIdentity("SimplePrinter2"))
 
scanner = ScannerI()
adapter.add(scanner, communicator.stringToIdentity("SimpleScanner"))
 
adapter.activate()
print("Servidor pronto (porta 11000)...")
communicator.waitForShutdown()