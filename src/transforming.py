import pandas as pd

def read_and_display_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def cleaning_df (df):

    df['jornada'] = df['jornada'].str.replace("'", '')
    df['jornada_date'] = df['jornada'].str.extract(r'(\d{2}-\d{2}-\d{4})')
    df['jornada'] = df['jornada'].str.split(',').str[0]
    df['date'] = pd.to_datetime(df['jornada_date'], format='%d-%m-%Y').dt.strftime('%Y/%m/%d')
    return df

def add_column (df):
    wdl_values = ['L', 'W', 'D', 'W', 'W', 'L', 'L', 'W', 'L', 'L', 'L', 'L', 'W', 'D', 'W', 'W', 'W', 'L', 'D', 'L', 'W', 'W', 'L', 'W', 'L', 'W']
    df['W/D/L'] = wdl_values
    return df

def rename_columns_1(df: pd.DataFrame):
    df = df.rename(columns={'jornada': 'ROUND', 'results': 'RESULTS', 'date': 'DATE'})
    df = df.drop('jornada_date', axis=1)
    #df = df.rename(columns={'date': 'DATE'})
    return df

def save_dataframe_to_csv(df, file_path, index=False):
    df.to_csv(file_path, index=index)

def cleaning_garmin (df):
    #Dropping unwanted columns
    df.drop("Unnamed: 3", axis=1, inplace=True)
    df.drop("Unnamed: 4", axis=1, inplace = True)
    #string into date int
    df["FECHA"] = pd.to_datetime(df["FECHA"], format='%B-%d').dt.strftime('%m/%d')
    #getting rid of the Zeros
    df['2022'] = df['2022'].astype(str).str.rstrip('.0')
    return df

def modifing_garmin (df):
    
    # New column with all date together
    df['Combined_Date'] = df['2022'].astype(str) + '/' + df['FECHA']
    df['Combined_Date'] = df['Combined_Date'].str.replace('/', '-')
    # Convert the 'Date' column to a datetime object
    df['Combined_Date'] = pd.to_datetime(df['Combined_Date'])
    # Create a new column with the day of the week
    df['Day_of_Week'] = df['Combined_Date'].dt.day_name()
    # Convert the 'COMBINED_DATE' column to datetime
    df['Combined_Date'] = pd.to_datetime(df['Combined_Date']).dt.strftime('%Y/%m/%d')
    return df

def rename_columns_2(df):
    df = df.rename(columns={'2022': 'YEAR',
                           'FECHA': 'MONTH/DAY',
                           'FRECUENCIA CARDIACA EN REPOSO': 'NORMAL HEART RATE',
                           'Combined_Date': 'DATE',
                           'Day_of_Week': 'WEEKDAY'})
    return df

def federacion_cleaning():
    df = read_and_display_csv("DATA/federacio_sucio.csv")
    df = cleaning_df (df)
    df = add_column(df)
    df = rename_columns_1(df)
    save_dataframe_to_csv(df, 'DATA/df_federacio.csv', index=False)


def garmin_cleaning ():
    df = read_and_display_csv("DATA/FREQUENCIA_CARDIACA_OK.csv")
    df = cleaning_garmin (df)
    df = modifing_garmin (df)
    df = rename_columns_2 (df)
    save_dataframe_to_csv(df, 'DATA/df_garmin.csv', index=False)