# python 3.7.3
# Author: Erick Enriquez
# comp_data_analysis.py - Calculates the sum of each row of weighted topic values in the output composition data sheet
# and writes them to the bottom of each column for later analysis.
import os, pprint, openpyxl as op, numpy as np
from paths import *

# Takes in a column and a number of rows and sums each cell within that range and corresponding column
# and returns this sum.
def do_sum(col, rowCount):
	sum = 0
	for row in range(0, rowCount):
		sum += float(col[row].value)
	return sum

# Iterates through each column designated and appends the sum of values in that column to a list. 
# This function will return that list of summed data.
def sum_each_column(start, end, sheet):
	data = []
	for col in sheet.iter_cols(min_col=start, max_col=end):
		sumCurrCol = do_sum(col, sheet.max_row)
		data.append(sumCurrCol)
	return data

# Loads the workbook containing the composition data, gets the appropriate sheet, and returns the summed values of 
# each column containing weighted data.
def load_data(path):
	wb = op.load_workbook(path)
	return wb

# Takes in a sheet and returns a list containing the sums of each of its columns from the designated first column to
# the last available column.
def sum_data(sheet):
	colRangeStart = firstScrapedCol
	colRangeEnd = sheet.max_column
	return sum_each_column(colRangeStart, colRangeEnd, sheet)

# Writes the sums of all columns in the sheet to the row immediately following the final conversation entry in composition
# data output file.
def write_sum(values, sheet, wb):
    writeRow = sheet.max_row + 1
    sheet.cell(row=writeRow, column=1).value = 'Summed Values'
    for i in range(len(values)):
        sheet.cell(row=writeRow, column=i + firstScrapedCol).value = values[i]
    wb.save(filename = compXlPath)


# Initializes excel sheet
wb = load_data(compXlPath)
sheet = wb[compSheet]

# Values to be used for graphing/visualization techniques.
weightedValues = sum_data(sheet)
numTopics = len(weightedValues)

write_sum(weightedValues, sheet, wb)
