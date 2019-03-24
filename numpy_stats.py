"""
numpy statistics

you learned how to use NumPy to analyze single-variable datasets. Here’s what we covered:

Using the np.sort method to locate outliers.
Calculating central positions of a dataset using np.mean and np.median.
Understanding the spread of our data using percentiles and the interquartile range.
Finding the standard deviation of a dataset using np.std.

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
# sorting outliers
temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 
                88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99,
                93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 
                90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 
                87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

# sort temps
sorted_temps = np.sort(temps)
print(sorted_temps)

print('='*40)

# median
large_set = np.array([ 173306.,  102204.,   96767.,   54264.,   40898.,   67887.,  118737.,   74847.,
                        104813.,  122787.,  122577.,  113890.,  100576.,   90345.,   94656.,   71403.,
                        153102., 228233., 85628., 106708., 57289., 42279., 157273., 71691.,
                        77030., 111763., 30770., 69563., 126201., 114726., 78125., 42670.,
                        161304., 74165., 114605., 27270., 3283., 84450., 106449., 89038.,
                        91897., 50975., 133062., 151264., 66383., 90675., 70498., 36092.,
                        160018., 58767., 121995., 63990., 226476., 111729., 127747., 57527.,
                        205382., 117022., 147723., 71284., 119317., 138942., 62945., 121499.,
                        66940., 80725., 47357., 98913., 79435., 92556., 151156., 126723.,
                        65019., 187295., 47038., 40008., 79243., 45334., 142448., 63090.,
                        92153., 251255., 50875., 46395., 76754., 43275., 43150., 57908.,
                        89343., 39451., 43198., 89666., 55168., 41133., 185956., 239637.,
                        63426., 153088., 86450., 195881., 78946., 80067., 69686., 184432.,
                        154515., 115804., 133530., 60730., 44099., 67570., 62957., 140604.,
                        42206., 94150., 86555., 152236., 91549., 105412., 82216., 117358.,
                        161862., 101036., 117315., 104048., 83689., 65307., 71789., 67782.,
                        61844., 71737., 203751., 99121., 44308., 47353., 44960., 82439.,
                        96041., 60345., 189146., 140438., 162413., 94489., 173568., 60460.,
                        154057., 137258., 151520., 77844., 218342., 132205., 60806., 58737.,
                        184590., 95922., 49074., 119246., 126128., 35538., 143795., 59662.,
                        65359., 187713., 128584., 134499., 166816., 105213., 76383., 29964.,
                        73273., 73307., 110846., 80573., 68186., 52601., 27428., 32568.,
                        178872., 111952., 42409., 188881., 132103., 53882., 41144., 60130.,
                        93221., 132447., 143502., 110259., 55159., 44512., 46611., 55662.,
                        142456., 70376., 67326., 53772., 75131., 36100., 121742., 33156.])

large_set_median = np.median(large_set)
print(large_set_median)
print('='*40)

"""
numpy precentiles

Some percentiles have specific names:

The 25th percentile is called the first quartile
The 50th percentile is called the median
The 75th percentile is called the third quartile
The minimum, first quartile, median, third quartile, and maximum of a dataset are called a five-number summary. 
This set of numbers is a great thing to compute when we get a new dataset.
The difference between the first and third quartile is a value called the interquartile range. 
"""
patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

# find the 30th percentile
thirtieth_percentile = np.percentile(patrons, 30)
print(thirtieth_percentile)

# find the 70th percentile
seventieth_percentile = np.percentile(patrons, 70)
print(seventieth_percentile)

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

# find the 25th and 75th percentiles
first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)

# find the interquartile range (75% - 25%)
interquartile_range = third_quarter - first_quarter

print(first_quarter)
print(third_quarter)
print(interquartile_range)
print('='*40)

# Standard Deviation
pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

# get avg pumpkin size
pumpkin_avg = np.mean(pumpkin)
print(pumpkin_avg)

# get ave acorn size
acorn_avg = np.mean(acorn_squash)
print(acorn_avg)

# pumpkin standard deviation
pumpkin_std = np.std(pumpkin)
print(pumpkin_std)

# acorn standard deviation
acorn_squash_std = np.std(acorn_squash)
print(acorn_squash_std)
print('='*40)

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

# find mean of rainfall
rain_mean = np.mean(rainfall)
print(rain_mean)

# find median of rainfall
rain_median = np.median(rainfall)
print(rain_median)

# find 25th and 75th percentiles
first_quarter_rain = np.percentile(rainfall, 25)
third_quarter_rain = np.percentile(rainfall, 75)
print(first_quarter_rain)
print(third_quarter_rain)

# find interquatile range of rainfall
interquartile_range = third_quarter_rain - first_quarter_rain
print(interquartile_range)

# determine standard deviation of the rainfall
rain_std = np.std(rainfall)
print(rain_std)
print('='*40)

calorie_stats = [70., 120., 70., 50., 110., 110., 110., 130., 90., 90., 120., 110.,
                120., 110., 110., 110., 100., 110., 110., 110., 100., 110., 100., 100.,
                110., 110., 100., 120., 120., 110., 100., 110., 100., 110., 120., 120.,
                110., 110., 110., 140., 110., 100., 110., 100., 150., 150., 160., 100.,
                120., 140.,  90., 130., 120., 100.,  50.,  50., 100., 100., 120., 100.,
                90., 110., 110., 80.,  90., 90., 110., 110.,  90., 110., 140., 100.,
                110., 110., 100., 100., 110.]

# find average calories
average_calories = np.mean(calorie_stats)
print(average_calories)

# sort the calorie stats
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# find median of calorie states
median_calories = np.median(calorie_stats)
print(median_calories)

# find lowest percent under 60
print(np.percentile(calorie_stats, 50))
print(np.percentile(calorie_stats, 25))
print(np.percentile(calorie_stats, 12))
print(np.percentile(calorie_stats, 6))
print(np.percentile(calorie_stats, 3))
print(np.percentile(calorie_stats, 4))

nth_percentile = 4
print(nth_percentile)

# what percent are over 60
more_calories = 100 - nth_percentile
print(more_calories)

# calculate standard deviation
calorie_std = np.std(calorie_stats)
print(calorie_std)

