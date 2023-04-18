# Creating PyBank code
#importing module os and csv
import os
import csv
txtpath = os.path.join("PyBank","Analysis","text_file.txt")
#Creating a text file to print results
with open(txtpath, "a") as f:
    csvpath = os.path.join("PyBank","Resources","budget_data.csv") 
    #opening file
   
    with open(csvpath, encoding='UTF-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        #skipping first row
        next(csvfile)
        #defining variables
        total_months = 0
        sum_months = 0
        list_months_total = []
        list_of_differences = []
        list_of_months = []
        profit_change=[]
        
        for m in csv_reader:
            months=m[0]
            amounts=m[1]
            #counting total amount of months
            total_months+= 1
            #calculating the total sum for the entire period
            sum_months = sum_months + float(m[1])
            #creating list of all values
            list_months_total.append(amounts)
            #creating list for all dates
            list_of_months.append(months)
        #changing the values list to integers            
        for i in range(0, len(list_months_total)):
            list_months_total[i] = int(list_months_total[i])
        print('Financial Analysis', file = f)
        print('--------------------------------------', file = f)
        print("Total Months: ", total_months, file = f)
        print("Total : $", sum_months, file = f)

        # Calculating difference list
        diff_list = []
        #defining i in values list
        for i in range(1, len(list_months_total)):
            #calculating difference between current date and the next one
            diff_list.append(list_months_total[i] - list_months_total[i-1])
            #calculating minimum profit
            min_profit_change=min(diff_list)
            #calculating maximum profit
            max_profit_change=max(diff_list)
            #finding the correct date throught index match
            max_profit_change_date = str(list_of_months[diff_list.index(max(diff_list))])
            min_profit_change_date = str(list_of_months[diff_list.index(min(diff_list))])
            #calculating average
            average_change = sum(diff_list)/len(diff_list)
            #formatting average to 2 decimals
            format_average = "{:.2f}".format(average_change)
        # printing difference list
        print("Average Change: ", format_average, file = f)
        print("Greatest Increase in Profits:", max_profit_change_date,"($", max_profit_change,")", file = f)
        print("Greatest Decrease in Profits:", min_profit_change_date,"($", min_profit_change,")", file = f)

