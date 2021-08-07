import plotly.figure_factory as ff
import statistics
import random
import pandas
import plotly.graph_objects as go
import csv
df = pandas.read_csv("data.csv")

mathScores = df["math score"].to_list()
readingScores = df["reading score"].to_list()
writingScores = df["writing score"].to_list()


math_mean = statistics.mean(mathScores)
reading_mean = statistics.mean(readingScores)
writing_mean = statistics.mean(writingScores)
#Median for math and reading
math_median = statistics.median(mathScores)
reading_median = statistics.median(writingScores)
writing_median = statistics.median(writingScores)
#Mode for math and reading
math_mode = statistics.mode(mathScores)
reading_mode = statistics.mode(readingScores)
writing_mode = statistics.mode(writingScores)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("Mean, Median and Mode of reading is {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode))
print("Mean, Median and Mode of writing is {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode))
#Standard deviation for math and reading
math_std_deviation = statistics.stdev(mathScores)
reading_std_deviation = statistics.stdev(readingScores)
writing_std_deviation = statistics.stdev(writingScores)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)
#1, 2 and 3 Standard Deviations for reading
reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation,writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

#Percentage of data within 1, 2 and 3 Standard Deviations for math
math_list_of_data_within_1_std_deviation = [result for result in mathScores if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in mathScores if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in mathScores if result > math_third_std_deviation_start and result < math_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for reading
reading_list_of_data_within_1_std_deviation = [result for result in readingScores if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_within_2_std_deviation = [result for result in readingScores if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_within_3_std_deviation = [result for result in readingScores if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_list_of_data_within_1_std_deviation = [result for result in writingScores if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_within_2_std_deviation = [result for result in writingScores if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_within_3_std_deviation = [result for result in writingScores if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]
#Printing data for math and reading (Standard Deviation)
print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(mathScores)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(mathScores)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(mathScores)))
print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(readingScores)))
print("{}% of data for reading lies within 2 standard deviations".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(readingScores)))
print("{}% of data for reading lies within 3 standard deviations".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(readingScores)))

print("{}% of data for writing lies within 1 standard deviation".format(len(writing_list_of_data_within_1_std_deviation)*100.0/len(writingScores)))
print("{}% of data for writing lies within 2 standard deviations".format(len(writing_list_of_data_within_2_std_deviation)*100.0/len(writingScores)))
print("{}% of data for writing lies within 3 standard deviations".format(len(writing_list_of_data_within_3_std_deviation)*100.0/len(writingScores)))