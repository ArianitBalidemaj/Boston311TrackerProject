# 311 Team B Project

## About the Project:
The project is an in depth analysis of the Boston 311 dataset. The dataset is a collection of all the service requests that the city of Boston has received from 2011 to 2023.

## What The Team Did:
The team was assigned to explore relationships and answer questions asked by the client, the City of Boston, about the dataset. Each person explored various relationships and addressed all the questions that the client had about the dataset and went even further as to give a more in depth analysis of the dataset for each question. Not only did the team answer the questions, but they also explored the dataset and found other interesting relationships that were not asked by the client. This took the form of extension questions that the we explored and answered to the best of our ability. Exploring the Social Vulnerability Index (SVI) dataset and correlating it with the 311 dataset was one of the extension questions that the team explored. The team also explored the dataset geographically and found interesting relationships between the location of the service requests and the time it took to close the service requests.

## File Structure:
The file structure is as follows:
1. The data folder where the data is stored and the scripts to get the data are stored.
2. The data_notebooks folder where all the notebooks are stored.
3. The base_questions folder where all the base questions are answered in the data_notebooks folder.
4. The extension_questions folder where all the extension questions are answered in the data_notebooks folder.

# Instructions for Running the Project
## Necessary Libraries:

There are some libraries that are needed for this project:
1. Numpy
2. Matplotlib
3. Requests
4. Pandas
5. Scipy
6. Seaborn
7. Plotly
8. Folium
9. Geopandas 

## Start the Project:

To start this project, you must approach these steps to have every preliminary data before you explore the base questions and extension questions:

1. First make sure to git clone this repository onto your local machine. 
2. Change directory to the fa23-team-b directory.
3. Then switch to the git branch for team b which is 
		``` git checkout team-b ```.
4. Next change directory to the data folder and run the “initial.py” file. This will take 2-3 hours so let it run for a while. If you do not feel like waiting you can go to this link [311 Datasets](https://data.boston.gov/dataset/311-service-requests). This is where the downloadable csv files are for the 311 dataset. Ensure that the file names for the csv are their respective years so for example if you were to download the 2011 csv from the website instead of waiting for the script, you then rename the csv to ‘2011.csv’. 
5. Once the script is finished or you downloaded the respective csv files, then run the “total_data_script.py”. This should run for a short period of time and create the “data_total.csv” file. <br>
   
If you need to update the 2023 dataset, you can run the “update_data.py” script. This will take a while to fetch the new data and then rerun the “total_data_script.py” script to update the “data_total2.csv” file.
6. Now change directory to the “fa23-team-b” directory
7. Now you have every single file you need in order to proceed to the analysis 

## Base Questions:

Now that you have everything you need, you can now go ahead and view the base questions in the “base_questions” folder in the “data_notebooks” folder. Make sure to run each cell in order in the respective files.

The following is where each base question is answered in the folder and what files are associated:

1. **Average_daily_contacts.ipynb** : What is the average # of daily contacts by year?
2. **Base_question.ipynb** : Which service requests are most common for the city overall AND by  NEIGHBORHOOD and how is this changing year over year by SUBJECT (department), REASON,QUEUE?
3. **Cases_per_year.ipynb** : What is the total volume of requests per year, or how many 311 requests is the city receiving per year?
4. **Percent_services.ipynb** : What % of service requests are closed (CLOSED_DT or CASE_STATUS) vs. no data (CASE_STATUS = null) vs. unresolved (CASE_STATUS = open)?
5. **Request_types.ipynb** : Volume of top 5 request types (TYPE)  
6. **Resol_time.ipynb** : Average goal resolution time by QUEUE and also Average goal resolution time by QUEUE and neighborhood
7. **Submission_source.ipynb** : How is the case volume changing by submission channel SOURCE?

## Pre-Extension: 

In order to run the extension parts, you must have the SVI dataset and in order to get the SVI dataset you must click the link [SVI Dataset](https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability). The file is a csv file located below in the website for download. Once you have the SVI dataset, you must put it in the “data” folder and rename it to “svi.csv”.

Once that is finished ensure that the SVI metric is there.

## Extension Questions:

You can now move onto the extension questions and run similar to the base questions:

1. **Ext_corr_heatmap_.ipynb** : Correlation using heat maps based on neighborhood and SVI metrics
2. **Extension.ipynb** : Using the SVI dataset to find correlations between neighborhoods and other components.
3. **Geo_Analysis.ipynb** : Analysis of cases based on location and heat maps of cases and time to close based on type of case with interactive maps. 

## End

Now you can freely go through all the notebooks and look at all the analysis portions for each question and correspond it to the Final Report that is on the main directory of "fa23-team-b".

## Error Helps
If you are experiencing error with the reading of the csv files, ensure that you are on the current working directory of fa23-team-b folder and when you need to run a particular notebook, ensure that you are on the current working directory of the notebook you are trying to run.

## Authors:
1. Arianit Balidemaj, Rishi Shah, Mark Maci, Ivanna Morales, and Richard Beuhling