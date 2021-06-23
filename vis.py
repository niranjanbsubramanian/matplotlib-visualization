# Line Plot
import pandas as pd
import matplotlib.pyplot as plt

#number of ice creams sold in a week
ice_cream = [35,33,65,44,75,88,101]

plt.plot(ice_cream)
plt.show()
#-------------------------------------------------------------#

# Scatter Plot
import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
sal = pd.read_csv('/Salary_Data.csv')

#storing the values of experience and sal in a separate variable
experience = sal['YearsExperience']
salary = sal['Salary']

plt.scatter(experience, salary)
plt.show()
#-------------------------------------------------------------#

# Bar Plot
import pandas as pd
import matplotlib.pyplot as plt

#number of ice creams sold in a week
ice_cream = [35,33,65,44,75,88,101]
days = ['Mon','Tues','Wed','Thur','Fri','Sat','Sun']

plt.bar(days, ice_cream)
plt.show()

#plotting horizontally
plt.barh(days, ice_cream)
plt.show()
#-------------------------------------------------------------#

# Pie Chart
# https://gs.statcounter.com/browser-market-share
x = [64.73,18.43,3.37,3.36,10.11]
labels = ['Chrome', 'Safari', 'Edge', 'Firefox', 'Others']

plt.pie(x, labels=labels,autopct='%.1f%%')
plt.show()

#explode all the slices
x = [64.73,18.43,3.37,3.36,10.11]
labels = ['Chrome', 'Safari', 'Edge', 'Firefox', 'Others']

plt.pie(x, labels=labels,autopct='%.1f%%',explode=[0.1]*5)
plt.show()

#explode a single slice
x = [64.73,18.43,3.37,3.36,10.11]
labels = ['Chrome', 'Safari', 'Edge', 'Firefox', 'Others']

plt.pie(x, labels=labels,autopct='%.1f%%',explode=[0,0.3,0,0,0])
plt.show()
#-------------------------------------------------------------#

#Histogram
import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
sal = pd.read_csv('/Salary_Data.csv')

#storing the values of experience and sal in a separate variable
experience = sal['YearsExperience']
salary = sal['Salary']
plt.hist(salary, bins=7)
plt.show()
#-------------------------------------------------------------#

#BOXPLOT
import pandas as pd
import matplotlib.pyplot as plt

sal = pd.read_csv('/content/Salary_Data.csv')

experience = sal['YearsExperience']
salary = sal['Salary']

plt.boxplot(salary)
plt.show()
#-------------------------------------------------------------#

# Making Plots more readable
#Adding Title, x and y label
import pandas as pd
import matplotlib.pyplot as plt

#number of ice creams sold for the week
ice_cream = [35,33,65,44,75,88,101]

plt.plot(ice_cream)
plt.title('Ice Cream Sales')
plt.xlabel('Day')
plt.ylabel('# ice creams sold')
plt.show()
#-------------------------------------------------------------#

#Adding Legend
import pandas as pd
import matplotlib.pyplot as plt

#number of ice creams sold for the week
ice_cream = [35,33,65,44,75,88,101]

plt.plot(ice_cream, label='No. Of Ice Creams sold')
plt.title('Ice Cream Sales')
plt.xlabel('Day')
plt.ylabel('# ice creams sold')
plt.legend()
plt.show()

#changing the location of legend
plt.plot(ice_cream, label='No. Of Ice Creams sold')
plt.title('Ice Cream Sales')
plt.xlabel('Day')
plt.ylabel('# ice creams sold')
plt.legend(loc='lower right')
plt.show()
#-------------------------------------------------------------#

#rotating xticks
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
plt.plot(days, ice_cream, label='No. Of Ice Creams sold')
plt.title('Ice Cream Sales')
plt.xlabel('Day')
plt.ylabel('# ice creams sold')
plt.legend(loc='lower right')
plt.xticks(rotation='vertical')
plt.show()
#-------------------------------------------------------------#

#Adding Subplots
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('/content/Iris.csv')

plt.subplot(2,2,1)
plt.title('Sepal Length')
plt.hist(iris['SepalLengthCm'])

plt.subplot(2,2,2)
plt.title('Sepal Width')
plt.hist(iris['SepalWidthCm'])

plt.subplot(2,2,3)
plt.title('Petal Length')
plt.hist(iris['PetalLengthCm'])

plt.subplot(2,2,4)
plt.title('Petal Width')
plt.hist(iris['PetalWidthCm'])

# to make the plots spaced out
plt.tight_layout()
plt.show()

#saving the figure
plt.savefig('output')
