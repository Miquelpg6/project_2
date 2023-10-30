import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Configuration to set so that all the Seaborn figs come out with this size
sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")



def read_DF(file_path):
    df = pd.read_csv(file_path)
    return df

def merge_df (df_federacio, df_garmin):

    merged_df = df_federacio.merge(df_garmin[['DATE', 'NORMAL HEART RATE']], on='DATE', how='left')

    # Rename the 'FREQUENCIA CARDIACA EN REPOSO' column from df_merged
    merged_df = merged_df.rename(columns={'NORMAL HEART RATE': 'MATCH DAY HEART RATE'})

    # Print the updated DataFrame

    return merged_df


def match_heart_rate (merged_df):

    plt.plot(merged_df["ROUND"] , merged_df['MATCH DAY HEART RATE'], marker='X')

    # Add labels and title
    plt.xlabel("Round")
    plt.ylabel("Heart Rate")
    plt.title("Match Day Heart Rate")

    # Show the plot
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('images/match_day_heart_evolution.png')


def day_hr (df):
   # mitja per dies de la setmana
    sns.boxplot(x="WEEKDAY", y="NORMAL HEART RATE", data=df)
    plt.xlabel('')
    plt.savefig('images/daily_hr.png')


def normal_hr (df_garmin):
    sns.histplot(x=df_garmin["NORMAL HEART RATE"], bins=20)
    plt.xlabel('Normal Heart Rate')
    plt.ylabel('')
    plt.savefig('images/normal_hr_histogram.png')


def matchday_hr (merged_df):
    sns.histplot(x=merged_df["MATCH DAY HEART RATE"], bins=8)
    plt.savefig('images/matchday_hr_histogram.png')


def join_histplots (df_garmin, merged_df):
    # Create a single figure and axis to host the histplots
    fig, ax = plt.subplots()

    # Plot the first histplot on the specified axis
    sns.histplot(x=df_garmin["NORMAL HEART RATE"], bins=20, ax=ax)

    # Plot the second histplot on the same axis
    sns.histplot(x=merged_df["MATCH DAY HEART RATE"], bins=8, color='orange', ax=ax)

    # Add labels for clarity
    ax.set_xlabel("Heart Rate")
    ax.set_ylabel("Frequency")

    plt.savefig('images/normalhr_vs_matchhr.png')


def violin_plot (df_garmin, merged_df):

    # Create a single figure and axis to host the violin plots
    fig, ax = plt.subplots()

    # Plot the first violin plot on the specified axis
    sns.violinplot(x=df_garmin['NORMAL HEART RATE'], ax=ax)
    ax.axvline(x=df_garmin['NORMAL HEART RATE'].median(), c="blue", label="Normal Heart Rate")

    # Plot the second violin plot on the same axis
    sns.violinplot(x=merged_df['MATCH DAY HEART RATE'], ax=ax)
    ax.axvline(x=merged_df['MATCH DAY HEART RATE'].median(), c="red", label="Match Day Heart Rate")

    # Add legends
    plt.legend()

    # Show the plot
    plt.savefig('images/violin_chart.png')





def visualization():
    file_path_1 = "DATA/df_federacio.csv"
    file_path_2 = "DATA/df_garmin.csv"

    df_federacio = read_DF(file_path_1)
    df_garmin = read_DF(file_path_2)
    merged_df = merge_df (df_federacio, df_garmin)
    match_heart_rate(merged_df)
    day_hr (df_garmin)
    normal_hr (df_garmin)
    matchday_hr(merged_df)
    join_histplots(df_garmin, merged_df)
    violin_plot(df_garmin, merged_df)

