import os

import pandas as pd

the_files = []

the_dataframes = []

output_filename = 'Output/consolidated_output.1.csv'

files = ['Input/data_source_1/sample_data.1.csv', 'Input/data_source_1/sample_data.2.dat', 'Input/data_source_2/sample_data.3.dat']

root_dir = os.path.dirname(__file__)

for f in files:
    filepath = os.path.join(root_dir, f.replace('/', os.sep))
    some_files = os.listdir(os.path.dirname(filepath))
    assert filepath.replace(os.path.dirname(filepath) + os.sep, '') in some_files, 'File does not exist: {}'.format(filepath)
    the_files.append(filepath)
    if (filepath.find('sample_data.2.dat')):
        df = pd.read_csv(filepath, sep='|')
    else:
        df = pd.read_csv(filepath)
    df.insert(0, 'datasource', [os.path.dirname(f) for i in range(len(df))])
    the_dataframes.append(df)
    if (len(the_dataframes) > 1):
        result = pd.concat([the_dataframes[0], df], axis=1, join='inner')
        the_dataframes[0] = result

output_filepath = os.path.join(root_dir, output_filename.replace('/', os.sep))

#print(the_dataframes[0])

the_dataframes[0].to_csv(output_filepath)
    
print(the_files)