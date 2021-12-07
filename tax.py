import os, textract, re, sys, webbrowser
from pathlib import Path

# function to operate on each file
# extract the total and append to txt file
def extract_total(filename):
  invTotalRegEx = re.compile(r'Total\n\nGBP\s*(\d,?\d+).00')
  # next 2 lines are to extract text from pdf then convert to a format usable with python3 strings
  text = textract.process(f"{filename}")
  op_text = text.decode('utf-8')
  # regex is applied and group 1 should contain the number
  mo = invTotalRegEx.search(op_text)

  return mo.group(1).replace(',', '')

def invoiceTotaller():
  #  get argv command line argument for filepath
  cmd_args = sys.argv
  # guard clause for if no path is given
  if len(cmd_args) > 1:
    # extract the arguments after script name and turn them to a path for whichever os
    subFolder = Path(*cmd_args[1:])
    # get home folder then concatenate with path given to chage dir of script operation
    homeFolder = str(Path.home())
    filePath = homeFolder / subFolder
    os.chdir(filePath)

  # clear out text file with nums and total
  if os.path.exists("save.txt"):
    os.remove("save.txt")
 # initialise array for values
  invoiceValues = []
  # loop through directory inspecting all files
  for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
      invoiceValues.append(int(extract_total(filename)))

  # script for totalling the file

  # opening a file and then appending the total to it
  file = open('save.txt', 'a')
  for x in invoiceValues:
    file.write(f'{x}\n')
  # writing a string with interpolation to the txt file
  file.write(f'\n\ntotal: {sum(invoiceValues)}')

  print(f'check {str(os.getcwd())} to see your save file with values and a total')
  webbrowser.open(f'file:///{str(os.getcwd())}')


if __name__ == "__main__":
  invoiceTotaller()
