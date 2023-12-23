
import requests
import numpy as np
import pandas as pd

resource_id = 'e6013a93-1321-4f2a-bf91-8d8a02f1e62f'

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
        print(f"Failed to fetch data for 2023")
        break  # Break the loop on error

# Concatenate all dataframes for the year
if year_dataframes:
    year_df = pd.concat(year_dataframes, ignore_index=True)


print(f"Data for 2023 fetched successfully.")

# Create the CSV file
year_df.to_csv('./2023.csv', index=False)