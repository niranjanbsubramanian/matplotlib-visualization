# Line Plot

import pandas as pd
import matplotlib.pyplot as plt

#number of ice creams sold in a week
ice_cream = [35,33,65,44,75,88,101]

plt.plot(ice_cream)
plt.show()


# Scatter Plot

import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
sal = pd.read_csv('/Salary_Data.csv')
sal.head()

#storing the values of experience and sal in a separate variable
experience = sal['YearsExperience']
salary = sal['Salary']

plt.scatter(experience, salary)
plt.show()

# Bar Plot

import pandas as pd
import matplotlib.pyplot as plt

#number of ice creams sold in a week
ice_cream = [35,33,65,44,75,88,101]
days = ['Mon','Tues','Wed','Thur','Fri','Sat','Sun']

plt.bar(days, ice_cream)
plt.show()
