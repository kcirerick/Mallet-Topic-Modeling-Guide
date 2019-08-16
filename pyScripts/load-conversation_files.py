# python3.7.3
# Author: Erick Enriquez - eenriquez@stanford.edu
# landtalk.py - We're gonna do some stuff with our data, not sure what that looks like yet.
import openpyxl, pprint, os #useful import packages
from paths import *
from dataFields import *
from workBooks import *

# Takes a row corresponding to a single conversation and returns a dictionary of its
# attributes to the values written on the spreadsheet.
def pull_conversation_data(currRow, fields):
    currConv = {}
    for i in range(len(fields)):
        currConv[fields[i]] = str(currRow[i].value)
    return currConv

# Takes in a sheet containing information about all the conversations
# and uses that data to create a list of conversation data.
def organize_data(sheet, fields):
    sheetData = []
    for i in range(sheet.max_row):
        currFile = pull_conversation_data(list(sheet.rows)[i], fields)
        sheetData.append(currFile)
    return sheetData

# Writes a given attribute to a given file and adds delimeters to ensure clean reading by other tools.
def write_fields(data, index, file):
	for i in range(len(cleanData)):
		file.write(data[index][cleanData[i]])
		file.write('. ')

# Writes relevant data from the xmlData we extracted such that each conversation contains its own file in the folder 'conversationResults'.
def write_conversation_files(xmlData):
	print('Writing conversation files...')
	for i in range(len(xmlData)):
		resultFile = open(conversationResultPath + str(i), 'w')
		write_fields(xmlData, i, resultFile)
		resultFile.close()
	print('Done.')

landTalkWorkBook = openpyxl.load_workbook(scrapedDataPath)
data = landTalkWorkBook[collectionSheet]
write_conversation_files(data, convDataFields)