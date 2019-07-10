# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

a = '0.1'
# Code starts here
d = 0
#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
for i in range(len(data['innings'][0]['1st innings']['deliveries'])):
    delKey = list(data['innings'][0]['1st innings']['deliveries'][i].keys())[0]
    if(data['innings'][0]['1st innings']['deliveries'][i][delKey]['batsman'] == 'SC Ganguly'):
        d = d + 1
    else:
        continue
    #i+=i
print("Ganguly faced " + str(d) + " no of deliveries")
#  Who was man of the match and how many runs did he scored ?
player = list(data['info']['player_of_match'])[0]
print("Man of the match: " , player)
#print(data['info']['player_of_match'])
runs=0
for x in range(len(data['innings'][0]['1st innings']['deliveries'])):
    delKey = list(data['innings'][0]['1st innings']['deliveries'][x].keys())[0]
    if(data['innings'][0]['1st innings']['deliveries'][x][delKey]['batsman'] == 'BB McCullum'):
        runs+=data['innings'][0]['1st innings']['deliveries'][x][delKey]['runs']['batsman']
    else:
        continue
    #i+=i
print( player + " scored " + str(runs) + " runs")
#  Which batsman played in the first inning?
batsman = []
for y in range(len(data['innings'][0]['1st innings']['deliveries'])):
    delKey = list(data['innings'][0]['1st innings']['deliveries'][y].keys())[0]
    if(data['innings'][0]['1st innings']['deliveries'][y][delKey]['batsman'] not in batsman):
        batsman.append(data['innings'][0]['1st innings']['deliveries'][y][delKey]['batsman'])
print(batsman)

# Which batsman had the most no. of sixes in first inning ?
six = []
for c in range(len(data['innings'][0]['1st innings']['deliveries'])):
    delKey = list(data['innings'][0]['1st innings']['deliveries'][c].keys())[0]
    
    if((data['innings'][0]['1st innings']['deliveries'][c][delKey]['runs']['batsman']) == 6):
        six.append(data['innings'][0]['1st innings']['deliveries'][c][delKey]['batsman'])
print("Batsman : " + max(six,key=six.count) + " scored most sixed")

# Find the names of all players that got bowled out in the second innings.
counter = []
for a in range(len(data['innings'][1]['2nd innings']['deliveries'])):
    delKey = list(data['innings'][1]['2nd innings']['deliveries'][a].keys())[0]
    key = 'wicket'
    #print(data['innings'][1]['2nd innings']['deliveries'][a][delKey])
    if(key in data['innings'][1]['2nd innings']['deliveries'][a][delKey]):
        #print(delKey)
        if((data['innings'][1]['2nd innings']['deliveries'][a][delKey]['wicket']['kind']) == 'bowled'):
            counter.append(data['innings'][1]['2nd innings']['deliveries'][a][delKey]['wicket']['player_out'])
    else:
        continue
print(counter)
# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
# Calculate for 1st innings
ext_1inn =0
for x in range(len(data['innings'][0]['1st innings']['deliveries'])):
    delKey = list(data['innings'][0]['1st innings']['deliveries'][x].keys())[0]
    if(data['innings'][0]['1st innings']['deliveries'][x][delKey]['runs']['extras'] > 0):
        ext_1inn+=1
# Calculate for 2nd innings
ext_2inn =0
for x in range(len(data['innings'][1]['2nd innings']['deliveries'])):
    delKey = list(data['innings'][1]['2nd innings']['deliveries'][x].keys())[0]
    if(data['innings'][1]['2nd innings']['deliveries'][x][delKey]['runs']['extras'] > 0):
        ext_2inn+=1
diff = ext_2inn - ext_1inn
print("EXtras in 2nd innings are more by :" + str(diff) + " then 1st innings")

# Code ends here
 



