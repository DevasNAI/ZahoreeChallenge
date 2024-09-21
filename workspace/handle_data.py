import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt



def read_dataset(file_name):
    """
        Retrieves the csv file as a Pandas DataFrame
        returns a Pandas Dataframe
    """
    return pd.read_csv(file_name)

def user_data_full(file_name, df):
    user_df = read_dataset(file_name)
    #   Ids de las canciones que le gustan al usuario
    user_df.columns = ["track_id", "track_name", "track_artist"]

    return user_df



df = read_dataset("spotify_songs.csv")
userA = user_data_full("User_A.csv", df)
userB = user_data_full("User_B.csv", df)
userJ = user_data_full("User_J.csv", df)
userO = user_data_full("User_O.csv", df)


# Check if there are null values in the data frame
print(df.isnull().sum())
print(df.shape)
# Finds null data
null_mask = df.isnull().any(axis=1)
null_rows = df[null_mask]
null_rows
# Deletes rows where there are null data
df = df.dropna(axis=0, how='any')

print(df.shape)

#-----------------------------------------------

# Create a new column with a list of playlist_genre and playlist_subgenre
df['playlist_genres'] = df.apply(lambda row: [row['playlist_genre'], row['playlist_subgenre']], axis=1)

# Display the DataFrame with the new column
#df.head()


# Feature set data preparation
float_cols = df.dtypes[df.dtypes == 'float64'].index.values


def create_genre_feature_set(df, float_cols):
  """
  Creates a feature set for genres by vectorizing them and adds scaled float columns
  and track_id to the new dataframe.

  Args:
    df: DataFrame containing the music dataset.
    float_cols: Array of column names with float values.

  Returns:
    A new DataFrame with the genre vector, scaled float values, and track_id.
  """

  # Create a TfidfVectorizer for genre features
  vectorizer = TfidfVectorizer()
  tfid_matrix = vectorizer.fit_transform(df["playlist_genres"].apply(lambda x: ' '.join(x)))
  genre_df = pd.DataFrame(tfid_matrix.toarray())
  genre_df.columns = ['genre' + "|" + i for i in vectorizer.get_feature_names_out()]
  genre_df.reset_index(drop = True, inplace=True)

  # Scale float columns
  floats = df[float_cols].reset_index(drop=True)
  scaler = MinMaxScaler()
  scaled_float_df = pd.DataFrame(scaler.fit_transform(floats), columns=float_cols) * 0.2

  # Create a new DataFrame combining genre vectors and scaled float values
  new_df = pd.concat([genre_df, scaled_float_df], axis=1)
  new_df['track_id'] = df['track_id'].values
 # new_df['playlist_id'] = df['playlist_id']

  return new_df

# Apply the function to create the new dataframe
feature_set_df = create_genre_feature_set(df, float_cols)

# Print the head of the new dataframe
feature_set_df.head()




def generate_playlist_feature_vector(user_df, feature_set_df):
  """
  Generates a playlist feature vector by averaging the feature vectors of the user's liked songs.

  Args:
    user_df: DataFrame containing the user's liked songs with a "track_id" column.
    feature_set_df: DataFrame containing the feature vectors for each track.

  Returns:
    A 1D NumPy array representing the playlist feature vector.
  """
  user_tracks_features = feature_set_df[feature_set_df['track_id'].isin(user_df['track_id'])]
  playlist_feature_vector = user_tracks_features.drop('track_id', axis=1).mean(axis=0).values

  return playlist_feature_vector




