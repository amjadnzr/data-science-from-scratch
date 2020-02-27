'''
Data Science from scratch, Chapter 3
'''
from matplotlib import pyplot as plt

#LINE CHART
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# adding a title
plt.title("Nominal GDP")

# adding a label to the y-axis
plt.ylabel("Billions of $")
plt.xlabel("Years")


'''
note: when savefig() was used after show() it just printed an
      empty white background.
'''
#plt.savefig(fname ='./gdp.png')
plt.show()


#BAR CHART
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.title("Best Movies of the year")
plt.ylabel("# of Academy Awards")
plt.xlabel("Movie Names")

'''
name the bars one by one by one along the axis 
use xticks() method on plt which takes the range and the array of names
'''
plt.xticks(range(len(movies)), movies)
plt.show()


# MORE ON BAR CHARTS
from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
print([x + 5 for x in histogram.keys()])
plt.bar([x + 5 for x in histogram.keys()],  # Shift bars right by 5
        histogram.values(),                 # Give each bar its correct height
        10,                                 # Give each bar a width of 10
        edgecolor=(0, 0, 0))                # Black edges for each bar

'''
the plt.axis() method accepts an array of 4 elements
the first two elements denotes the range of x cordinates
the second two elements denote the rang of y cordinates

In plit.bar() the reason for shifting 5 is because when we specify the width as 10
it will gather 5 from right and 5 from left
'''
plt.axis([ 0, 105, 0, 5])                  # x-axis from -5 to 105,
                                           # y-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])    # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
