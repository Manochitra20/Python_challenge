#!/usr/bin/env python
# coding: utf-8

# In[2]:


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


# In[3]:


csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath


# In[4]:


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Defining all variables to be used in the analysis
    total_months=0
    total_revenue =0
    current_budget = 0
    previous_budget = 0
    total_change = 0
    change_count = 0
    change=0
    greatest_increase_revenue = 0
    greatest_decrease_revenue = 0
    #since date is a string variable use ""
    greatest_increase_date = ""
    greatest_decrease_date = ""
    
    for row in csvreader:
        #calculating total_months
        total_months += 1
        #caluclating total revenue
        total_revenue += int(row[1])
        
        #Calculating the change in profits over the whole period
   
        current_budget = int(row[1])
    
        if previous_budget != 0:
            change = current_budget - previous_budget
            total_change += change
            change_count += 1
         
        previous_budget = current_budget
        
       #obtaining the greatest increase and decrease in revenue and the dates when these changes were obeserved
        if change > greatest_increase_revenue:
            greatest_increase_revenue = change
            greatest_increase_date = row[0]
            
        if change < greatest_decrease_revenue:
            greatest_decrease_revenue = change
            greatest_decrease_date = row[0]


# In[5]:


output = (
f"-------------------------------------------------------\n"
f"Financial Analysis\n"
f"-------------------------------------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_revenue:,}\n"
f"Average Change: ${total_change/change_count:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_revenue:,})\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_revenue:,})\n"
f"-------------------------------------------------------\n")


# In[6]:


print(output)


# In[7]:


output_file = os.path.join("..", "PyBank", "analysis.txt")
output_file


# In[8]:


# writing output into the file
with open(output_file, 'w', newline='') as text:  
    text.write(output)


# In[ ]:




