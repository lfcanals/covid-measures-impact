import sys
import process as p


#
# Main program arguments:
#
#   argument1 : classes file name
#   argument2 : data file name
#

p.process(sys.argv[1], sys.argv[2], '2020-04-15', \
  ['date','location','class','new_cases_per_million','new_tests_per_thousand'],\
  'output.csv')
