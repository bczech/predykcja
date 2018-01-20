import pandas as pd
from calculations import Calc

data = pd.read_csv('pedigree10.txt', sep='\t')
data2 = pd.read_csv('dane10.txt', sep='\t')
h2val = 0.64

datasi = Calc().datasire(data, data2)
ranking = Calc().rankingchange(h2val, datasi[0], datasi[1], datasi[2])
pearson = Calc().Pearson(ranking[1], ranking[2])
#plot = Calc().makeplot(ranking[1], ranking[2])

print(pearson)



