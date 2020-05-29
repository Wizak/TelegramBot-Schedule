import json


with open('schedule.json', encoding='utf-8') as f:

	content = json.load(f)

for i in content:
	for k in content[i]:
		print(content[i][k])

input()