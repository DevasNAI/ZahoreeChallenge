import pandas as pd


def read_dataset(file_name):
    """
        Retrieves the csv file as a Pandas DataFrame
        returns a Pandas Dataframe
    """
    return pd.read_csv(file_name)

def user_data_full(file_name, df):
    user_df = read_dataset(file_name)

    return pd.merge(user_df, df, "on='track_id", how="left")



df = read_dataset("spotify_songs.csv")
userA = user_data_full("User_A.csv")
userB = user_data_full("User_B.csv")
userJ = user_data_full("User_J.csv")
userO = user_data_full("User_O.csv")






