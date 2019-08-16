# python 3.7.3
# Author: Erick Enriquez
# I'm gonna use ths file to do some quick maths and graphing of data on here.
import os, pprint, openpyxl as op
from paths import *

def do_sum(col, rowCount):
	for cell in range(firstScrapedRow, rowCount)
		sum += cell.value
	return sum

# Iterates through each column designated and appends the sum of values in that column to a list. 
# This function will return that list of summed data.
def sum_each_column(start, end, sheet):
	data = []
	for col in sheet.iter_cols(min_col=start, max_col=end, sheet.max_rows):
		sumCurrCol = do_sum(col)
		data.append(sumCurrCol)
	return data

# Loads the workbook containing the composition data, gets the appropriate sheet, and returns the summed values of 
# each column containing weighted data.
def load_data():
	wb = openpyxl.load_workbook(compXlPath)
	sheet = wb[compSheet]
	return sheet

def sum_data(sheet):
	colRangeStart = firstScrapedCol
	colRangeEnd = sheet.max_col
	return sum_each_column(colRangeStart, colRangeEnd, sheet)
	
def create_histogram(x, y):

sheet = load_data()
verticalValues = sum_data(sheet)
horizontalValues = sheet.max_col - firstScrapedCol
create_histogram(horizontalValues, verticalValues)
