import re  
import pandas as pd
from os.path import join
 
def is_abbrev(abbrev, text):
    pattern = "(|.*\s)".join(abbrev.lower())
    return re.match("^" + pattern, text.lower()) is not None
# "(|.*\s)" makes sure the characters in the abbreviation will only match if they are next to each 
# other, or if the next character appears at the start of a new word    
# The "^" makes sure that the first character of the abbreviation matches the 
# first character of the word, it should be true for most abbreviations.
# https://docs.python.org/2/library/re.html    

# Test
#abbrev = 'QPR'
#text = 'Pueens Park Rangers FC' 
data_path = '/home/sroy/Desktop/Thinkful/Students/Dean'
read_file = pd.read_csv(join(data_path,'royLookUpMaths.csv'))

list_to_lookup = read_file['Team to lookup'].tolist()
complete_list_correct_version = read_file['HomeTeam'].tolist()
