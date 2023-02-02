from pathlib import Path
import csv

def overheads_function():
    """
    - This function will find the highest overhead category and write the computed amount in the summary report.
    - No parameter is required
    """
    # create a file path to csv file
    file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
    
    # create a file path to summary_report.txt
    fp_summary = Path.cwd()/"summary_report.txt"
    
    # create two variables to store highest overhead value and category
    overhead = 0
    category = ""
    
    # open file in read mode
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file) # Instantiate a reader object
        next(reader) # return the next item from the iterator

        # If value is larger than the current value, it will update the two variables
        for line in reader:
            if float(line[1]) > overhead:
                overhead = float(line[1])
                category = line[0]
    
    # open file in append mode and write the computed amount in the summary report
    with fp_summary.open(mode="a", encoding="UTF-8", newline="") as file:
        file.write(f"[HIGHEST OVERHEADS] {category.upper()}: {overhead}%\n")

    # Close the file
    file.close()