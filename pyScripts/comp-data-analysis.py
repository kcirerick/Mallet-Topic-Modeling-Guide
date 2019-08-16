# python 3.7.3
# Author: Erick Enriquez
# I'm gonna use ths file to do some quick maths and graphing of data on here.
import os, pprint, openpyxl as op

def do_sum(col):
	sum = #apply sum formula here

# Iterates through each column designated and appends the sum of values in that column to a list. 
# This function will return that list of summed data.
def sum_each_column(start, end, sheet, rowNum):
	data = []
	for i in range(start, end):
		currSum = do_sum(sheet.column[i])
		data.append(currSum)
	return data

# Loads the workbook containing the composition data, gets the appropriate sheet, and returns the summed values of 
# each column containing weighted data.
def load_data():
	wb = openpyxl.load_workbook(compXlPath)
	sheet = wb[compSheet]
	rowNum = sheet.max_rows + 1
	colRangeStart = #far left data column
	colRangeEnd = #far right data column
	return sum_each_column(colRangeStart, colRangeEnd, sheet, rowNum)
	
def create_histogram():

data = load_data()
summedData = do_sum(data)
create_histogram(summedData)
