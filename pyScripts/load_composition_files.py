# python 3.7.3
# Author: Erick Enriquez
import openpyxl
from paths import *

# This function takes in the desired name of a new spreadsheet and the desired path
# of a new excel file and creates a workbook with the specified sheet name. This function
# returns that sheet.
def initialize_spreadsheet(sheetName, wb):
	sheet = wb.active
	sheet.title = compSheet
	wb.save(filename = compXlPath)
	return sheet

# Opens a file and reads each line from the file into a list object. This
# function returns that list.
def initialize_content(contentPath):
	compFile = open(contentPath)
	compContent = compFile.readlines()
	return compContent

# This function takes in a list of strings and tokenizes each string and creates a
# list of each token in that line and appends these tokens to a two-dimensional
# list of tokens.
def tokenize_content(content):
	tokenizedContent = []
	for currLine in content:
		parsedLine = currLine.split()
		tokenizedContent.append(parsedLine)
	return tokenizedContent

# Takes in a sheet object and a list of lists containing each token in a file.
# This function writes that list into the sheet.
def write_to_spreadsheet(sheet, content):
	cellRow = 1
	cellCol = 1
	print(sheet.title)
	for currLine in content:
		for currToken in currLine:
			sheet.cell(row = cellRow, column = cellCol).value = currToken
			cellCol += 1
		cellCol = 1
		cellRow += 1

compDataWorkBook = openpyxl.Workbook()
currSheet = initialize_spreadsheet(sheetTitle, compDataWorkBook)
compContent = initialize_content(compDataPath)
parsedContent = tokenize_content(compContent)
write_to_spreadsheet(currSheet, parsedContent)
wb.save(compXlPath)




