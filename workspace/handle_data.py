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
    #   Fixing user dataframe columns
    user_df.columns = ["track_id", "track_name", "track_artist"]

    return user_df

def create_genre_feature_set(df, float_cols):
  """
  @brief Creates a feature set dataframe for genres by vectorizing them and adds scaled float columns and track_id to the new dataframe.

  @param df           Music dataframe
  @param float_cols   Floating value columns from dataframe

  @return Dataframe with genre features.
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


def generate_playlist_feature_vector(user_df, feature_set_df):
  """
  Generates a playlist feature vector by averaging the vector's features of liked user songs.

  @param user_df        User playlist dataframe 
  @param feature_set_df Feature dataframe 

  @return A playlist feature vector
  """
  # Looks for the user's songs in the playlist
  user_tracks_features = feature_set_df[feature_set_df['track_id'].isin(user_df['track_id'])]
  # Calculates the mean of the values of the song's vectors and stores it as a vector
  playlist_feature_vector = user_tracks_features.drop('track_id', axis=1).mean(axis=0).values

  return playlist_feature_vector



def generate_recommendation(playlist_vector, feature_set_df, df, top_n=15):
  """
  Generates music recommendations based on a playlist vector using cosine similarity.

  @param playlist_vector  Playlist Feature vector with user likeness.
  @param feature_set_df   Feature set dataframe.
  @param df               Spotify dataframe.
  @param top_n            Size of playlist.

  @returns DataFrame containing the top N recommended tracks.
  """

  # Remove track_id from the feature set
  feature_set_without_id = feature_set_df.drop('track_id', axis=1)

  # Calculate cosine similarity between the playlist vector and all tracks in the feature set
  similarity_scores = cosine_similarity(playlist_vector.reshape(1, -1), feature_set_without_id)

  # New dataframe with similarity score for each song
  similarity_df = pd.DataFrame({'track_id': feature_set_df['track_id'], 'similarity': similarity_scores[0]})

  # Sort the DataFrame by similarity score in descending order and recomend the highest score
  sorted_similarity_df = similarity_df.sort_values('similarity', ascending=False)
  top_n_recommendations = sorted_similarity_df.head(top_n)

  # Get metadata from spotify dataset
  recommended_tracks = pd.merge(top_n_recommendations, df, on='track_id', how='left')

  return recommended_tracks


def recommend_playlist_name(playlist_vector, df, top_n=1):
  """
  Recommends a playlist.

  @param  playlist_vector   The playlist feature vector.
  @param  df                DataFrame containing the original track information.
  @param  top_n             Number of playlist names to recommend.

  @return A list of recommended playlist names.
  """
  # Calls for cosine recomendation dataframe
  recommendations_df = generate_recommendation(playlist_vector, feature_set_df, df, top_n)

  # Sort the recomendation
  playlist_counts = recommendations_df.groupby('playlist_name').size().sort_values(ascending=False)

  # Playist recomendation
  return playlist_counts.index.tolist()[:top_n]




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


# Feature set data preparation
float_cols = df.dtypes[df.dtypes == 'float64'].index.values

# Apply the function to create the new dataframe
feature_set_df = create_genre_feature_set(df, float_cols)

