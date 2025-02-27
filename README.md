# Data Processing Assignment

This repository contains a script for processing cricket player data. The script reads data from CSV and JSON files, merges them, filters the data based on certain conditions, and saves the results to separate output files.

## Example of Data Processing

1. **Read Data:**
   - The script reads data from `testDataSet1.csv` and `testDataSet2.json` input files.

2. **Merge Data:**
   - The data from both files are concatenated into a single DataFrame.

3. **Filter Data:**
   - Players with missing data for runs and wickets are removed.
   - Players with age greater than 50 or less than 15 are excluded.

4. **Save Results:**
   - The filtered data is saved to separate CSV files based on the event type (ODI and TEST).

## Running the Script

Create / update the below paths with the your file/directory paths:
   common_folder = "C:\\Downloads\\assignment\\inputDataSet"
    customer1_folder = "C:\\Downloads\\assignment\\OutPut_Dataset\\Customer1"
    customer2_folder = "C:\\Downloads\\assignment\\OutPut_Dataset\\Customer2"
    temp_folder = "C:\\Downloads\\assignment\\ResultFolder"
    
To run the script, use the following command:

python Data_Processor.py
