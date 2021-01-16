#define dependencies
import os
import csv
#show file directory
pyPollpath = os.path.join('Resources','election_data.csv')

#create outpot path
pyPolloutput = os.path.join('Analysis', 'PyPollAnalysis.txt')

#set variables for calculations,set winner as a string
Total_Votes = 0
Candidate = []
Candidate_Votes = {}
Winner = ""
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
    #print(ElectionResults)
    #txtfile.write(ElectionResults)     

    #calculate votes for each candidate
    for candidate in Candidate_Votes:
        Votes = Candidate_Votes.get(Candidate)
        Percentage_Votes = round(((Votes / Total_Votes) *100), 3)
        Candidate_Results = f'{candidate}: {Percentage_Votes}% ({Votes}) \n'
        print (Candidate_Results)
        txtfile.write(CandidateOutput)

        #figure out winner
        if Votes > WinningCount:
           WinningCount = Votes
           Winner = candidate
    

# create output
output = (
    
)
    #show results
with open(pyPollpath, 'w') as txtfile:
    ElectionResults =(
        'Election Results \n'
        '------------------------------- \n'
        f'Total Votes: {Total_Votes} \n'
        '------------------------------- \n'
    Winning_Results = (
        '------------------------------------- \n'
        f'Winner: {Winner} \n'
        '------------------------------------- \n'
    )

    print(Winning_Results)
    txtfile.write(Winning_Results)