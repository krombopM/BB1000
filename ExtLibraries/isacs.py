import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np

data = open('Laurdan_0_va.log', 'r')
line_list = []
temperature_list = []
sum_list = []
for line in data.readlines():
    line_list.append(line)
    if 'Sum of electronic and thermal Enthalpies' in line:
        sum_list.append(line[53:-1] + ' ')
    if 'Temperature' in line:
        temperature_list.append(line[15:23])
#Find smallest value
values = []
for i in range(len(sum_list)):
    value = float(sum_list[i])
    values.append(value)
x = 100
for i in (values):
    if i < x:
        x = i
min_val = x
#Creates list with relative energy
relative = []
relative_float = []
for i in sum_list:
    rel = float(i)
    rel -= min_val
    rel = rel*627.509  #Convert to kcal/mol
    rel = round(rel,4)
    relative_float.append(rel)
    rel = str(rel)
    relative.append(rel)
#Cumulative sum
cumsum = np.cumsum(relative_float)
cumsum.tolist()
for i in range(len(cumsum)):
    cumsum[i] = round(cumsum[i],4)


full_list = [temperature_list, sum_list, relative, cumsum]
full_list = {'temperature': temperature_list, 'Sum Enthalpy': sum_list, 'rH': relative, 'rH_cums': cumsum}
df = pd.DataFrame(full_list, columns=['temperature', 'Sum Enthalpy', 'rH', 'rH_cums'])
df.to_csv('Exercise_3_output', sep=' ')
#Statistics
m = np.average(relative_float)
m = str(m)
std = np.std(relative_float)
std = str(std)
stat = open('statistics','w')
stat.write('The average is ' + m + ' kcal/mol' + '\n')
stat.write('The standard deviation is ' + std + ' kcal/mol')


t_float = []
for i in temperature_list:
    t_float.append(float(i))

print(t_float)
print(cumsum)
plt.plot(t_float,cumsum,'r--')
plt.xticks(np.arange(0, 480, 40))
plt.xlabel('Temperature')
plt.ylabel('kcal/mol')
plt.title('Cumulative relative enthalpies')
plt.savefig('testplot.png')
