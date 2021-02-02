Dic1 = {'2': "Name1", '1': "Name2", '3': "Name3", '6': "Name6", '10': "Name10"}
Dic2 = {'3': 50, '2': 60, '1': 70, '20': 100, '15': 170}

p1 = max(Dic1, key=Dic1.get)
p2 = max(Dic2, key=Dic2.get)
print(p1)
print(p2)