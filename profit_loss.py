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