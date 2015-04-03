from os import listdir
from os.path import join
import pandas as pd
import sexmachine.detector as gender

directory = '/home/sroy/Desktop/Thinkful/kauffman_12432156'
data_path = '/home/sroy/Desktop/Thinkful'
files = listdir(directory)
sample_file = join(directory, files[0])
df = pd.read_csv(sample_file)
final_headers = df.columns.tolist()

dfs = pd.DataFrame(columns = final_headers)
for filename in files:
    df1 = dfs.append(pd.read_csv(filename, low_memory=False), ignore_index=True) # you gotta store the append funbction some where in a dataframe. Append is by default volatile
    df2 = df1.drop_duplicates(cols='screen_name', take_last=True) # drop the duplicates and keep the last one
    dfs = df2

list_gender = []
d = gender.Detector()
for j in df1['name']:
    gender = d.get_gender(j)
    list_gender.append(gender)
df1['gender'] =  list_gender # add a new column as a gender in the data frame
# save as a csv
df1.to_csv(join(data_path, 'kauffman_test.csv'),index = True)

