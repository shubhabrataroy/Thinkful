""" make sure you have blaze 0.7.2 in your system. check it by 
import blaze as bz
bz.__version__
if it is not 0.7.2 then update using "condas install blaze" from the terminal
version 0.6.3 does not work well
 """
from blaze import *  # for reading big files
d = Data('account_*.csv')
d = d.distinct() # removes the rows which have duplicates
into('output.csv', d)
