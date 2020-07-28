import csv
import datetime


class classifier():
  #
  # parameters:
  #   classes: a dictionary of country versus array of classes
  #   dates:   a dictionary of country versus array of validity dates for class,
  #            such that, classes[country][i] is valid from dates[country][i] 
  #            to dates[country][i+1] or infinity
  #
  def __init__(self, classes, dates):
    self.classes = classes
    self.dates = dates
    self.epoch = datetime.datetime.utcfromtimestamp(0)

  #
  # Gets the class for the given date valid just in the requested moment.
  #
  # parameters:
  #   country: a string with the name of ther country
  #   date:    a string with the date in format yyyy-MM-dd
  #
  # return: the name of the class valid in this moment
  #
  def get_class(self, country, date):
    moment = (datetime.datetime.strptime(\
          date, '%Y-%m-%d')-self.epoch).total_seconds()

    if self.dates.get(country) == None:
      return None

    i = 0
    while i<len(self.dates[country]) and self.dates[country][i] <= moment: 
      i += 1

    if i<0: return None
    else: return self.classes[country][i-1]

    


#
# Return an object with method get_class(country, dateText) that
# gives the class of country according to the dates described in input file.
#
# Format of input file:
#
#   Country,DateFrom,Class
#   (empty lines ignored, heder ignored)
#   (dates in format YYYY-MM-DD)
#
def read_classes(fileName):
  dates = {}
  classes = {}
  epoch = datetime.datetime.utcfromtimestamp(0)

  with open(fileName) as csvClassFile:
    reader = csv.reader(csvClassFile, delimiter=',')
    header = next(reader)
    headerMap = {}
    for i in range(len(header)): headerMap[header[i].lower()] = i

    for row in reader:
      # Careful with empty lines
      if len(row)<3: continue

      # Ignore comments
      if row[0][0] == '#': continue

      country = row[headerMap['location']]
      dateFrom = row[headerMap['datefrom']]
      clazz = row[headerMap['class']]

      if dates.get(country) == None:
        dates[country] = []
        classes[country] = []

      dates[country].append((datetime.datetime.strptime(\
          dateFrom, '%Y-%m-%d')-epoch).total_seconds())
      classes[country].append(clazz)
      
      # Check data is sorted
      if len(classes[country])>1:
        if classes[country][-1] <= classes[country][-2]:
          raise "Dates in " + csvClassFile + " for each country must be sorted"

  return classifier(classes, dates)
      

