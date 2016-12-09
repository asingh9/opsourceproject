import sys, getopt
import PyPDF2
from pymongo import MongoClient
import re
from collections import Counter
import pandas
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use('ggplot')

def open_file(filename):
	# set up PDF reader
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	return pdfReader

def word_summary(reader, numWords):
	# set up PDF reader

	#set up db for storing word information
	#client = MongoClient()
	#client = MongoClient('localhost', 27017) # set to default port
	#db = client.tldr
	#wordcount = db.word_count

	common_words = ['THE', 'BE', 'TO', 'OF', 'AND', 'A', 'IN', 'THAT', 'HAVE', 'I',
				   'IT', 'FOR', 'NOT', 'ON', 'WITH', 'HE', 'SHE', 'AS', 'YOU', 'DO',
				   'AT', 'THIS', 'BUT', 'HIS', 'HER', 'BY', 'FROM', 'THEY', 'WE', 'SAY',
				   'OR', 'AN', 'WILL', 'MY', 'ONE', 'ALL', 'WOULD', 'THERE', 'THEIR', 'WHAT',
				   'SO', 'UP', 'OUT', 'IF', 'ABOUT', 'WHO', 'GET', 'WHICH', 'GO', 'ME',
				   'ANY', 'IS', 'ARE', 'USE', 'YOUR']

	all_counts = []
	total_count = Counter()
	for n in range(reader.numPages):
		page = reader.getPage(n)
		contents = page.extractText().upper()

		words = re.findall(r'\w+', contents)
		new_words = [word for word in words if word not in common_words and len(word) > 2]
		counts = Counter(new_words)
		for word in list(counts):
			total_count[word] += counts[word]

	top = total_count.most_common(numWords)
	print "The most important words found in the document are:"
	print "\tWord" + ' ' * 11 + "Frequency"
	for n, word in enumerate(top):
		print str(n) + "\t" + word[0] + ' ' * (15-len(word[0])) + str(word[1])

	return top

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "usage: tldr.py <input.pdf> <num_words>"
		sys.exit(2)
	if not sys.argv[1].lower().endswith('.pdf'):
		print "usage: input file must be PDF!"
		sys.exit(2)
   	
   	# open file and create PDF reader object
   	reader = open_file(sys.argv[1])
   	# collect word data
   	data = word_summary(reader, int(sys.argv[2]))
   	labels = ['Words','Frequency']
   	# plot data
   	df = pandas.DataFrame.from_records(data, columns=labels)
   	df.plot(kind='bar')
   	plt.show()


