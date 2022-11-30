import csv

import os

# Assign variable for file to load and the path


# this is the direct path method
#file_to_load = "Resources/election_results.csv"

#this is the direct file path method to open the file
#election_data = open(file_to_load,"r")

#this is the indirect path method
file_to_load = os.path.join("Resources", "election_results.csv")


#after reading the file, close file

#election_data.close()


#modified versions of lines 29, and 37

#Question: Why don't we need to add , r within the open() function after the _file_to_load variable

with open(file_to_load) as election_data:

    #print file object

    print(election_data)


# create a filename variable to a direct or indirect path to the file

file_to_save = os.path.join("analysis", "election_analysis.txt")

#code below is the open() and close() method for reading/writing data to the file

#open the file with "w" mode to write data to the file
#outfile = open(file_to_save, "w")

#Instead we are going to use the with file open method:
#Also, we acreated a new variable for the opened file. Its called txt_file

with open(file_to_save, "w") as txt_file:

#Write some data to the file

    #txt_file.write("Hello World")

    #write three counties to the file

    # if you want to have a line break between each county, add a newline to the end of each line. "   \n    "

    txt_file.write("Counties in the Election\n-------------------------\n")

    txt_file.write("Arapahoe\nDenver\nJefferson\n")

# Close the file

#outfile.close()

# No need to write close() when we use the code "with open(file_to_save, "w") as txt_file





#YO














