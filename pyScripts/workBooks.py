# python 3.6.3
# Author: Erick Enriquez
# This file allows you to load data from a spreadsheet into an openpyxl workbook and also allows you to create a new spreadsheet
# for loading data.
import openpyxl as op
from paths import *
landTalkWorkBook = openpyxl.load_workbook(scrapedDataPath)
