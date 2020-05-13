# -*- coding: utf-8 -*-

# consult documentation https://docs.python.org/3/library/csv.html
import csv
from pprint import pprint

# make dict of all clubs list from given csv file
# returns a dict, mapping club -> list of its members
def load_clubs_data_from(filename):
  result = dict()
  # some info for 2020 spring season
  # must refactor this for flexibility
  col_name = 2
  col_approve = 1
  col_club = 3
  str_approve = "허가"
  # using csv library
  with open(filename, newline='') as csvfile:
    rdr = csv.reader(csvfile)
    for row in rdr:
      approve = row[col_approve]
      str_uid = row[col_name]
      str_club = row[col_club]
      # if approved
      if approve == str_approve:
        if str_club in result.keys():
          # append to existing list
          result[str_club].append(str_uid)
        else:
          # create new key and append
          result[str_club] = [str_uid]
      
  return result

# make list of all student list from clubsdata
# because one student can be in multiple clubs,
# duplicate must be removed
def stud_list_from_clubs_data(clubsdata):
  stud_list = set()
  for clubname, memlist in clubsdata.items():
    #print(clubname, memlist)
    stud_list.update(set(memlist))
  return list(stud_list)

# write a csv of club summary, given clubname and members list,
# automatically decides filename and save to given dire
def write_clubs_csv(clubname, memlist, dir):
  num_member = len(memlist)
  filename = "동아리명_{name}_인원수_{n}.csv".format(name = clubname, n = num_member)
  filepath = "{d}/{fname}".format(d=dir, fname=filename)
  with open(filepath, 'w') as csvfile:
    wtr = csv.writer(csvfile)
    wtr.writerow(["동아리명", clubname])
    for i in range(num_member):
      uid = memlist[i]
      wtr.writerow([i, uid])
    wtr.writerow(["인원수", num_member])

def main():
  clubs_data = load_clubs_data_from("resource/UserRequest-2020-05-11.csv")
  stud_data = stud_list_from_clubs_data(clubs_data)
  pprint("총인원수:{n}".format(n=len(stud_data)))
  for clubname, memlist in clubs_data.items():
    write_clubs_csv(clubname, memlist, "./output")
  

if __name__ == "__main__":
  main()