import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)
 
base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 98.90.53.6 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 98.90.53.6 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
 
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy para Printer")
 
base_s = communicator.stringToProxy("SimpleScanner:tcp -h 98.90.53.6 -p 11000")
scanner = Demo.ScannerPrx.checkedCast(base_s)
 
if not scanner:
    raise RuntimeError("Invalid proxy para Scanner")
 
print("=== Printer ===")
 
printer1.printString("Hello World from printer1!")
printer2.printString("Hello World from printer2!")
 
printer1.printUpperCase("texto em maiusculas via printer1")
printer2.printUpperCase("texto em maiusculas via printer2")

printer1.printCount("ZeroC ICE")
printer2.printCount("Computacao Distribuida")
 
print("\n=== Scanner ===")
 
print("Status:", scanner.getStatus())
 
resultado1 = scanner.scanDocument("relatorio.pdf")
print("Resultado:", resultado1)
 
resultado2 = scanner.scanDocument("contrato.docx")
print("Resultado:", resultado2)
 
print("Status:", scanner.getStatus())
 
scanner.resetScanner()
print("Status apos reset:", scanner.getStatus())
 
communicator.destroy()