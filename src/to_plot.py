import sys
import random
import csv
import datetime

#
# parameter:
#   inputFileName: csv result of process with columns
#       date,location,class,val1,val2,...
#
#   outputFileName: csv SEPARATED-BY-SEMICOLON (;) with these values:
#         date,location,class,val1,val2...,Y
#       Y will be set randomly in the environment of class to not mix with
#       other classes.
#
def to_plot(inputFileName, outputFileName):
  with open(inputFileName) as inputFile, open(outputFileName,'w') as outputFile:
    reader = csv.reader(inputFile)
    header = next(reader)
    headerMap = {}
    for i in range(len(header)): headerMap[header[i].lower()] = i
    headerMap['Y'] = len(header)

    writer = csv.writer(outputFile, delimiter=';')
    writer.writerow(headerMap.keys())

    for row in reader:
      Y = int(row[headerMap['class']])
      Y += Y + (random.random()-0.5)*2
      resultingRow = row
      resultingRow.append(Y)

      writer.writerow(resultingRow)


if len(sys.argv) != 3:
  print("Usage:")
  print("        inputFileName: csv result of processing with 'process.py'")
  print("        outputFile: csv separated by semi-colon with Y to plot clouds")
  print
else:
  to_plot(sys.argv[1], sys.argv[2])
