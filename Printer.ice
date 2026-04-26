module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpperCase(string s);  
        void printCount(string s);
    }

    interface Scanner
    {
        string scanDocument(string filename);
        string getStatus();
        void   resetScanner();
    }
}
