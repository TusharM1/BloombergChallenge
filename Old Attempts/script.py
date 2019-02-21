#!/usr/bin/env python

import json
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

json_data = json.load(open("SBHSData.json"))

sets = [['area', set()], ['version', set()], ['uptime', set()], ['hostname', set()]]
lists = [['area', []], ['version', []], ['uptime', []], ['hostname', []]]

# Check if there is a way to SELECT areas like an SQL Query instead of this
# Shouldn't need this, there should be a library to get json atributes and cast to set
for element in json_data:
	for item in sets:
		if item[0] in element:
			item[1].add(element[item[0]])
		else:
			item[1].add("")	
	for item in lists:
		if item[0] in element:
			item[1].append(element[item[0]])
		else:
			item[1].append("")	


# for element in json_data:
# 	if 'area' in element:


print("Sets Length", len(sets[0][1]), len(sets[1][1]), len(sets[2][1]), len(sets[3][1]))
print("List Length", len(lists[0][1]), len(lists[1][1]), len(lists[2][1]), len(lists[3][1]))

# objects = tuple(sets[0][1])
# y_pos = np.arange(len(objects))
# performance = [10, 8, 6, 4, 2, 1, 10, 8, 6, 4, 2, 1]
# print(objects)
 
# print(sys.version) 

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.xlabel('Languages')
# plt.ylabel('Usage')
# plt.title('Programming language usage')

# x = lists[2][1], 
y = [x for x in range(0, len(lists[2][1]), 50)]
print(y)

plt.hist(lists[2][1], y, histtype='bar')

plt.show()

# print(sets[0][1])

# plt.plot([1, 2, 3, 4], [1, 4, 3, 16])
# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
# plt.ylabel('Element')

# print(len(area_set), len(version_set), len(uptime_set), len(hostname_set))

# area_set, version_set, uptime_set, hostname_set = ([] for i in range(4))
# lists = [['area', area_set], ['version', version_set], ['uptime', uptime_set], ['hostname', hostname_set]]

# lists = ['area', 'version', 'uptime', 'hostname']

# TODO fix this ugly stuff
# for element in json_data:
# 	if 'area' in element:
# 		area_set.append(element['area'])
# 	else:
# 		area_set.append("")	
# 	if 'version' in element:		
# 		version_set.append(element['version'])
# 	else:
# 		version_set.append("")	
# 	if 'uptime' in element:
# 		uptime_set.append(element['uptime'])
# 	else:
# 		uptime_set.append("")	
# 	if 'hostname' in element:
# 		hostname_set.append(element['hostname'])
# 	else:
# 		hostname_set.append("")	

# area_set, version_set, uptime_set, hostname_set = (set(),) * 4
# area_set = set()
# version_set = set()
# uptime_set = set()
# hostname_set = set()

# element = json_data[0]
# print(element["area"], element["version"], element["uptime"], element["hostname"])
# for x in range(0, size(json_data)):
	# area_set.add(json_data[x]["area"])
	# version_set.add(json_data[x]["version"])
	# uptime_set.add(json_data[x]["uptime"])
	# hostname_set.add(json_data[x]["hostname"])
	# element["area"], element["version"], element["uptime"], element["hostname"]
		# print(element)
# area_set.add(json_data[0::4])
# version_set.add(element['version'])
# uptime_set.add(element['uptime'])
# hostname_set.add(element['hostname'])	