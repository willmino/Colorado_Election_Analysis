# path to csv is
# Resources/election_results.csv


#General formula for opening a file
#file_vairable = open(filename,mode)

#mode is a string specifying the mode for reading or writing the file object. The possible modes are:
#"r": Open a file to be read.
#"w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
#"x": Open a file for exclusive creation. If the file does not exist, it will not create one.
#"a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
#"+": Open a file for reading and writing.

#tell computer to find the .csv file in this specific pathway in the directory

import csv

import os



file_to_load = "Resources/election_results.csv"

#set variable election_data to the action of opening the file to be read that is called "file_to_load".
#election_data = open(file_to_load, 'r')





#after reading the file, close file

#election_data.close()


#modified versions of lines 29, and 37

with open(file_to_load) as election_data:

    #To do: perform analysis

    print(election_data)




#YO














