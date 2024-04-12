# Predicting-NBA-Awards

This project was a three-step process, ordered as such:
  1. Data Scraping
  2. Data Parsing and Preprocessing
  3. Machine Learning and Analysis

MAKE SURE THE SCRIPTS ARE RAN IN ORDER (A FAILURE TO DO THIS WILL RESULT IN ERRORS)

My project's goal was to see how close I could get to the predictions of this year's NBA awards from statistical data. In NBA award voting history, there has always been subjective bias over how the awards were chosen in addition to the objective stats. 

Understanding this notion, I scraped NBA data from 1997-2023 to gather as many regular and advanced statistics as possible. From there, I parsed this data from HTML files, cleaned the data, and synthesized everything into clean CSV files. From there, I used these CSV files, along with RFEs Random Forest Regression models, to predict the NBA awards for this season. They are not out yet, but going off of recent betting odds for awards, I have gotten relatively close to the actual results.

I will reupload the files on April 15th, 2024, as this is the last day of the NBA season. Only then will all of the statistics and data be up to date.  
A few notes:
- All HTML files came from the step_1:data_scrape.py file.
- To run the step_2:data_parse.ipynb file, you need to have all of the HTML files in the correct directories or folders they are in, such as the player_stats, team_standings, and NBA_awards directories.
- All the CSV files came from the step_2:data_parse.ipynb file.
- To run the step_3:predict_awards.ipynb file, you need to have all the CSV files in the correct directories or folders they are in, such as the CSV_files directory.
- Failure to follow these directions will result in errors in running the program scripts. 
- Make sure libraries are installed if you do not previously have them installed
- It is likely that libraries such as "playwright.sync_api", "bs4", "sklearn.ensemble", "sklearn.metrics", and "sklearn.feature_selection" may not have been previously downloaded




