"""
A python script to arrange the files from whatsapp backup in a
human-friendly manner.
Pass Directory path as argument while running the script.
"""
from sys import argv
import os

base_addr = argv[1]  # Address where files are to be manipulated.
month_list = (
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct',
    'Nov', 'Dec'
    )
for file in os.listdir(base_addr):
    year = file[4:8]
    month_index = int(file[8:10])
    month = month_list[month_index-1]
    date = file[10:12]

    path = base_addr+'/'+year+'/'+month+'/'+date
    os.makedirs(path, exist_ok=True)
    os.rename(base_addr+'/'+file, path+'/'+file[13:])
