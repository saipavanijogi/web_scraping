import json
with open ('5_task.json','r') as f:
    j=json.load(f)
ra={}
i=0
pav=0
while  i<len(j):
    if j[i]['language']=='English':
        pav=pav+1
        ra['english']=pav
    i=i+1
with open ("6_task.json","w") as f:
    json.dump(ra,f )
        
