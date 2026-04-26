from sys import version_info as _version_info_
import Ice, IcePy
 
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'
 
_M_Demo._t_Printer = IcePy.defineValue('::Demo::Printer', Ice.Value, -1, (), False, True, None, ())
 
if 'PrinterPrx' not in _M_Demo.__dict__:
    _M_Demo.PrinterPrx = Ice.createTempClass()
    class PrinterPrx(Ice.ObjectPrx):
 
        def printString(self, s, context=None):
            return _M_Demo.Printer._op_printString.invoke(self, ((s, ), context))
 
        def printStringAsync(self, s, context=None):
            return _M_Demo.Printer._op_printString.invokeAsync(self, ((s, ), context))
 
        def printUpperCase(self, s, context=None):
            return _M_Demo.Printer._op_printUpperCase.invoke(self, ((s, ), context))
 
        def printUpperCaseAsync(self, s, context=None):
            return _M_Demo.Printer._op_printUpperCase.invokeAsync(self, ((s, ), context))

        def printCount(self, s, context=None):
            return _M_Demo.Printer._op_printCount.invoke(self, ((s, ), context))
 
        def printCountAsync(self, s, context=None):
            return _M_Demo.Printer._op_printCount.invokeAsync(self, ((s, ), context))
 
        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.PrinterPrx.ice_checkedCast(proxy, '::Demo::Printer', facetOrContext, context)
 
        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.PrinterPrx.ice_uncheckedCast(proxy, facet)
 
        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'
 
    _M_Demo._t_PrinterPrx = IcePy.defineProxy('::Demo::Printer', PrinterPrx)
    _M_Demo.PrinterPrx = PrinterPrx
    del PrinterPrx
 
    _M_Demo.Printer = Ice.createTempClass()
    class Printer(Ice.Object):
 
        def ice_ids(self, current=None):
            return ('::Demo::Printer', '::Ice::Object')
 
        def ice_id(self, current=None):
            return '::Demo::Printer'
 
        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'
 
        def printString(self, s, current=None):
            raise NotImplementedError("servant method 'printString' not implemented")
 
        def printUpperCase(self, s, current=None):
            raise NotImplementedError("servant method 'printUpperCase' not implemented")
 
        def printCount(self, s, current=None):
            raise NotImplementedError("servant method 'printCount' not implemented")
 
        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_PrinterDisp)
 
        __repr__ = __str__
 
    _M_Demo._t_PrinterDisp = IcePy.defineClass('::Demo::Printer', Printer, (), None, ())
    Printer._ice_type = _M_Demo._t_PrinterDisp
 
    Printer._op_printString = IcePy.Operation(
        'printString', Ice.OperationMode.Normal, Ice.OperationMode.Normal,
        False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
 
    Printer._op_printUpperCase = IcePy.Operation(
        'printUpperCase', Ice.OperationMode.Normal, Ice.OperationMode.Normal,
        False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
 
    Printer._op_printCount = IcePy.Operation(
        'printCount', Ice.OperationMode.Normal, Ice.OperationMode.Normal,
        False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
 
    _M_Demo.Printer = Printer
    del Printer
    
_M_Demo._t_Scanner = IcePy.defineValue('::Demo::Scanner', Ice.Value, -1, (), False, True, None, ())
 
if 'ScannerPrx' not in _M_Demo.__dict__:
    _M_Demo.ScannerPrx = Ice.createTempClass()
    class ScannerPrx(Ice.ObjectPrx):
 
        def scanDocument(self, filename, context=None):
            return _M_Demo.Scanner._op_scanDocument.invoke(self, ((filename, ), context))
 
        def scanDocumentAsync(self, filename, context=None):
            return _M_Demo.Scanner._op_scanDocument.invokeAsync(self, ((filename, ), context))
 
        def getStatus(self, context=None):
            return _M_Demo.Scanner._op_getStatus.invoke(self, ((), context))
 
        def getStatusAsync(self, context=None):
            return _M_Demo.Scanner._op_getStatus.invokeAsync(self, ((), context))
 
        def resetScanner(self, context=None):
            return _M_Demo.Scanner._op_resetScanner.invoke(self, ((), context))
 
        def resetScannerAsync(self, context=None):
            return _M_Demo.Scanner._op_resetScanner.invokeAsync(self, ((), context))
 
        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.ScannerPrx.ice_checkedCast(proxy, '::Demo::Scanner', facetOrContext, context)
 
        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.ScannerPrx.ice_uncheckedCast(proxy, facet)
 
        @staticmethod
        def ice_staticId():
            return '::Demo::Scanner'
 
    _M_Demo._t_ScannerPrx = IcePy.defineProxy('::Demo::Scanner', ScannerPrx)
    _M_Demo.ScannerPrx = ScannerPrx
    del ScannerPrx
 
    _M_Demo.Scanner = Ice.createTempClass()
    class Scanner(Ice.Object):
 
        def ice_ids(self, current=None):
            return ('::Demo::Scanner', '::Ice::Object')
 
        def ice_id(self, current=None):
            return '::Demo::Scanner'
 
        @staticmethod
        def ice_staticId():
            return '::Demo::Scanner'
 
        def scanDocument(self, filename, current=None):
            raise NotImplementedError("servant method 'scanDocument' not implemented")
 
        def getStatus(self, current=None):
            raise NotImplementedError("servant method 'getStatus' not implemented")
 
        def resetScanner(self, current=None):
            raise NotImplementedError("servant method 'resetScanner' not implemented")
 
        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_ScannerDisp)
 
        __repr__ = __str__
 
    _M_Demo._t_ScannerDisp = IcePy.defineClass('::Demo::Scanner', Scanner, (), None, ())
    Scanner._ice_type = _M_Demo._t_ScannerDisp
 
    Scanner._op_scanDocument = IcePy.Operation(
        'scanDocument', Ice.OperationMode.Normal, Ice.OperationMode.Normal,
        False, None, (), (((), IcePy._t_string, False, 0),), (), IcePy._t_string, ())
 
    Scanner._op_getStatus = IcePy.Operation(
        'getStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal,
        False, None, (), (), (), IcePy._t_string, ())
 
    Scanner._op_resetScanner = IcePy.Operation(
        'resetScanner', Ice.OperationMode.Normal, Ice.OperationMode.Normal,
        False, None, (), (), (), None, ())
 
    _M_Demo.Scanner = Scanner
    del Scanner