#import our dependencies

import os
import csv

#create a variable set as the indirect path to the file we want to open to read
file_to_load = os.path.join("Resources", "election_results.csv")


#create a variable set as the indirect path to the file we want to open and write
file_to_save = os.path.join("analysis", "election_analysis.txt")


#initialize a total vote counter, empty list of candidates, and an empty dictionary of candidates and their corresponding votes

total_votes = 0

candidate_options = []

candidate_votes= {}

# Track the winning candidate, vote count, and percentage

winning_candidate = ""

winning_count = 0

winning_percentage = 0

#Open the election results and read the file

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row

    headers = next(file_reader)

    #read each row in the CSV file, and add a count to the total_votes count every time a line is read

    for row in file_reader:


        # add 1 to the total vote count for all candidates each time a row of data is read      
             
        total_votes = total_votes + 1

        #obtain the candidate name in column 3 of each row

        candidate_name = row[2]



    # also for each row, if the candidate name is not already in the list candidate_options, append the candidate name to the list

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
        
            #begin tracking that candidate's vote count

            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count

        candidate_votes[candidate_name] += 1

# Save the results to our txt file.

with open(file_to_save, "w") as txt_file:

    #print the final vote count to the terminal.
    
    election_results = (
        
        f'\nElection Results\n'

        f'-------------------------\n'

        f'Total Votes: {total_votes:,}\n'

        f'-------------------------\n')

    print(election_results, end='')

    # After printing final vote count to terminal, write the txt_file with the string in the variable election_results.

    txt_file.write(election_results)

    # In order to print each candidates results, iterate through the dictionary candidate_votes
    # candidate_votes[candidate_name] will acquire the values (votes) of the keys (candidate_name) from the dictionary 
    # so you can use the values in the variables for votes and vote_percentage.

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = 100*(float(votes)/float(total_votes))

        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n') 
    
        print(candidate_results)

        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage
            
            winning_candidate = candidate_name


    #Print the winning candidate's results to the terminal.

    winning_candidate_summary = (

        f'-------------------------\n'

        f'Winner: {winning_candidate}\n'

        f'Winning Vote Count: {winning_count:,}\n'

        f'Winning Percentage: {winning_percentage:.1f}%\n'
        
        f'-------------------------\n'
    )



    print(winning_candidate_summary)

    #Save the winning candidate's results to the text file.

    txt_file.write(winning_candidate_summary)
   



