import csv
import json
import os

### change this file path to point to the folder that contains all the jsons
json_path = r"C:\Users\Emily\Documents\Grad School\GIS 5578\GitHub\class-project-ruetz007\Karen_test_Sept2019\Karen_test_Sept2019"

### change this filename to be the desired name of the output csv. It will write into the directory that contains this Python script
csv_out_file = "result.csv"

#if not os.path.exists("csv"): #create a folder to store the csv if one does not already exist
#    os.mkdir("csv")

first = True
f = csv.writer(open(csv_out_file, "w", newline=''))

for filename in os.listdir(json_path):
    #print(filename)
    if filename.endswith(".json"):
        values = []
        headers = []
        json_file_open = open(json_path+"\\"+filename, 'rb')
        data = json_file_open.read().decode('utf-8', errors='ignore')
        #print(data)
        loaded = json.loads(data)
        #print(loaded)
        if first:
            for x in loaded:
                headers.append(x)
            f.writerow(headers)
            first = False
        for key in loaded:
            multiple = []
            if type(loaded[key]) == str:
                values.append(loaded[key])
            elif type(loaded[key]) == list:
                for y in loaded[key]:
                    multiple.append(y)
                values.append("".join(multiple))
            else:
                print("something else")
        f.writerow(values)
    json_file_open.close()
#f.close()