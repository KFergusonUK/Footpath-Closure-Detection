import fnmatch
import os
import csv
count = 0

print("ROAD AND FOOTPATH CLOSURE DETECTION PROGRAM. \nUSE WITH APPLICATIONS AND WORKS EXPORT FROM STREET MANAGER. \nDEVELOPED BY KEVIN FERGUSON. \nKevin.Ferguson@durham.gov.uk \n")
input("PLEASE CONFIRM THE EXPORT FILE IS IN THE SAME FOLDER AS THIS .EXE AND THAT THE FOLDER ONLY CONTAINS THESE TWO FILES. \nPRESS A KEY TO CONTINUE:\n")

try:
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.csv'):
            print("File " + file + " detected in folder. \n")
            print("Processing file...\n\n")
except:
        print("Error in loading file, pleae ensure you place only one .csv file in the folder with this program.")

try:        
    # open upload and check file for reading.
    with open(file, encoding='utf-8', newline='') as smexport:

          filtered = (line.replace('\r', '') for line in smexport)

          for row in csv.reader(filtered):
              # #Column of FP Closure amended to meet DfT changes in Permits Export, removing the COVID column.
              if row[73] == "Yes":
                  count += 1
                  print("*FOOTPATH CLOSURE ON:")
                  print(row[0])
                  print(row[1])
                  print(row[2])
                  print("")
              elif row[27] == "Road closure":
                  count += 1
                  print("ROAD CLOSURE ON: ")
                  print(row[0])
                  print(row[1])
                  print(row[2])
                  print("")
          if count == 0:
              print("No closures detected. \n")
                  
except IndexError as error:
        print("The file in this folder does not contain the expected amount of entires, or is missing, please ensure you have only placed one Street Manager (Applications and Works) export file in this folder.")
except:
        print("Error encountered, please ensure Applications and WOrks csv exists in this folder and re-run. Shutting down.")

input("\nPress a key to exit.")
