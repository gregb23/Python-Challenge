#define dependencies
import os
import csv
#show file directory
pyPollpath = os.path.join('Resources','election_data.csv')

#create outpot path
pyPolloutput = os.path.join('Analysis','PyPollAnalysis.txt')

#set variables for calculations,set winner as a string
Total_Votes = 0
Candidate = []
Candidate_Votes = {}
Winner = ''
WinningCount = 0


#open file to read
with open(pyPollpath,'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')
    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header} ")
    # Read each row of data after the header
    
    for row in csvreader:
        #calculate total votes
        Total_Votes +=1
        Candidate_Name = row['Candidate']
	    
        #verify all candidates are in list if not add
        if Candidate_Name not in Candidate:
            Candidate.append(Candidate_Name)
            Candidate_Votes[Candidate_Name] = 0

        #add vote to individual candidate
        Candidate_Votes[Candidate_Name] +=1


#print election results
#ith open(pyPolloutput, 'w') as txtfile:
    #Election_Results = (
        #'Election Results \n',
        #'------------------------- \n'
        #f'Total Votes: {Total_Votes} \n'
        #'------------------------- \n'
    #)
    #print(Election_Results)
    #txtfile.write(Election_Results)

    #show vote count per candidate
    for Candidate_Name in Candidate_Votes:
        Votes = Candidate_Votes.get(Candidate_Name)
        Vote_Percentage =round(((Votes / Total_Votes) * 100), 3)
        #Candidate = f"{Candidate}: {Vote_Percentage}% ({Votes}) \n"

        #print(Candidate_Name)
        #txtfile.write(Candidate_Name)
        
        #determine winner
        if Votes > WinningCount:
            WinningCount = Candidate_Votes
            Winner = Candidate_Name

    #print winning data
    #WinningResults = (
        #'-------------------------- \n'
        #f"Winner: {Winner} \n"
        #'-------------------------- \n'
    #)        
    #print(WinningResults)
    #txtfile.write(WinningResults)

#create output
output = (
    'Election Results \n'
    '----------------------------------------------'
    f'Total Votes: {Total_Votes} \n'
    '---------------------------------------------- \n'
    f'{Candidate}: {Vote_Percentage}% ({Votes}) \n'
    '---------------------------------------------- \n'
    f'Winner: {Winner} \n'
    '---------------------------------------------- \n'
)
#print(output)
with open (pyPolloutput, 'w') as txtFile:
    txtFile.write(output)