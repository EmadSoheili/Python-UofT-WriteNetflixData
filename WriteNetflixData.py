
# Write Netflix Data
    # A University of Toronto Project
    # Sep 2022 - Emad Soheili

import os
import csv

csv_path = os.path.join("Resources","netflix_ratings.csv")

movie_name = input("Please enter the movie title: ").lower()
movie_list = []

with open(csv_path) as netflix_data:
    reader = csv.reader(netflix_data)

    hader = next(reader)

    for row in reader:
        if movie_name in str.lower(row[0]):
            if row[0] not in movie_list:
                print(f'Title: {row[0]} - Rating Level: {row[1]} - Rated: {row[5]}')
                movie_list.append(row[0])
if movie_list == []:
    print("The title is not in the list!")


