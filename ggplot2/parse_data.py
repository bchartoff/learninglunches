import csv
import os

def filter_orgs():
  crp = csv.reader(open("source_data.csv","rU"))
  csv_out = csv.writer(open("data_tmp.csv","wb"))
  data = {}
  for row in crp:
    org = (row[0],row[1])
    year = row[3]
    amt = row[2]
    cat = row[4]
    if cat == "B3600":#sample filter, orgs matching "Landscaping & Excavation Svcs" CRP category code
      if org not in data:
        data[org] = {}
      data[org][year] = amt

  for org in data:
    for year in data[org]:
      row = [org[0],org[1],year,data[org][year]]
      csv_out.writerow(row)


def rank_and_reshape():
  cr = csv.reader(open("data_tmp.csv","rU"))
  inflation = csv.reader(open("inflation_2012.csv","rU"))
  cw = csv.writer(open("ggplot_data.csv","wb"))

  cw.writerow(["ultorg","client","year","amt","infl_amt","rank"])

  #build inflation converter
  head = inflation.next()
  infl = {}
  for row in inflation:
    infl[int(row[0])] = float(row[1])

  years = {}
  for year in range (1990,2015):
    years[year] = []

  #build dict of organizations and their lobbying amt
  for row in cr:
    org = (row[0],row[1])
    year = int(row[2])
    amt = float(row[3])

    years[year].append((org,amt))

  #sort by lobbying amt
  for year in years:
    years[year].sort(key=lambda tup: tup[1],reverse=True)

  cr = csv.reader(open("data_tmp.csv","rU"))

  for row in cr:
    org = (row[0],row[1])
    year = int(row[2])
    amt = float(row[3])
    infl_amt = infl[year]*amt #convert to 2012 dollars
    rank = [x[0] for x in years[year]].index(org)+1 #calculate rank, based on sorted list

    row_out = [org[0],org[1],year,amt,infl_amt,rank]
    cw.writerow(row_out)


filter_orgs()
rank_and_reshape()
os.remove("data_tmp.csv")