"""
numpy statistics
"""

import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

# find average of each array
store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)

print(store_one_avg)
print(store_two_avg)
print(store_three_avg)

best_seller = store_two

print('='*40)

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 
                        1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 
                        1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 
                        1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 
                        1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 
                        1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 
                        2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 
                        1979, 1987])

# save percentage of classes after 2005 as millennials
millennials = np.mean(class_year > 2005)
print(millennials)

print('='*40)

# calculate the value of 2d arrays
allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

# find total mean of array
total_mean = np.mean(allergy_trials)
print(total_mean)

# find the mean of each trial day there are 3 days
# axis=1 means across all rows
trial_mean = np.mean(allergy_trials, axis=1)
print(trial_mean)

# find the average mean of each person in the trial, 5 people
# axis=0 is the columns
patient_mean = np.mean(allergy_trials, axis=0)
print(patient_mean)

print('='*40)

# Outliers

