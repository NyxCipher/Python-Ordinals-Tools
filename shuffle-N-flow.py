import os, sys
import random
import os.path
import json
import csv

parser = json.JSONDecoder()
parsed = [] 

def check_if_exists(x, ls):
    arr = []
    with open('search.json', 'w') as srch:
        if x in ls:
            print(str(x) + str(ls))
            arr.append(str(x))
        else:
            print('none')
        data=json.dumps(arr)
        srch.write(data)

path = os.getcwd()
xPath="/Users/{path}/mix/"

# Task A
# Randomize *.PNGs & Store Data for JSON
f = open("ins.txt", "a")
f.write(File,new)
i = 1
c_i = str(i)
c_path = str(path)
x_path = str(xPath)
x = 1
for filename in os.listdir( path ):
    x = random.randint(1,4028)
    c_x = str(x)
    filepath = os.path.join(path, filename)
    filepathX = os.path.join(xPath, filename)
    print(filepath)
    
    if filename.endswith(".png"):
        os.rename(filepath, os.path.join(path+'/mix/' + c_x + '.png'))
        f.write(filename+','+c_x+'\n')
    f.close()

# Handle JSON Data
# Task B
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'No' to
			# be the primary key
			key = rows['File']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=2))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'ins.txt'
jsonFilePath = r'ins.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)

with open("ins.json") as csv, open('200.json') as json_file, open('200x.json', 'w') as outp:
    # Json.Load our Data from CSV to JSON from Nex.Py
    data = json.load(csv)
    dataJ = json.load(json_file)
    
    i = 2661
    x = f'{i}'
    # Arrays
    result = []
    print(data)
    for i in range(1,4028):
        appendFileName = data[x]['File']
        print(data[x]['ID'])
        print(data[x]['File'])
        print(dataJ)
        print(dataJ['name'])
        print(dataJ['edition'])
        print(dataJ['image'])
        Properties = dataJ['name']
        result.append({
                'name':['\''+str(appendFileName)+'\''],
                })
        #write.dataJ
        i+=1
        dataJ=json.dumps(result)
        # print(data)
        outp.write(dataJ)
