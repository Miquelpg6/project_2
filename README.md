# project_2 - Heart Rate and Futsal Matches

Overview
The aim of this project is to get a primary database and add information using Web Scraping in order to make visualizations about both dataset. 
This project has used a personal database from the Heart Rate of a wearable (Garmin Watch) for the first database. 
The second database has been build from the Federació Catalana de Futbol data via Web Scrapping. 

Requirements/Libraries Used:
This code was written in Python/Jupyter Notebook, using the following libraries:

Numpy
Pandas
Beautiful Soup
matplotlib.pyplot
Seaborn


Hypotheses/Analysis:

This project has the objective to analyze the Garmin Data frame and compare it with the Federacio Data frame, in order to see if the average heart rate is the same between regular days and match days. It has also been useful to make an analysis of my personal heart rate and how it changes over time.

FIRST PART - GARMIN DATABASE

The heart rate database has been downloaded from the app Garmin Connect.
The first part consisted on cleaning the database in order to get a final and clean data frame:

First, I got the dirty Garmin database from Garmin Connect.
I removed the unwanted columns, modified the DATE and YEAR columns. After that, I used another function to rename the columns and have an output where the columns would match to the ones of the second database.
Once I had the desired information in the way I wanted, I export the data frame into a clean CSV named df_garmin.csv


SECOND PART - FEDERACIÓ DATABASE

The second part had the aim to get information through Web Scrapping of the website https://www.fcf.cat/ (Federació Catalana de Futbol).

I wanted to get all my team results from last year's league, this involved 26 rounds. I also wanted to get the number of the round and the date that the match was played. 

Throughout Web Scrapping, I was able to extract all the results from every round, taking in consideration that I only wanted the result of our team (SD ESPANYOL B) and not the other results involved in each round.

Once I had the list of the results for every round, I had to extract the DATE in order to know when the match was played.
I also used BeautifulSoup to extract the Round and the Date of every match. Taking into consideration that had to be our match and not the general weekend, as there are some games played on Saturday and some played on Sunday for every weekend.

Once I had the desired information (matches and rounds) I created a dictionary to join them, create a Data frame and export into a CSV named df_federacio.csv


THIRD PART - JOIN DATA FRAMES AND VISUALIZATION

Now that I had both data frames clean, I proceed to import them into a new notebook (df_garmin and df_federacio). From this point I analyzed different aspects:

1. MATCH DAY HEART RATE: 
    
    I merged the df_federació with the column normal heart rate, creating a new column called Match Heart Rate in order to see which was the heart rate on match days. I displayed this in a chart to see which was the average heart rate in match days. 
    We can see that there isn't a regular heart rate per match day, every match has slightly different heart rates. 
    An interesting conclusion is that in on  match days my heart rate isn't lower than 42 and not higher than 57.
    The empty data points are the matches that I didn't play due to injury.

 ![image](https://github.com/Miquelpg6/project_2/blob/main/images/match_day_heart_evolution.png?raw=true)

 ![image](https://github.com/Miquelpg6/project_2/blob/main/images/matchday_hr_histogram.png?raw=true)



2. DAILY HEART RATE:

    With this chart I wanted to analyze which is the average heart rate per day. 
    We can see that on the weekend is where I have the highest average heart rate. Mondays have the lowest average, this is probably due to the fatigue of the weekends match.

 ![image](https://github.com/Miquelpg6/project_2/blob/main/images/daily_hr.png?raw=true)



3. HISTOGRAM: AVERAGE HEART RATE VS MATCH DAY HEART RATE:

    With this histogram, I wanted to represent the distribution of the average heart rate and compare it with the distribution of the days that I had match. We can see that in normal days the heart rate are wider, going from a minimum of 38 hr/day to a maximum of 78 hr/day. On the other hand, on match days the distribution is narrower, going from a minimum of 42 hr/day to a maximum of 57 hr/day. 

![image](https://github.com/Miquelpg6/project_2/blob/main/images/matchday_hr_histogram.png?raw=true)

 ![image](https://github.com/Miquelpg6/project_2/blob/main/images/normal_hr_histogram.png?raw=true)

 ![image](https://github.com/Miquelpg6/project_2/blob/main/images/normalhr_vs_matchhr.png?raw=true)

4. VIOLIN PLOT: AVERAGE HEART RATE VS MATCH DAY HEART RATE:

    Violin plot normal heart rate vs match heart rate: In this final Violin plot, I represented the difference between the daily heart rate and the match day heart rate. 
    We can see that there is a slight difference of 2 heartbeats between both averages. If in the previous histogram we could see how the distribution is narrower on match days, in this one we can see that the average of match days is higher.
    This can be due to the fact that on match day I can be sometimes more nervous despite being relaxed the whole day.

![image](https://github.com/Miquelpg6/project_2/blob/main/images/violin_chart.png?raw=true)

    
CONCLUSION:

With this project, I have been able to compare two databases and extract interesting insights. With the comparison of the Garmin Database with the Federacio database, I've seen that there is a slight difference between the normal days and the match days on the average heart rate. The analysis has also been useful to analyze the heart rate in the different days of the week for future analysis. 
Having said this, as the data of the match days are reduced, we would have to take into consideration a larger set of data of the following years to see if the 

