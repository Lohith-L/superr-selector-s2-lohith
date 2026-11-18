import json
D='data/'
L=lambda n:json.load(open(D+n))
data=dict(bat=L('bat.json'),bowl=L('bowl.json'),pub=dict(bat=L('published_bat.json'),bowl=L('published_bowl.json')),ev=L('evidence.json'),facts=L('facts.json'),squad=json.load(open('data/squad_fit.json')),robust=json.load(open('data/robustness.json')))
for w in ('bat','bowl'):
    for m in ('random','time'):
        v=data['ev']['validation'][w][m]; data['ev']['validation'][w][m]={k.replace('Our ','My '):x for k,x in v.items()}
for r in ('bat','bowl'):
    for p in data[r]['players']: p.pop('trad',None)
j=json.dumps(data,separators=(',',':')).replace('</','<\\/')
t=open('template.html').read().replace('__DATA__',j)
open('../index.html','w').write(t); print(len(t)//1024,'KB total,',len(open('template.html').read())//1024,'KB template')
