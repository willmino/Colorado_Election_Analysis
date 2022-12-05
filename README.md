# Election_Analysis

## Project Overview

> A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election.
The election audit was carried out by analyzing raw voter data to obtain the following key output values:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate received out of total election votes.
5. Determine the winner of the election based on popular vote.
6. Get a complete list of the counties in Colorado which voted in the election.
7. Calculate the total number of votes per county.
8. Calculate each county's percentage of votes out of the total election votes.
9. Determine the county with the most votes.

> To perform the election anaylsis and satisfy the criteria listed above, I used python to open a .csv file, read through the rows of the data to obtain relevant counts, and perform calculations and an analysis. I then printed the results to a command line, and wrote the results of the analysis to another .txt file.

## Resources

- Data Source: election_results.csv
- Software: Python 3.9.13, Visual Studio code, 1.73.1


## Results
> Before performing any reading and analysis of the file, we needed to import the relevant python dependencies and modules for additional python functions like os file path determination and csv file reading. The code below depicts the importing of the modules.

`import csv`

`import os`
> With some help from the
`os.path.join()` function we could create a file path for the .csv or .txt files we wanted to load or save without knowing the exact file pathway. Once python could tell the computer what path to open, we used the `with` statement to open a file and perform various functions while the file was open. This eliminated the need for a close() function and allowed for less lines of code. When the file was opened, we then use `csv.reader()` to read through the file:

`with open(file_to_load) as election_data:`

&nbsp;&nbsp;&nbsp;&nbsp; `reader = csv.reader(election_data)`

> Reading through every row of the .csv file, one row at a time, was accomplished by using an indented for loop.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `for row in reader:`

> By including indented code within the reader `for` loop, we could pick up relevant bits of data to help us with our calculations and analysis.

* How many votes were cast in this congressional election?

> Since every row of data was a vote in the csv file, for every row of data read, the indented line of code, `total_votes = total_votes + 1`, allowed python to add a `1` to the total vote count. After reading through every row of data in the file, python would yield the exact `total_votes` count. There were 369,711 total votes in this congressional election.

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

> Earlier in the code, we declared an empty list, `county_list`, to hold the names of all the Colorado counties voting in this election. We also declared an empty dictionary ,`county_votes` to hold all of county names as keys with their votes as the corresponding values. Later, using a double indented line of code relative to the `with open(file_to_load)` statement, we created a variable for`county_name` and set it equal to the index position 1 of `row` which represented the second column of data in the .csv file and contained the data for the county names. If county name was not previously detected by the code, the code would add `county_name` to `county_list`. Then, we declared a `county_name` number of keys in the `county_votes` dictionary with values equal to zero. While reading through every row, a single indented line of code added a value of `1` to each county's vote count whenever the name of the county was detected. Final county vote counts were represented by the dictionary `county_votes`. The keys in this dictionary were the county names and the values were the votes per each county. The code is summarized below.

`if county_name not in county_list:`

&nbsp;&nbsp;&nbsp;&nbsp;`county_list.append(county_name)`

&nbsp;&nbsp;&nbsp;&nbsp;`county_votes[county_name] = 0`

`county_votes[county_name] += 1`

> An additional for loop was used to iterate through the `county_votes` dictionary to acquire the values associated with the `county_name` keys in order to perform iterable calculations for the percentage of total votes per county and store them in the `countyvote_percentage` variable. The `for` loop also performed iterable print functions of each county name and each county's percentage of the total vote, and the number of votes for each county. The coding is visualized below.

`for county_name in county_votes:`

&nbsp;&nbsp;&nbsp;&nbsp;`iterated_county_votes = county_votes.get(county_name)`
        
&nbsp;&nbsp;&nbsp;&nbsp;`countyvote_percentage = 100 * (float(iterated_county_votes)/total_votes)`

&nbsp;&nbsp;&nbsp;&nbsp;`county_results = (`

&nbsp;&nbsp;&nbsp;&nbsp;`f'{county_name}: {countyvote_percentage:.1f}% ({iterated_county_votes:,})\n')`

`print(county_results)`

> As mentioned before, there was a total of 369,711 votes. From our new for loop, python told us Jefferson county had 38,855 votes and represented 10.5% of the total votes. The majority of votes came from Denver county at 306,055 votes and 82.8% of the total vote. The minority of the votes came from Arapahoe county at 24,801 votes and represented 6.7% of the total vote.

* Which county had the largest number of votes. 

> To have python tell us which county had the largest number of votes, we first  declared variables in the start of our code to help us with calculations later on. These string and integer variables would eventually represent the name and the vote count for the county with the largest number of votes.

`largest_county_name = ""`

`largest_county_votes = 0`

`largest_county_percentage = 0`

> We could then observe which county had the largest number of votes using another `if` loop nested within the already written line of code, `for county_name in county_votes:`. If each county's vote total, represented by values within the `county_votes` dictionary as `iterated_county_votes`, was greater than the variable `largest_county_votes`, then that county name was set equal to the `largest_county_votes` and thus became the county with the largest number of votes. Python would yield the county with the highest vote count after iterating through all the counties' vote counts. This `if` loop also returned the county with the highest percentage of the total votes.


&nbsp;&nbsp;&nbsp;&nbsp;`if (iterated_county_votes > largest_county_votes) and (countyvote_percentage >`

&nbsp;&nbsp;&nbsp;&nbsp;`largest_county_percentage):`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`largest_county_votes = iterated_county_votes`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`largest_county_name = county_name`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`largest_county_percentage = countyvote_percentage`

> We then created the readout below to allow python to tell us what county had the largest number of votes. This was not nested in the most recent `if` loop, but it was nested within the `with open(file_to_save, "w")` statement.

`largest_county_summary = (`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f'\n-------------------------\n'`
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f'Largest County Turnout: {largest_county_name}\n'`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f'-------------------------\n'`
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`)`

`print(largest_county_summary)`

`txt_file.write(largest_county_summary)`

> By printing the `largest_county_summary` and writing the summary to another file, python told us in the command terminal and [our output file](https://github.com/willmino/Election_Analysis/blob/main/analysis/election_results.txt) that the county with the largest voter turnout was Denver at 306,055 votes.

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

> To calculate the number of votes each candidate received, we started with a `for` loop looking through every row of data for candidate names and their votes. This same `for` loop was used as previously mentioned to calculate each counties' votes and percentage of votes. The only difference for the votes per candidate coding was to create an empty list of candidate names called `candidate_options` and an empty dictionary called `candidate_votes`. As we were looking through every row, if the candidate name (`candidate_name = row[2[]`; the third column of data in the .csv file) was not already in a row, it was added to the list `candidate_options`. Then, whenever a candidate's name was detected, the code line `candidate_votes[candidate_name] += 1` would add a vote to the total vote count. After iterating through all the rows in the .csv file, python yielded a total number of votes per candidate (values) corresponding to each candidate name (keys) in the `candidate_votes` dictionary. The code for obtaining each candidate's vote count is summarized below.

`for row in reader:`

&nbsp;&nbsp;&nbsp;&nbsp;`candidate_name = row[2]`

&nbsp;&nbsp;&nbsp;&nbsp;`if candidate_name not in candidate_options:`
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`candidate_options.append(candidate_name)`
            
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`candidate_votes[candidate_name] = 0`

        
&nbsp;&nbsp;&nbsp;&nbsp;`candidate_votes[candidate_name] += 1`

> Within the below `for` loop, we could then perform an iterable percentage calculation to determine each candidate's percentage of votes out of the total number of votes. We created the `votes` variable so that we could extract each candidate's vote value from the `candidate_votes` dictionary. The `votes` variable was then fed into the `vote_percentage` calculations. We created an f-string `candidate_results` which contained variables for all of the previously mentioned information. Python then performed an iterable print function of `candidate_results` to deliver the final results for each candidate's name, percentage of total votes, and the number of votes each candidate received. The results were achieved using the summarized code below. The resulting information was displayed in the terminal command line and the output file.

`for candidate_name in candidate_votes:`

&nbsp;&nbsp;&nbsp;&nbsp;`votes = candidate_votes.get(candidate_name)`

&nbsp;&nbsp;&nbsp;&nbsp;`vote_percentage = float(votes) / float(total_votes) * 100`

&nbsp;&nbsp;&nbsp;&nbsp;`candidate_results = (`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`)`

&nbsp;&nbsp;&nbsp;&nbsp;`print(candidate_results)`

&nbsp;&nbsp;&nbsp;&nbsp;`txt_file.write(candidate_results)`

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

> Python could tell us which candidate won the election by creating a variable called `winning_candidate_summary`. Within this summary, if any candidates vote and vote percentage were respectively greater than an initial variable `winning_count` and an initial variable `winning_percentage` (which were set to zero at the beginning of the code), then this candidate's name would then be set equal to the `winning_candidate` variable. Python needed to iterate through all of the `candidate_name`'s within the `candidate_votes` dictionary to yield a final winning candidate name. Printing the variable string `winning_candidate_summary` and writing this variable to the output .txt file allowed python to tell us the winning candidate's name and voting metrics for this election.

&nbsp;&nbsp;&nbsp;&nbsp;`if (votes > winning_count) and (vote_percentage > winning_percentage):`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`winning_count = votes`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`winning_candidate = candidate_name`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`winning_percentage = vote_percentage`
 
`winning_candidate_summary = (`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f"-------------------------\n"`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f"Winner: {winning_candidate}\n"`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f"Winning Vote Count: {winning_count:,}\n"`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f"Winning Percentage: {winning_percentage:.1f}%\n"`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`f"-------------------------\n")`

`print(winning_candidate_summary)`

`txt_file.write(winning_candidate_summary)`

> The winning candidate was Diana DeGette. She received 73.8% of the total vote. She received a total of 272,892 votes.

## Summary 
The analysis of the election showed that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anythony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anythony Doane received 3.1% of the vote and 11,606 votes.
- The counties voting in this election were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results were:
    - Jefferson county had 10.5% of the total votes with 38,855 votes.
    - Denver had 82.8% of the total votes with 306,055 votes.
    - Arapahoe had 6.7% of the total votes with 24,801 votes.
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892
    
## Election-Audit Summary
1.  With some modifications, this script can be used for any future elections. By modifying the input file pathway for the `os.path.join()` function, any election whose results are logged into a .csv input file with the same format as the file used in this script example can be used for an audit. Even if the election results information was delivered as a .txt file, we could open the file for read using a similar `with` statemen like the one we used in the code in this analysis. We could then continue to iterate through every line of the code in the same manner as before:

`joinedfilepath = os.path.join("Resources", "election_data.txt")`

`with open(joinedfilepath) as filehandle:`

&nbsp;&nbsp;&nbsp;&nbsp;`reader = filehandle.read()`

&nbsp;&nbsp;&nbsp;&nbsp;`for row in reader:`

2.  This script could also be modified to prevent election fraud by checking the 'Ballot ID' of each vote for repeats. In the same manner as creating an empty list and appending each candidate name to the new list of candidate options when they first appear, the script could be adjusted to have an empty list of ballot id's and then append the ballot id to the list when each one is detected. If the ballot id is already added to the list but appears again in the voting data, then you could have part of the script reject the vote by having python add zero to the total vote count.

`ballot_id_list = []`

`for row in reader` 

&nbsp;&nbsp;&nbsp;&nbsp;`if ballot_id not in ballot_id_list:`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ballot_id_list.append(ballot_id)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`total_votes += 1`

&nbsp;&nbsp;&nbsp;&nbsp;`elseif ballot_id in ballot_id_list:`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `total_votes += 0`
