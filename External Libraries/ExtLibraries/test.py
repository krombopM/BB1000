'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('out_top1000.csv')
#print(df)
births = df.groupby(['year'])['births'].sum().values.tolist()
#print(births)
year = list(set(df.year))
birthsum =[]
for item in births:
    birthsum.append(item)
yearlist = []
for item in year:
    yearlist.append(item)
plt.plot(yearlist,birthsum)
plt.savefig('plot1.png')



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('out_top1000.csv')
donalds = df.loc[df['name'] == 'Donald']
prop = donalds['prop'].values.tolist()
years = donalds['year'].values.tolist()
plt.plot(years,prop)
plt.savefig('donaldplot.png')
'''


from biopandas.pdb import PandasPdb
import numpy as np
ppdb = PandasPdb().fetch_pdb('3IE9')
new_file = open('3IE9.extra_info', 'w')
heatatmdf = ppdb.df['HETATM']

df_other = heatatmdf[['atom_number', 'x_coord', 'y_coord', 'z_coord']].copy()
df_other.columns = ['Atom', 'X', 'Y', 'Z']
df_other['OXYGEN'] = np.nan
for index, row in heatatmdf.iterrows():
    if heatatmdf['atom_name'][index] == 'O':
        df_other['OXYGEN'][index] = True
    else:
        df_other['OXYGEN'][index] = False
df_other.to_csv('3IE9.extra_info', sep='\t')
print(df_other)





#print('PDB Code: %s' % ppdb.code)
#print('PDB Header Line: %s' % ppdb.header)
#print('\nRaw PDB file contents:\n\n%s\n...' % ppdb.pdb_text[:10000])

