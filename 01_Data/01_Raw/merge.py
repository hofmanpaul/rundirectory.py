import csv, codecs				                        
Data=[]

#import BL data
with open('BL_Data.csv', 'rb') as csvfile:
	datareader = csv.reader( codecs.EncodedFile(csvfile, 'utf8', 'utf-8-sig') , delimiter=',', quotechar='|')
	for row in datareader:
		Data.append(row + ['1'])

#import EL data
with open('EL_Data.csv', 'rb') as csvfile:
	datareader = csv.reader( codecs.EncodedFile(csvfile, 'utf8', 'utf-8-sig') , delimiter=',', quotechar='|')
	rowno=0
	for row in datareader:
		if rowno==0:
			rowno+=1
			continue
		else:
			Data.append(row + ['2'])
			rowno+=1

#Fix header row
Data[0]=['ID','Income','Treat','Time']

#Write to new file
with open('../02_Clean/appended.csv', 'wb') as csvfile:
    datawriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in Data:
    	datawriter.writerow(row)
