import pandas

a = pandas.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
                 columns=['dogs', 'cats'])
print(a.iloc[:,1].name)
a = [['1',5],['1',0],['1',1],['1',2],['1',-7],['1',-4],['1',0],['1',7],['1',6],['1',4]]
a.sort(key=lambda x: x[1])
print(a)
