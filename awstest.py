import json
import pandas as pd

# crate a list to add dataframes to
awsc_list = list()

# list of files
files_list = ['test.json', 'test2.json']

# read the files
for file in files_list:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    
    # normalize the file and append it to the list of dataframe
    awsc_list.append(pd.json_normalize(data, 'Records', sep='_'))
    
# concat the files into a single dataframe
awsc = pd.concat(awsc_list).reset_index(drop=True)

print(awsc)
