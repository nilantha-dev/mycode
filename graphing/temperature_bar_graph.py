#!/usr/bin/python3

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

days = ['sun', 'mon', 'tue', 'wed']
counts = [40, 55, 49, 51 ]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(days, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('temperature on days')
ax.set_title('temperature and color')
ax.legend(title='temperature  color')

plt.savefig("/home/student/mycode/temp.png")
plt.savefig("/home/student/static/temp.png")
