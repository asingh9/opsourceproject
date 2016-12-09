### TLDR

##### Origin
This project originated as a tool to parse long documents for important information and be able to summarize it in a visually appealing fashion that can be easily digestible by someone interested in the subject but with little time or patience to sift through a lengthy body of work. The intended use would be for legal documents, long transcripts, or any political filings/briefings too long for the average person to realistically read. 

##### Progress
I have created a command-line python program that scans a PDF document and outputs as many of the most frequent words as specified by user. The program outputs to the shell a list of words and their corresponding frequencies as found in the document. Using Python libraries matplotlib and pandas, the results are plotted as a bar graph for visual feedback. Unfortunately, with little time and effort spent on this project, this is the current state of the tool. Another goal of mine was to develop a web framework to encapsulate the aforementioned functionality but the main challenge proved to be lack of familiarity with web development issues and inability to learn a new framework within a short time period. I chose Django as a web framework based on its relationship with Python, as I chose that for its large extension library. Learning this framework and its nuances took longer than I thought and I spent a lot of time sorting out errors just to get a basic instance running. Eventually I got the front-end to run the way I intended but more issues remainined for connecting the actual word counter functionality.

#### Usage

For the command-line tool, use tldr.py and provide arguments \<inputfile.pdf> and \<numWords>, respectively the PDF file to parse and the number of most frequent words to output.
