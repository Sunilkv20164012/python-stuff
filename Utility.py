

# import asyncio
import requests
from functools import reduce
import re
import pprint
from excelUtils import convertCSVtoXLSX, getInfoXLSX, readXLSX, readColumn, createXLSX, writeXLSX, appendXLSX, readCSV, writeCSV
from jsonparse import JSONParse


def writeFile(content, fileName):
    file1 = open(fileName,"w")
    # file1.write("Hello \n")
    print("Writing to file....... ")
    file1.writelines(content)
    print("Writing complete.")
    file1.close()

def writeJsonFile(content, file_name):
    print("Writing JSON to file....... ")
    with open(fileName, 'w') as f:
        json.dump(data, f)
    print("Writing JSON to file complete.")


def readFile(file_name):
    print("Reading  to file....... ")
    with open(fileName, 'r') as file_handle:
	    file_contents=file_handle.read()
    print("Reading  to file complete ")
    return file_contents
    

def readJsonFile(file_name):
    print("Reading JSON to file....... ")
    return JSONParse(file_name)


writeCSV([['aerthb'], ['aerghjhjhb']], "StyleId", 'Sunil.csv')

convertCSVtoXLSX('Sunil.csv', 'outputdh.xlsx')
getInfoXLSX('outputdh.xlsx')
result = list(readXLSX('outputdh.xlsx'))
print(result)

result2 = list(readCSV('Sunil.csv'))
print(result2)


writeXLSX(['123', '456', '987678', '234523'],'hello.xlsx')

# def main():
    # writeXLSXFile('Sunil.xlsx')
    # loop = asyncio.get_event_loop()
    # futures = [
    #     loop.run_in_executor(
    #         None, 
    #         requests.get, 
    #         'http://example.org/'
    #     )
    #     for i in range(20)
    # ]
    # for response in await asyncio.gather(*futures):
    #     pass

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())



