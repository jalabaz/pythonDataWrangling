import pandas as pd

d = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
df = pd.DataFrame(d,columns=['Box','Dimension','Value'])
tidydf = df.pivot(index='Box', columns= 'Dimension', values='Value').reset_index()
tidydf['Volume'] = tidydf['Height']*tidydf['Length']*tidydf['Width']