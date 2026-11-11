import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

colums = ["Node", "Occurences"]
data = pd.read_csv('report.csv', sep=' ',names=colums)
plt.show()

