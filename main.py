import pandas as pd
import json

with open('meteo_data.json') as f:
    parsed_data = json.load(f)

print(parsed_data)





df = pd.DataFrame.from_dict(parsed_data, orient='columns')

#print(df)
column_names = list(df.columns.values)
#print(column_names)
#print(df['data'])


unique_date = []
for row in df['data']:
    tmp = row.get('date')
    if tmp not in unique_date:
        unique_date.append(row.get('date'))




final_dict =dict.fromkeys(unique_date)


year = ''
sum = 0
q=0
for i,v in enumerate(unique_date):
    if i >0:
        if q == 0:
            final_dict[year] = sum
        else:
            final_dict[year] = sum/q
    sum=0
    year = i
    q= 0
    for row in df['data']:
        if i == row.get('date'):
            global sum
            global q
            sum+=row.get('tC')
            q+=1

print(final_dict)

