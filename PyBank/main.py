#define dependencies
import os
import csv
#show file directory
pyBankpath = os.path.join('Resources','budget_data.csv')

#create outpot path
pyBankoutput = os.path.join('Analysis', 'PyBankAnalysis.txt')

#set variables for calculations
Total_Months = 0
total_PL = 0
Profit_Loss_Change = 0
Previous_Profit_Loss = 0
Greatest_Increase = 0
Greatest_Decrease = 0

#open file to read
with open(pyBankpath,'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ',')
    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header} ")
    # Read each row of data after the header
    #for row in csvreader:
        #print(row)

    
    #calculate total number of months
    for row in csvreader:
        Total_Months +=1
        total_PL += int(row['Profit/Losses'])

        # calculations for PL
        Profit_Loss_Change = int(row['Profit/Losses']) - Previous_Profit_Loss
        Previous_Profit_Loss = int(row['Profit/Losses'])
        
        #if/else statement gives 9 errors; 
        #resource for writing if statements 
        #https://www.datacamp.com/community/tutorials/elif-statements-python?utm_source=adwords_ppc&utm_campaignid=1565261270&utm_adgroupid=67750485268&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=295208661514&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9011779&gclid=EAIaIQobChMI5Yjp5tCe7gIV0P_jBx0s6Aj4EAAYASAAEgJS0PD_BwE
        if  Profit_Loss_Change > Greatest_Increase:
            Greatest_Increase = Profit_Loss_Change
            Greatest_Month = row['Date']
        elif Profit_Loss_Change < Greatest_Decrease:
            Greatest_Decrease = Profit_Loss_Change
            Least_Month = row['Date']

    #calculate average change use round function        
    averageChange = round((total_PL/Total_Months), 2)

# create output 
output = (
'Financial Analysis \n'
'-------------------------------------------------------------------------- \n'
#use regular quotes for f strings not single quotes
f"Total Months: {Total_Months} \n"
f"Total = ${total_PL} \n"
f"Average Change: ${averageChange} \n"
f"Greatest Increase in Profits: {Greatest_Month}, (${Greatest_Increase}) \n"
f"Greatest Decrease in Profits: {Least_Month}, (${Greatest_Decrease} \n"
)

#print output to text file
print(output)
with open (pyBankoutput, 'w') as txtFile:
    txtFile.write(output)   
