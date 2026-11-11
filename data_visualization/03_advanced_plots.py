import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

x

y

plt.plot(x, y, "r")
plt.xlabel('X Axis Title')
plt.ylabel('Y Axis Title')
plt.title('String Title')
plt.show()

# Empty canvas of 1 by 2 subplots
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x,y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

# Display the figure object

objects = ( 'Python', 'C++', 'JavaScript', 'COBOL', 'Scala', 'Rust', 'Julia', 'C#')
y_pos = np.arange(len(objects))
performance = [14,12,10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.9, color=['black', 'red', 'green', 'blue', 'cyan', 'yellow', 'purple', 'orange'])
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

colums = ["Node", "Occurences"]
data = pd.read_csv('report.csv', sep=' ',names=colums)
data

plt.style.use('ggplot')
data.plot(kind='bar')

import seaborn as sns
sns.set()

sns.displot(data=data, x='Occurences', y='Node')

sns.catplot(data=data, kind='violin', x='Occurences', y='Node')

