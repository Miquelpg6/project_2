# project_2 - Heart Rate and Futsal Matches

Overview
This aim of this project is to get a first database and add information using web scraping in order to make visualizations about both dataset. This project has used a personal database from the heart rate of a wearable (Garmin Watch) for the first database. The second database has been build from the data of the Federació Catalana de Futbol via web scraping. 

Requirements/Libraries Used:
This code was written in Python/Jupyter Notebook, using the following libraries:

Numpy
Pandas
matplotlib.pyplot
Seaborn
Beautiful Soup

Hypotheses/Analysis:

This project has the objective to analyze the Garmin Data and compare this data with the matches days in order to see if the average heart rate is the same between regular days and matches day

FIRST PART - GARMIN DATABASE

The heart rate database  has been downloaded from the app Garmin Connect.
The first part consisted on cleaning the database in order to get a final and clean dataframe:
This has been made through 2 main functions:
    1. Cleaning function: With this function we removed the unwanted columns, and modify the date and year to get it in the way we wanted
    2. Columns function: With this functiont we named the columns with the wanted name in order to match it with the other future database

Once we had the desired information in the way we wanted we created a dataframe and exported into a csv


SECOND PART - MATCH DATABASE

The second part had the aim to get information through web scrapping of the website https://www.fcf.cat/ (Federació Catalana de Futbol).

We wanted to get all the results from las years league, this involved 26 rounds. We also wanted to get the number of the round and the date that the match was played. This is how it was done:

We created a funciton with BeautifulSoup to extract all the results from every round, taking in consideration that we only wanted the result of our team and not the others involved in the same round.

Once we had the list of the results for every Round, we had to extract its date in order to now when was the match played.
For this we created a second function with BeautifulSoup to extract the Round and the date of every match.

Once we had both desired databases we created a dictionary to join them and create a dataframe and export into a csv

THIRD PART - JOIN DATAFRAMES AND VISUALIZATION

Now that we had both dataframes we proceed to import them into a new jupyter notebook (df_garmin and df_federacio). From this point we analyzed diferent things:

    1. We merged the df_federació with the column normal heart rate creating a new column called Match Heart Rate in order to see wich was the heart rate on match days. We displayed thi in a chart to see how was the heart rate in match day

        CHART MATCH HEART RATE

    2. Pie plot for results. We created a pie plot to see the results of the league

        PIE CHART RESULTS

    3. Daily heart rate. With this chart we analyzed which is the average heart rate each every day of the week. We can see that on weekend is where I have the     highest average heart rate. On mondays it appears to be the lowest, this is probably due to the fatigue of the weekend match.

        CHART MITJANES DIES

    4. Histograma heart rate


    5. Violin plot normal heart rate vs match heart rate

    



