import pandas as pd
from Consumer import Consumer
from Appliance import Appliance
from Prosumer import Prosumer

df2 = pd.read_csv('data/data.csv')
df2 = df2.drop(df2.index[14384:], 0)
df2 = df2.drop(df2.index[0:14335], 0)
df2 = df2.reset_index(drop = True)

pv1 = [df2['DE_KN_residential1_pv'][i+1] - df2['DE_KN_residential1_pv'][i] for i in range(24)]
pv2 = [df2['DE_KN_residential1_pv'][i+1] - df2['DE_KN_residential1_pv'][i] for i in range(24,48,1)]

ev1 = [df2['DE_KN_residential4_ev'][i+1] - df2['DE_KN_residential4_ev'][i] for i in range(24)]
ev2 = [df2['DE_KN_residential4_ev'][i+1] - df2['DE_KN_residential4_ev'][i] for i in range(24,48,1)]

df = pd.read_csv('../data/data2.csv')
#print(df)

df_prices = pd.read_csv('../data/prices2.csv')
#print(df_prices)

df_appliances = pd.read_csv('../data/appliances.csv')
print(df_appliances)

# instaciation of appliances :

#for i in range(len(df)):
dic = {}
dic['consumer1'] = Consumer("", "", "")

appliance_P1 = {}
appliance_P2 = {}
appliance_C1 = {}
appliance_C2 = {}
for i in range(len(df_appliances)):
  if df_appliances['P1'][i] == 'yes':
    appliance_P1[df_appliances['appliances'][i]] = Appliance(df_appliances['appliances'][i], 
    df_appliances['starting_time'][i], df_appliances['ending_time'][i], df_appliances['duration_of_operation'][i], 
    df_appliances['power_rating'][i])
  if df_appliances['P2'][i] == 'yes':
    appliance_P2[df_appliances['appliances'][i]] = Appliance(df_appliances['appliances'][i], 
    df_appliances['starting_time'][i], df_appliances['ending_time'][i], df_appliances['duration_of_operation'][i], 
    df_appliances['power_rating'][i])
  if df_appliances['C1'][i] == 'yes':
    appliance_C1[df_appliances['appliances'][i]] = Appliance(df_appliances['appliances'][i], 
    df_appliances['starting_time'][i], df_appliances['ending_time'][i], df_appliances['duration_of_operation'][i], 
    df_appliances['power_rating'][i])
  if df_appliances['C2'][i] == 'yes':
    appliance_C2[df_appliances['appliances'][i]] = Appliance(df_appliances['appliances'][i], 
    df_appliances['starting_time'][i], df_appliances['ending_time'][i], df_appliances['duration_of_operation'][i], 
    df_appliances['power_rating'][i])

prosumer1 = Prosumer(Consumer(appliance_P1, '', '', ev1, pv1))
prosumer2 = Prosumer(Consumer(appliance_P2, '', '', ev2, pv2))
consumer1 = Consumer(appliance_C1, '', '', ev1)
consumer2 = Consumer(appliance_C2, '', '')