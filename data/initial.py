import requests
import numpy as np
import pandas as pd

# List of years and resource ids for the API call
years1 = []
years_resource_ids = {
    2011: '94b499d9-712a-4d2a-b790-7ceec5c9c4b1',
    2012: '382e10d9-1864-40ba-bef6-4eea3c75463c',
    2013: '407c5cd0-f764-4a41-adf8-054ff535049e',
    2014: 'bdae89c8-d4ce-40e9-a6e1-a5203953a2e0',
    2015: 'c9509ab4-6f6d-4b97-979a-0cf2a10c922b',
    2016: 'b7ea6b1b-3ca4-4c5b-9713-6dc1db52379a',
    2017: '30022137-709d-465e-baae-ca155b51927d',
    2018: '2be28d90-3a90-4af1-a3f6-f28c1e25880a',
    2019: 'ea2e4696-4a2d-429c-9807-d02eb92e0222',
    2020: '6ff6a6fd-3141-4440-a880-6f60a37fe789',
    2021: 'f53ebccd-bc61-49f9-83db-625f209c95f5',
    2022: '81a7b022-f8fc-4da5-80e4-b160058ca207',
    2023: 'e6013a93-1321-4f2a-bf91-8d8a02f1e62f',
}

# Function to make the API call
def API_call(years_resource_ids):
    dataframes = []
    
    # Loop through the years and make the API call
    for year, resource_id in years_resource_ids.items():
        URL = f"https://data.boston.gov/api/3/action/datastore_search?resource_id={resource_id}"
        offset = 0
        limit = 100
        year_dataframes = []
        
        # Goes through the pages in the data with offset and limit
        while True:
            params = {
                'offset': offset,
                'limit': limit
            }
            response = requests.get(URL, params=params)
            
            if response.status_code == 200:
                data = response.json()['result']['records']
                if not data:
                    break  # No more data for this year
                df = pd.DataFrame(data)
                year_dataframes.append(df)
                offset += limit
            else:
                print(f"Failed to fetch data for {year}")
                break  # Break the loop on error
        
        # Concatenate all dataframes for the year
        if year_dataframes:
            year_df = pd.concat(year_dataframes, ignore_index=True)
            dataframes.append(year_df)

        print(f"Data for {year} fetched successfully.")
    
    return dataframes


    
dataframes = API_call(years_resource_ids)

# Create the CSV files
for i, df in enumerate(dataframes):
    year = 2011 + i
    df.to_csv(f'../data/{year}.csv', index=False)

print("CSV files created successfully.")

