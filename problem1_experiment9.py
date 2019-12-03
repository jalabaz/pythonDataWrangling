import pandas as pd

d = {'Student':['Ice Bear', 'Panda', 'Grizzly'],'Math':[89,95,79]}
math = pd.DataFrame(d,columns=['Student','Math'])

d = {'Student':['Ice Bear', 'Panda', 'Grizzly'],'Electronics':[85,81,83]}
electronics = pd.DataFrame(d,columns=['Student','Electronics'])

d = {'Student':['Ice Bear', 'Panda', 'Grizzly'],'GEAS':[90,79,93]}
geas = pd.DataFrame(d,columns=['Student','GEAS'])

d = {'Student':['Ice Bear', 'Panda', 'Grizzly'],'ESAT':[93,89,88]}
esat = pd.DataFrame(d,columns=['Student','ESAT'])

grades = pd.merge(geas,esat, on='Student')
grades = pd.merge(electronics,grades, on='Student')
grades = pd.merge(math,grades, on='Student')

gradesdf = pd.melt(grades,id_vars=['Student'],var_name='Subject',value_name='Grades')