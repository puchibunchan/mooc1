import populartimes
gid="hikonejo" #Google Maps API key 
pid="ChIJw9u_XSsrAmARMIwpeAshKu4" #Place ID Hikone Castle

data=populartimes.get_id(gid, pid)
d1=data['populartimes']

import pandas as pd
df = pd.DataFrame()
col_list=[]
for i in range(len(d1)):
   m = d1[i]
   df[i]=m['data']
   col_list.append(m['name'])

df.columns=col_list
df.to_csv('week.csv')
