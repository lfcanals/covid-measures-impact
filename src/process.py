import read_classes as r
import csv
import datetime

#
# parameter:
#   columns: array of string with column names  to show in lowercasse.
#            for example ['date','location','class','new_cases_per_million']
#   firstDate: YYYY-mm-dd first date from consider data
#
def process(classFileName, dataFileName, firstDateStr, columns, outputFileName):
  firstDate = datetime.datetime.strptime(firstDateStr, '%Y-%m-%d')
  classifier = r.read_classes(classFileName)

  with open(dataFileName) as dataFile, open(outputFileName,'w') as outputFile:
    reader = csv.reader(dataFile)
    header = next(reader)
    headerMap = {}
    for i in range(len(header)): headerMap[header[i].lower()] = i
    headerMap['class'] = len(header)

    writer = csv.writer(outputFile)
    writer.writerow(columns)

    for row in reader:
      if datetime.datetime.strptime(row[headerMap['date']], '%Y-%m-%d') \
          < firstDate: continue
      row.append(classifier.get_class(row[headerMap['location']], \
          row[headerMap['date']]))

      resultingRow = []
      for column in columns: 
        resultingRow.append(row[headerMap[column]])

      writer.writerow(resultingRow)

