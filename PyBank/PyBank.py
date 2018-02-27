#import modules
import os
import csv

#file path
budget_data = os.path.join("budget_data_1.csv")
budget_data_2 = os.path.join("budget_data_2.csv")

#Open file
with open(budget_data, "r", newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
with open(budget_data_2, "r", newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
 

    #Creating lists
    date = []
    revenue = []
    revenue_change = []
    
    for row in csvreader:
    
    #Calculating Total Months
        date.append(row[0]) 
      
    #Calculating Total Revenue
        revenue.append(int(row[1]))


 #Calculate Average Change in Revenue 
    for i in range(1, len(revenue)):
        revenue_difference = revenue[i] - revenue[i-1]
        revenue_change.append(revenue_difference)
        average_revenue_change = int(sum(revenue_change) / len(revenue_change))
    
    #Greatest Revenue Increase
    greatest_revenue_increase = int(max(revenue_change))
    increase_index = revenue_change.index(greatest_revenue_increase)
    increase_date = date[increase_index]

    #Greatest Revenue Decrease
    greatest_revenue_decrease = int(min(revenue_change))
    decrease_index = revenue_change.index(greatest_revenue_decrease)
    decrease_date = date[decrease_index]
    
total_months = len(date) 
total_revenue = int(sum(revenue))

    #Print results
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_revenue_change))
print("Greatest Increase in Revenue: " + str(increase_date) + " ($" + str(greatest_revenue_increase)+ ")")
print("Greatest Decrease in Revenue: " + str(decrease_date) + " ($" + str(greatest_revenue_decrease)+ ")")

