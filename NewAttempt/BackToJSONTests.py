import pandas as pd

# global attribute_list, attribute_list_length, lists, sets

sample_data = pd.read_json("SBHSData.json")

# attribute_list = ['area', 'version', 'uptime', 'hostname']
# attribute_list_length = len(attribute_list)

attribute_lists = {'area': [], 'version': [], 'uptime': [], 'hostname': []}
attribute_sets = {'area': set(), 'version': set(), 'uptime': set(), 'hostname': set()}

# lists = [[],] * attribute_list_length
# sets = [set(),] * attribute_list_length

for i in attribute_lists.keys():
	attribute_lists[i] = list(sample_data[i])
	attribute_sets[i] = set(sample_data[i])	

area_counts = sample_data['area'].value_counts()
version_counts = sample_data['version'].value_counts()
version_per_area_counts = {x:dict() for x in attribute_sets['area']}
data_as_list = [sample_data.iloc[x] for x in range(len(attribute_lists['area']))]
for area in version_per_area_counts:
	for entry in range(len(data_as_list)):
		if data_as_list[entry][0] == area:
			if data_as_list[entry][3] in version_per_area_counts[area]:
				version_per_area_counts[area][data_as_list[entry][3]] = version_per_area_counts[area][data_as_list[entry][3]] + 1
			else:
				version_per_area_counts[area][data_as_list[entry][3]] = 0
print(version_per_area_counts)				
# print(version_per_area_counts)				
		# print(entry)
	# for entry in sample_data['area']:
	# 	print(entry)
		# if entry['area'] == area:
		# 	version_per_area_counts[area] = version_per_area_counts[area] + 1
# print(version_per_area_counts)
	# version_counts[area] = sample_data['area']
# print(dict(area_counts))
	# lists[i] = list(sample_data[attribute_list[i]])
	# sets[i] = set(sample_data[attribute_list[i]])

# versions_in_area = {}

# uptime_list, uptime_set = [], set()
# for i in sample_data.uptime:
# 	try: 
# 		uptime_list.append(int(i))
# 		uptime_set.add(int(i))
# 	except:
# 		uptime_list.append(0)

# lists[2] = uptime_list
# sets[2] = uptime_set
