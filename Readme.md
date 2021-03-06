# CS586-CensusAnalysis
CS586 - Big Data Analysis Census Data Analysis

## Overview
This project analyzes subsets of the 2010 Census Data set. It was created with the goal of in house processing, 
meaning that this program does not use any API calls.

## Needed Resources
The following is a list of resources needed in order to perform the included analysis:

- 2010 Census Summary File 01 Urban Rural Update - [Link to Dataset](https://www2.census.gov/census_2010/04-Summary_File_1/Urban_Rural_Update/)
- Header Definitions for Summary File (Can be decoded from SAS File) - [Link to File](https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/pl_geohd_2010.sas)
- 2010 Census Summary File 01 Technical Documentation - [Link to File](https://www.census.gov/prod/cen2010/doc/sf1.pdf)
- GeoJSON Counties FIPS File - [Link to File](https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json)
- State FIPS Code to State Name Data - (Copy and Paste the state-level FIPS Code and Place Names) [Link to File](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt#:~:text=FIPS%20codes%20are%20numbers%20which,to%20which%20the%20county%20belongs.)

## Dependencies
The following is a list of dependencies to process and analyze the dataset:

- pandas
- plotly
- pymongo

## Setup
The following needs to be done before any code is ran:

1. The urban dataset needs to be in a folder called Census_Data.
    - Each folder will have a path structure like the following: Census_Data/Alabama
2. Save the GeoJSON Counties FIPS file to Census_Data/geojson-counties-fips.json
3. Create a file called Census_Data/state_fips.csv and copy the State FIPS Code to State Name dataset into it. Replace the spaces in-between code and name with a comma. Also remove leading white spaces. 
3. The Header Definitions SAS file should be stored as a text file named Census_Data/GeoHeaders.txt
    - It should have the following structure: @1 FILEID $6. /\*File Identification*/
    - This will ensure that the geo file in each location folder is read in properly
4. An empty State_JSONs folder should be created for all JSONs to be dumped into.
5. An empty Census_Analysis folder should be created for all the JSONs from the analysis to be dumped into.

## Running the Analysis
The code needs to be ran in the following order. If your data is already in MongoDB you can skip to the __ step:

1. First run unzip_tool.py. This will unzip every folder automatically. Be warned that the entire dataset is over 100GB
2. Next run process_geo_files.py. This will convert the geo files into a pandas readable file. This process is very memory intensive
3. First ensure that a mongo database is created with the name census. Then ensure that the mongo_info.py file contains the correct connection information
5. Then run auto_run.py. This will convert the first three state files into one JSON file for each state. This will take some time to do.
6. Next run the mongo_import.py which will import the JSON data into the Mongo database. This will take some time.
7. Finally run analysis/main.py which will run the given analyses. 
    1. Note: Each analysis will output a dataset file to the Census Analysis folder to use for subsequent rerun instead of querying MongoDB
    
## Diversity Index
Diversity Index (DI) captures the racial and ethnic diversity of the country with a single number. 
The DI expresses the probability that any two individuals chosen at random will have different racial or ethnic backgrounds. (Source: [Link](https://diversity.missouristate.edu/DiversityIndex.htm))

The formulas are as follows:

1. Two individuals with the same racial identity:
    - `Pr(same race) = Pr(Asian)^2 + Pr(Black)^2 + Pr(Indian/Alaskan)^2 + Pr(Other)^2 + Pr(Hawaiian/Pacific)^2 + Pr(Two or More)^2 + Pr(White)^2`
2. Two individuals with different racial identities:
    - `Pr(different race) = 1-Pr(same race)`
    
In the Racial Diversity Calculation, we use the second equation.

## Credits
Created by Kevin Bimonte