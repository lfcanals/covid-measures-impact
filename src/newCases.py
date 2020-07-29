import sys
import process as p


#
# Main program arguments:
#
#   argument1 : classes file name
#   argument2 : data file name
#


if len(sys.argv) != 2:
  print("Usage:");
  print("        classesFileName: csv file with location and starting date")
  print("                         for each class")
  print("        dataFileName:    csv with column numerical data for each ")
  print("                         location and dates")
  print()
  print("Starting date will be 2020-04-15 and considered columns for output")
  print("will be new_cases_per_million and new_tests_per_thousand");
  print("Results will be writen into file name 'output.csv'")
  print()
else:
  p.process(sys.argv[1], sys.argv[2], '2020-04-15', \
    ['date','location','class','new_cases_per_million',\
    'new_tests_per_thousand'], 'output.csv')
