# python3.7.3
# Author: Erick Enriquez - eenriquez@stanford.edu
# landtalk.py - We're gonna do some stuff with our data, not sure what that looks like yet.
import openpyxl, pprint, os #useful imports

#These two paths should be modified by each user.
xmlPath = '/Users/Home/desktop/mallet-files/python-stuff/scraped.xlsx'
resultPath = '/Users/Home/desktop/mallet-files/python-stuff/conversationResults/conversation'
landTalkWorkBook = openpyxl.load_workbook(xmlPath)

#Attributes common to all conversations
conversationAttributes = ['sourceUrl', 'url', 'title', 'lat', 'long', 'oldLook', 'newLook', 'historicActs', 'currActs', 'vidUrl', 'sum', 'trans']

# Takes a row corresponding to a single conversation and returns a dictionary of its
# attributes to the values written on the spreadsheet.
def populate_conversation_data(currRow, attributes):
    currConv = {}
    for i in range(len(attributes)):
        currConv[attributes[i]] = str(currRow[i].value)
    
    return currConv

# Takes in a sheet containing information about all the conversations
# and uses that data to create an array of conversation data.
def populate_conversation_sheet_data(sheet, attributes):
    sheetData = []
    for i in range(sheet.max_row):
        currFile = populate_conversation_data(list(sheet.rows)[i], attributes)
        sheetData.append(currFile)
    return sheetData

# Writes all data from a given structure into a master file.
def write_master_file(data):
	print('Writing Master File...')
	masterFile = open('master-conversation-file', 'w')
	masterFile.write(pprint.pformat(data))
	masterFile.close()
	print('Done.')

# Writes a given attribute to a given file and adds delimeters to ensure clean reading by other tools.
def write_attr(attr, data, index, file):
	file.write(data[index][attr])
	file.write('. ')

# Writes relevant data from the xmlData we extracted such that each conversation contains its own file in the folder 'conversationResults'.
def write_conversation_files(xmlData):
	print('Writing conversation files...')
	for i in range(len(xmlData)):
		resultFile = open(resultPath + str(i), 'w')
		write_attr('title', xmlData, i, resultFile)
		write_attr('oldLook', xmlData, i, resultFile)
		write_attr('newLook', xmlData, i, resultFile)
		write_attr('historicActs', xmlData, i, resultFile)
		write_attr('currActs', xmlData, i, resultFile)
		write_attr('sum', xmlData, i, resultFile)
		write_attr('trans', xmlData, i, resultFile)
		resultFile.close()
	print('Done.')


landTalkData = populate_conversation_sheet_data(landTalkWorkBook['Collection1'], conversationAttributes)
write_master_file(landTalkData)
write_conversation_files(landTalkData)
