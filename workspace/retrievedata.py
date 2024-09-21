import pandas as pd


def read_dataset(file_name):
    """
        Retrieves the csv file as a Pandas DataFrame
        returns a Pandas Dataframe
    """
    return pd.read_csv(file_name)

def user_data_full(file_name, df):
    user_df = read_dataset(file_name)
    #   Ids de las canciones que le gustan al usuario
    user_df = user_df.drop(['Song', 'Artist'], axis=1)

    return pd.merge(user_df, df, "on='track_id", how="left")



df = read_dataset("spotify_songs.csv")
userA = user_data_full("User_A.csv")
userB = user_data_full("User_B.csv")
userJ = user_data_full("User_J.csv")
userO = user_data_full("User_O.csv")






# prompt: based on the metadata info of df, create a feature set for the genres to vectorize it and vectorize the whole dataset into a new one in a function

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

def create_genre_feature_set_and_vectorize(df):
  """
  Creates a feature set based on the metadata of the DataFrame for genres, 
  vectorizes the genre information, and vectorizes the entire DataFrame.

  Args:
      df (pd.DataFrame): The input DataFrame containing song metadata.

  Returns:
      tuple: A tuple containing the vectorized DataFrame and the TF-IDF vectorizer.
  """
  # Create a feature set based on metadata for genres
  df['genre_features'] = df.apply(lambda row: ' '.join([str(row['playlist_genre']), 
                                                       str(row['playlist_subgenre'])]), axis=1)

  # Vectorize the genre features using TF-IDF
  vectorizer = TfidfVectorizer()
  tfidf_matrix = vectorizer.fit_transform(df['genre_features'])

  # Create a new DataFrame with the vectorized features
  df_vectorized = pd.DataFrame(tfidf_matrix.toarray(), index=df.index)

  # Add the original DataFrame columns to the vectorized DataFrame
  df_vectorized = pd.concat([df, df_vectorized], axis=1)

  return df_vectorized, vectorizer

# Example usage:
df_vectorized, vectorizer = create_genre_feature_set_and_vectorize(df)
df_vectorized.head()







###############################

import pandas as pd
def generate_playlist_feature_vector(user_df, feature_set_df):
  """
  Generates a playlist feature vector by averaging the feature vectors of the songs in the playlist.

  Args:
    user_df: DataFrame containing the user's liked songs.
    feature_set_df: DataFrame containing the feature vectors for all songs.

  Returns:
    A playlist feature vector as a Pandas Series.
  """
  full_feature_set_playlist = feature_set_df[feature_set_df['track_id'].isin(user_df['track_id'].values)]
  full_feature_set_playlist = feature_set_df.merge(user_df[['track_id']], on='track_id', how='inner')
  full_feature_set_nonplaylist = feature_set_df[~feature_set_df["track_id"].isin(user_df["track_id"].values)]
  
  # Merge user_df and feature_set_df based on 'track_id'
  #merged_df = pd.merge(user_df, feature_set_df, on='track_id', how='inner')

  # Calculate the average of the feature vectors for the playlist
  #playlist_feature_vector = merged_df.drop(['track_id'], axis=1).mean()

  
  #return playlist_feature_vector
  return full_feature_set_nonplaylist
# Generate the playlist feature vector for user_df_A
playlist_feature_vector_A = generate_playlist_feature_vector(user_df_A, feature_set_df)

# Print the playlist feature vector
playlist_feature_vector_A.shape
