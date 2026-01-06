dic1 = {'kulcs1':'ertek1' , 'kulcs2' : 'ertek2'}
print(dic1['kulcs1'])
 #print(dic1['kulcs444'])
dic2 = {'k1': 123, 'k2': [12, 23, 45], 'k3': ['alma', 'citrom', 'eper']}
print(dic2['k3'][0].upper())
dic2['k2'].append(55)
print(dic2)
dic3 = {'kulcs_egy':'alma','K2':{'AK1':{'AAK1' : 'citrom'}}}
print(dic3['K2']['AK1']['AAK1'])
print(dic2.keys())
print(dic2.values())
print(dic2.items())
print(dic2.get('k1'))
print(dic3['kulcs_egy'])
dic4 = {}
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
dic2.clear()
print(dic2)
print(get)

