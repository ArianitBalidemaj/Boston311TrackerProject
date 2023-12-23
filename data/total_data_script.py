import numpy as np
import pandas as pd

# List of file names
file_names = ['./2011.csv', './2012.csv', './2013.csv', './2014.csv', './2015.csv', './2016.csv', './2017.csv', './2018.csv', './2019.csv', './2020.csv', './2021.csv', './2022.csv', './2023.csv']
# Read the data from the CSV files into a list of DataFrames to be combined and filter the first row of all of the files except the first one
data_list = []

for file in file_names:
    data = pd.read_csv(file,low_memory=False)
    data_list.append(data)

# Concatenate the DataFrames
data_total = pd.concat(data_list, ignore_index=True)

# Save the concatenated data to a new CSV file
data_total.to_csv('../data/data_total2.csv', index=False)
