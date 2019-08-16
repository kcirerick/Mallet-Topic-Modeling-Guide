# python 3.7.3
# Author: Erick Enriquez
# I'm gonna use ths file to do some quick maths and graphing of data on here.
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
def load_data():
	wb = op.load_workbook(compXlPath)
	sheet = wb[compSheet]
	return sheet

# Takes in a sheet and returns a list containing the sums of each of its columns from the designated first column to
# the last available column.
def sum_data(sheet):
	colRangeStart = firstScrapedCol
	colRangeEnd = sheet.max_column
	return sum_each_column(colRangeStart, colRangeEnd, sheet)
     

def create_histogram(xValues, yValues):
	xEdges = x_edges(len(xValues))
	np.histogram2d(xValues, yValues)


sheet = load_data()
weightedValues = sum_data(sheet)
numTopics = len(weightedValues)
xValues = range(numTopics)
create_histogram(xValues, weightedValues)