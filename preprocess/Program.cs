using System;
using System.IO;
using iTextSharp.text.pdf;
using iTextSharp.text.pdf.parser;
using asprise_ocr_api;
using RasterEdge.XDoc.PDF;

namespace preprocess
{
    class program
    {
        static void Main(string[] args)
        {
            program a = new program();
            string url = "/home/dong/text_summarization/doc/vbtc.pdf";
            // Console.WriteLine(a.getTextFromPDF(url));
            // string text = a.getTextFromPDF(url);
            // Console.Write(text);       
            a.getText2(url);
        }
        public string getTextFromPDF(string inputFile)
        {
 
            //open file
            PdfReader reader = new PdfReader(inputFile);
            StringWriter output = new StringWriter();
            for (int i = 1; i <= reader.NumberOfPages; i++){
                output.WriteLine(PdfTextExtractor.GetTextFromPage(reader, i, new SimpleTextExtractionStrategy()));
                output.WriteLine("\n");
                output.WriteLine("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            }
            return output.ToString();
 
        }
        public void getText2(string inputFile){
              // Open a PDF file.
            String inputFilePath = inputFile;
            PDFDocument doc = new PDFDocument(inputFilePath);

            // The folder that contains '.traineddata' files.
            OCRHandler.SetTrainResourcePath(@"D:\Alice\DLL\Source\");
            // Set output file path.
            Stream[] streams = new MemoryStream[doc.GetPageCount()];
            for (int i = 0; i < doc.GetPageCount(); i++)
            {
                BasePage page = doc.GetPage(i);
                streams[i] = new MemoryStream();
                //the default resolution is 96, if you set larger, it will be helpful to recognize the text, but it can't be too large.
                Bitmap bmp = page.ConvertToImage(96);//192,288....
                OCRPage ocrPage = OCRHandler.Import(bmp);
                ocrPage.Recognize();
                ocrPage.SaveTo(MIMEType.DOCX, streams[i]);
                streams[i].Seek(0, SeekOrigin.Begin);
            }
            DOCXDocument.CombineDocument(streams, @"C:\output.docx");
        }
    }
}

