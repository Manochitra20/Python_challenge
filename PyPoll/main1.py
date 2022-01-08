#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


# In[ ]:


csvpath = os.path.join('Resources', 'election_data.csv')
csvpath


# In[ ]:


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Defining variables to start analysing the election results
    
    total_vote =0
    Khan = ""
    Correy = ""
    Li = ""
    OTooley = ""
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0
    
    # Read each row of data after the header
    for row in csvreader:
       
        total_vote += 1
        
        percent_format="{0:.3f}%"
       #adding an if statement to count number of votes each candidate obtained in the election
        if row[2] == "Khan":
            khan_count += 1
            khan_percent = int(khan_count)/int(total_vote) * 100
            khan_percent=percent_format.format(khan_percent)
        
        elif row[2] == "Correy":
            correy_count += 1
            correy_percent = int(correy_count)/int(total_vote) * 100
            correy_percent=percent_format.format(correy_percent)
            
        elif row[2] == "Li":
            li_count += 1
            li_percent = int(li_count)/int(total_vote) * 100
            li_percent=percent_format.format(li_percent)
        else:
            otooley_count += 1
            otooley_percent = int(otooley_count)/int(total_vote) * 100
            otooley_percent=percent_format.format(otooley_percent)
        
        
print (total_vote)
print (khan_count, khan_percent)
print (correy_count, correy_percent)
print (li_count,li_percent )
print (otooley_count,otooley_percent )


# In[ ]:


# Determining variables to find winning vote count, winning percentage, and winning candidate

namepercent_dict={"Khan": khan_percent , "Correy":correy_percent, "Li":li_percent, "OTooley": otooley_percent}
candidate_votes=[khan_count, correy_count, li_count, otooley_count]
candidate_percent=[khan_percent, correy_percent, li_percent, otooley_percent ]
winner_count=0
winner_percent=0
winner_name=""

#Finding the winner(votes, percentage and name) of the election
winner_name=max(namepercent_dict, key=namepercent_dict.get)
winner_percent=max(candidate_percent)
winner_count=max(candidate_votes)


# In[ ]:


print(winner_name)
print(winner_percent)
print(winner_count)


# In[ ]:


election_results=(
f"-----------------------------\n"
f"Election Results\n"
f"-----------------------------\n"
f"Total Votes: {total_vote}\n"
f"-----------------------------\n"
f"Khan: {khan_percent} ({khan_count})\n"
f"Correy: {correy_percent} ({correy_count})\n"
f"Li: {li_percent} ({li_count})\n"
f"O'Tooley: {otooley_percent} ({otooley_count})\n"
f"-----------------------------\n"
f"Winner: {winner_name}\n"
f"-----------------------------\n")


# In[ ]:


print(election_results)


# In[ ]:


results_file = os.path.join("..", "PyPoll", "election_analysis.txt")
results_file


# In[ ]:


# writing output into the file
with open(results_file, 'w', newline='') as text:  
    text.write(election_results)


# In[ ]:




