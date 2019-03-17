"""
Numpy key points:

- Arrays are a special type of list that allows us to store values in an organized manner.

- An array can be created by either defining it directly using np.array() or by importing a CSV using 
np.genfromtxt('file.csv', delimiter=',').

- An operation (such as addition) can be performed on every element in an array by simply performing 
it on the array itself.

- lements can be selected from arrays using their index and array locations, both of which start at 0.

- Logical operations can be used to create new, more focused arrays out of larger arrays.

"""



# import numpy 
import numpy as np

test_1 = [92, 94, 88, 91, 87]

# turn into numpy list
test_1_np = np.array(test_1)

# create list from CSV
# sample.csv = 34, 9, 89, 34, 71
# turn into numpy list delimiter can be many things.
# test_2 = np.genfromtxt('sample.csv', delimiter=',')

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

# add 2 points to each number in test_3
test_3_fixed = test_3 + 2

# add all lists together
total_grade = test_1 + test_2 + test_3_fixed

# divide total_grade by the number of tests taken
final_grade = total_grade // 3

# print results
print(final_grade)

# select scores for student 4 on test_s
s4_test_2 = test_2[3]

# compare how student2 and student3 did on the first test
s2_s3_test_1 = test_1[1:3]

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

# find certain row and index
print(student_scores[2,1])

# for entire column
print(student_scores[:,0])

# select first 3 elements of first row
print(student_scores[0,0:3])

# student 1 wants to know how she did on her 3rd test
sudent_1_test_3 = student_scores[2,0]

# student 5 wants all test results
student_4_scores = student_scores[:,4]

temp = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

# select temps under 60
cold = temp[(temp <= 60)]
print('cold = ', cold)

# select temps over 80
hot = temp[(temp >= 80)]
print('hot = ', hot)

# find temps between 60 and 80
perfect = temp[(temp > 60) & (temp < 80)]
print('perfect = ', perfect)