import os
import textract
import re
import sys
from pathlib import Path

# TODO get argv command line argument for filepath
stuff = sys.argv
if len(stuff) > 1:
  subFolder = Path(*stuff[1:])

  homeFolder = str(Path.home())
  ting = homeFolder / subFolder
  # print(str(ting))
# set directory for this page
if ting:
  os.chdir(ting)
else:
  os.chdir('.')
# clear out text file with nums and total
if os.path.exists("save.txt"):
  os.remove("save.txt")

# function to operate on each file
# extract the total and append to txt file
def extract_total(filename):
  invTotalRegEx = re.compile(r'Total\n\nGBP\s*(\d,?\d+).00')
  # next 2 lines are to extract text from pdf then convert to a format usable with python3 strings
  text = textract.process(f"{filename}")
  op_text = text.decode('utf-8')
  # regex is applied and group 1 should contain the number
  mo = invTotalRegEx.search(op_text)
  #print(mo.group(1))
  payment = mo.group(1).replace(',', '')
  #payment = payment.replace(',', '')
  # print(payment)
  # add value to file for totalling
  saver = open('save.txt', 'a')
  saver.write(f'{payment}\n')


# loop through directory inspecting all files
for filename in os.listdir('.'):
  if filename.endswith(".pdf"):
    extract_total(filename)


# script for totalling the file
filey = open('save.txt')
content = filey.readlines()
filey.close


# create list of integers for summing, bit of cleaning first
# this is a list comprehension
num_list = [ int(x.strip()) for x in content]
total = sum(num_list)

# opening a file and then appending the total to it
file2 = open('save.txt', 'a')
# writing a string with interpolation to the txt file
file2.write(f'\n\ntotal: {total}')

print(f'check {str(os.getcwd())} to see your save file with values and a total')
