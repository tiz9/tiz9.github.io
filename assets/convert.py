import csv
import json
import uuid

data = {
  'items': []
}

with open('ref.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='"')
  header = False
  for row in reader:
    if not header:
      data['ids'] = []
      data['fields'] = {}
      for field in row:
        id = str(uuid.uuid4())
        data['ids'].append(id)
        data['fields'][id] = field
      header = True
    else:
      entry = {}
      for i, f in enumerate(data['fields']):
        if row[i] != '':
          entry[data['ids'][i]] = row[i]
      data['items'].append(entry)

print(json.dumps(data))
