from pathlib import Path
import csv

def profitloss_function():
    """
    - This function will compute the difference in Net Profit if the current day is lower than the previous day
      and write the computed amounts in the summary report.
    - If net profit is higher than previous day between all days, it will be written in the summary report.
    - No parameter is required
    """
    # create a file path to csv file
    file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
    
    # create a file path to summary_report.txt
    fp_summary = Path.cwd()/"summary_report.txt"

    # create empty list to store days and profits
    profit = []
    
    # create two variables store deficit and the order
    order = 0
    deficit = 0    

    # open file in read mode
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file) # Instantiate a reader object
        next(reader) # return the next item from the iterator

        # append days and profit to empty list
        for value in reader:
            profit.append([value[0], value[4]])

        # loop will continue looping if order variable is lesser than the length of profit list
        while order + 1 < len(profit):
            
            # create two variables to store previous and current day values
            previous = int(profit[order][1])
            current = int(profit[order + 1][1])

            # evaluate if previous value is bigger than current value
            if previous > current:
                # If condition is met, the deficit will be calculated and appended in the summary report  
                deficit = previous - current
                with fp_summary.open(mode="a", encoding="UTF-8", newline="") as file:
                    file.write(f"[PROFIT DEFICIT] DAY: {profit[order + 1][0]}, AMOUNT: USD{deficit}\n")
                order += 1 # order will increase by 1 

            else: # If condition is not met, order will increase by 1
                order += 1

        # evaluate if deficit equals to 0 at the end of the loop
        if deficit == 0:
            # If condition is met, open file in append mode and write the computed amount in the summary report
            with fp_summary.open(mode="a", encoding="UTF-8", newline="") as file:
                file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    
    # close the file
    file.close() 