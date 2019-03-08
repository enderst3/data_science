'''
see word doc for all notes.
'''


import numpy as np

# ratings for Lorie, Marty, Tori, and Kurts
movie_ratings = np.array([63.0, 54.0, 70.0, 50.0])

movie_ratings = np.array([[63.0, 54.0, 70.0, 50.0],
                         [94.0, 85.0, 89.0, 95.0],
                         [64.0, 90.0, 73.0, 85.0]])

# makes 5 star ratings
movie_ratings_stars = movie_ratings / 20

# finds the 3rd rating in each list
tori_ratings = movie_ratings[:, 2]
print(tori_ratings)

# finds 2nd rating in each list
marty_ratings = movie_ratings[:, 1]

# finds higher rated movies
print(marty_ratings[marty_ratings > 80])