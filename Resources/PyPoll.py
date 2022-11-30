#import our dependencies

import os
import csv

#create a variable set as the indirect path to the file we want to open to read
file_to_load = os.path.join("Resources", "election_results.csv")


#create a variable set as the indirect path to the file we want to open and write
file_to_save = os.path.join("analysis", "election_analysis.txt")


#open the results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)


    # two lines below will print all of the rows of the csv file

    #for row in file_reader:
    #    print(row)

    # two print the headers and then print the rows, use the two lines of code below

    headers = next(file_reader)

    print(headers)