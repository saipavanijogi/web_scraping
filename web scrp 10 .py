import json
with open ('5_task.json','r') as f:
    j=json.load(f)
ra={"english:2"}
lan={}
i=0
pav=0
swa=0
ch=0
while  i<len(j):
    if j[i]['director']=='madhavan':
        if j[i]['language']=='English':
           pav=pav+1
           ra['english']=pav
    lan['madhavan']=ra
             
    if j[i]['director']=='sundar':
        if j[i]['language']=='engish':
            lan['sundar']=ra
            swa=swa+1
            ra['english']=swa
    lan['sundar']=ra
        
    if j[i]['director']=='mani ratnam':
        if j[i]['language']=='english':
            ch=ch+1
            ra['english']=ch
    lan['mani ratnam']=ra
    i=i+1
    
# with open ("10_task.json","w") as f:
#     json.dump(lan,f,indent=8)
        
print(lan)