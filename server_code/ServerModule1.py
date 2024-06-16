import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import pandas as pd
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.

# -----------------------CREATE SELECTED DATAFRAMES
df_europe = pd.read_csv(data_files['all_predicted_values_55.csv'])
df_belgium = pd.read_csv(data_files['BE_predicted_values_55.csv'])
df_estonia = pd.read_csv(data_files['EE_predicted_values_55.csv'])
df_finland = pd.read_csv(data_files['FI_predicted_values_55.csv'])
df_france = pd.read_csv(data_files['FR_predicted_values_55.csv'])
df_greece = pd.read_csv(data_files['EL_predicted_values_55.csv'])
df_romania = pd.read_csv(data_files['RO_predicted_values_55.csv'])
df_serbia = pd.read_csv(data_files['RS_predicted_values_55.csv'])
df_ukireland = pd.read_csv(data_files['UK_predicted_values_total.csv'])

selected_var = app_tables.selectedvariables_i.search()
variable_dicts = [{'initialrank':r['initialrank'], 'adjustedrank':r['adjustedrank'], 'age':r['age'],'sex':r['sex'],'maritalstatus':r['maritalstatus'], 'employment':r['employment'], 'education':r['education'], 'country':r['country']} for r in selected_var]

df_selectedvariables = pd.DataFrame.from_dict(variable_dicts)
selected_money = app_tables.moneyvalues.search()
money_dicts = [{'housing':r['housing'], 'transport':r['transport'], 'nutrition':r['nutrition'],'clothing':r['clothing'],'laundry':r['laundry'], 'childcare':r['childcare'], 'adultcare':r['adultcare'], 'voluntaryactivity':r['voluntaryactivity']} for r in selected_money]
df_selectedmoney = pd.DataFrame.from_dict(money_dicts)
print(df_selectedvariables)
print(df_selectedmoney)
#---------------------CREATED CSV DATAFRAMES
data_country = df_selectedvariables.at[0,'country']
# print(data_country)
df_monthlytimevalues = None
if data_country == 'Europe (all)': df_monthlytimevalues = df_europe
if data_country == 'Belgium': df_monthlytimevalues = df_belgium
if data_country == 'Estonia': df_monthlytimevalues = df_estonia
if data_country == 'Finland': df_monthlytimevalues = df_finland
if data_country == 'France': df_monthlytimevalues = df_france
if data_country == 'Greece': df_monthlytimevalues = df_greece
if data_country == 'Romania': df_monthlytimevalues = df_romania
if data_country == 'Serbia': df_monthlytimevalues = df_serbia
if data_country == 'United Kingdom of Great Britain and Northern Ireland': df_monthlytimevalues = df_ukireland
# print(df_monthlytimevalues)
#------------------select correct dataframe values
selection_initialrank = df_selectedvariables.at[0,'initialrank']
selection_adjustedrank = df_selectedvariables.at[0,'adjustedrank']
selection_age = df_selectedvariables.at[0,"age"]    
selection_sex = df_selectedvariables.at[0,'sex']
selection_maritalstatus = df_selectedvariables.at[0,"maritalstatus"]
selection_employment = df_selectedvariables.at[0,"employment"]
selection_education = df_selectedvariables.at[0,"education"]

if selection_initialrank == 'Good':
    selection_initialrank = 'good'
if selection_initialrank == 'Poor':
    selection_initialrank = 'bad'
if selection_initialrank == 'Fair':
    selection_initialrank = 'fair'
if selection_adjustedrank == 'Good':
    selection_adjustedrank = 'good'
if selection_adjustedrank == 'Poor':
    selection_adjustedrank = 'bad'
if selection_adjustedrank == 'Fair':
    selection_adjustedrank = 'fair'
if selection_age == '55-64':
    selection_age = '55_64'
if selection_age == '65-74':
    selection_age = '65_74'
if selection_age == '75+':
    selection_age = '75_more'
if selection_sex == 'Male':
    selection_sex = 'male'
if selection_sex == 'Female':
    selection_sex = 'female' 
if selection_maritalstatus == 'Married':
    selection_maritalstatus = 'married'
if selection_maritalstatus == 'Unmarried':
    selection_maritalstatus = 'unmarried'
if selection_maritalstatus == 'Other':
    selection_maritalstatus = 'other'
if selection_employment == 'Part Time':
    selection_employment = 'part_time'
if selection_employment == 'Full Time':
    selection_employment = 'full_time'
if selection_employment == 'Not Paid':
    selection_employment = 'not_paid'
if selection_education == 'Lower Than Secondary':
    selection_education = 'lower_than_secondary'
if selection_education == 'Secondary':
    selection_education = 'secondary_non_tertiary'
if selection_education == 'Tertiary':
    selection_education = 'tertiary'
selection_total = (selection_initialrank,selection_adjustedrank,selection_age,selection_sex,selection_maritalstatus,selection_employment,selection_education)
# print(selection_total)
#----------------------------------
initial_filter_criteria = (df_monthlytimevalues['sph_rec_rel']==selection_initialrank)&(df_monthlytimevalues['age_rec_10y']==selection_age)&(df_monthlytimevalues['sex_rec']==selection_sex)&(df_monthlytimevalues['marital_rec_rel']==selection_maritalstatus)&(df_monthlytimevalues['employment_rec']==selection_employment)&(df_monthlytimevalues['education_rec']==selection_education)
df_initial = df_monthlytimevalues[initial_filter_criteria]
# print(df_initial)

adjusted_filter_criteria = (df_monthlytimevalues['sph_rec_rel']==selection_adjustedrank)&(df_monthlytimevalues['age_rec_10y']==selection_age)&(df_monthlytimevalues['sex_rec']==selection_sex)&(df_monthlytimevalues['marital_rec_rel']==selection_maritalstatus)&(df_monthlytimevalues['employment_rec']==selection_employment)&(df_monthlytimevalues['education_rec']==selection_education)
df_adjusted = df_monthlytimevalues[adjusted_filter_criteria]
# print(df_adjusted)

df_initial.drop(['age_rec_10y','sph_rec_rel','sex_rec','marital_rec_rel','employment_rec','education_rec','COUNTRY'],axis=1,inplace=True)
df_initial.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
df_initial.drop(["a"], axis=1, inplace=True)

df_adjusted.drop(['age_rec_10y','sph_rec_rel','sex_rec','marital_rec_rel','employment_rec','education_rec','COUNTRY'],axis=1,inplace=True)
df_adjusted.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
df_adjusted.drop(["a"], axis=1, inplace=True)

df_initial.rename(columns={"link": "initial_monthlytime"},inplace = True)
df_adjusted.rename(columns={"link": "adjusted_monthlytime"},inplace = True)
# print(df_initial)   
# print(df_adjusted) 

df_combo = pd.merge(df_initial,df_adjusted, on='ACTIVITY')
df_combo.drop(['combination_x','SE_x','combination_y','SE_y'],axis=1,inplace=True)
df_combo.set_index('ACTIVITY',inplace=True)
# print(df_combo)

money_housing = df_selectedmoney.at[0,'housing']
money_housing = float(money_housing)
money_transport = df_selectedmoney.at[0,'transport']
money_transport = float(money_transport)
money_nutrition = df_selectedmoney.at[0,'nutrition']
money_nutrition = float(money_nutrition)
money_clothing = df_selectedmoney.at[0,'clothing']
money_clothing = float(money_clothing)
money_laundry = df_selectedmoney.at[0,'laundry']
money_laundry= float(money_laundry)
money_childcare = df_selectedmoney.at[0,'childcare']
money_childcare = float(money_childcare)
money_adultcare = df_selectedmoney.at[0,'adultcare']
money_adultcare = float(money_adultcare)
money_voluntaryactivity = df_selectedmoney.at[0,'voluntaryactivity']
money_voluntaryactivity = float(money_voluntaryactivity)

hourly_data = [money_housing,money_transport,money_nutrition,money_clothing,money_laundry,money_childcare,money_adultcare,money_voluntaryactivity]

df_hourlymoneyrate = DataFrame(data = hourly_data, columns = ['HourlyMoney'])
df_hourlymoneyrate.index =['Housing','Transport','Nutrition','Clothing','Laundry','ChildCare','AdultCare','Voluntary']
# print(df_hourlymoneyrate)


df_combo['difference_monthlytime'] = (df_combo.adjusted_monthlytime-df_combo.initial_monthlytime)
df_combo['initial_monthlyvalue'] = (df_combo.initial_monthlytime * (df_hourlymoneyrate.HourlyMoney/60))
df_combo['adjusted_monthlyvalue'] = (df_combo.adjusted_monthlytime * (df_hourlymoneyrate.HourlyMoney/60))
df_combo['difference_monthlyvalue'] = df_combo.adjusted_monthlyvalue-df_combo.initial_monthlyvalue
# print(df_combo)

# housing_difference = (df_combo.at['Housing',"adjusted_monthlyvalue"])-(df_combo.at['Housing',"initial_monthlyvalue"])
# transport_difference = (df_combo.at['Transport',"adjusted_monthlyvalue"])-(df_combo.at['Transport',"initial_monthlyvalue"])
# nutrition_difference = (df_combo.at['Nutrition',"adjusted_monthlyvalue"])-(df_combo.at['Nutrition',"initial_monthlyvalue"])
# clothing_difference = (df_combo.at['Clothing',"adjusted_monthlyvalue"])-(df_combo.at['Clothing',"initial_monthlyvalue"])
# laundry_difference = (df_combo.at['Laundry',"adjusted_monthlyvalue"])-(df_combo.at['Laundry',"initial_monthlyvalue"])
# childcare_difference = (df_combo.at['ChildCare',"adjusted_monthlyvalue"])-(df_combo.at['ChildCare',"initial_monthlyvalue"])
# adultcare_difference = (df_combo.at['AdultCare',"adjusted_monthlyvalue"])-(df_combo.at['AdultCare',"initial_monthlyvalue"])
# voluntary_difference = (df_combo.at['Voluntary',"adjusted_monthlyvalue"])-(df_combo.at['Voluntary',"initial_monthlyvalue"])

# list_difference = [housing_difference,transport_difference,nutrition_difference,clothing_difference,laundry_difference,childcare_difference,adultcare_difference,voluntary_difference]

# df_difference = DataFrame(data = list_difference, columns = ['difference_monthlyvalue'])
# df_difference.index =['Housing','Transport','Nutrition','Clothing','Laundry','ChildCare','AdultCare','Voluntary']
# df_final_raw= pd.merge(df_combo,df_difference, left_index=True, right_index=True)


df_final = df_combo.apply(lambda column: column.astype(int))
df_final[df_final < 0] = 0

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df_final)
# print(df_final.dtypes)

total_initial_time = df_final['initial_monthlytime'].sum()
total_adjusted_time = df_final['adjusted_monthlytime'].sum()
total_difference_time = df_final['difference_monthlytime'].sum()
total_initial_value = (df_final['initial_monthlyvalue'].sum())*12
total_adjusted_value = (df_final['adjusted_monthlyvalue'].sum())*12
total_difference_value = (df_final['difference_monthlyvalue'].sum())*12

totals = (total_initial_time,total_adjusted_time,total_difference_time,total_initial_value,total_adjusted_value,total_difference_value)

df_totals = DataFrame(data = totals, columns = ['HourlyValue'])
df_totals.index=['total_initial_time','total_adjusted_time','total_difference_time','total_initial_value','total_adjusted_value','total_difference_value']
# print(df_totals)


total_initial_time_diff = 43800 - (total_initial_time)
total_adjusted_time_diff = 43800 - (total_adjusted_time)
total_difference_time_diff = 43800 - (total_difference_time)
total_time_diff = {'Non-Market Productive Activities':[total_initial_time,total_adjusted_time,total_difference_time],'All Other Activities':[total_initial_time_diff,total_adjusted_time_diff,total_difference_time_diff]}
df_total_diff = pd.DataFrame(data=total_time_diff)
df_total_diff.index = ['initial_times','adjusted_times','difference_times']
df_total_diff_trans = df_total_diff.T
# print(df_total_diff_trans)

#display(df_final)
#----------------------------------------------------------------------------------------------------------------------------------------------------
df_pop = pd.read_csv(data_files['pop_total.csv'])
print(df_pop)

popselected_var = app_tables.pop_info.search()
pop_variable_dicts = [
    {'pop_country': r['pop_country'], 'pop_name': r['pop_name'], 'pop_age': r['pop_age'], 'pop_initial': r['pop_initial'], 'pop_percent': r['pop_percent'], 'pop_percentsuccess': r['pop_percentsuccess'], 'pop_adjusted': r['pop_adjusted']}
    for r in popselected_var
]
df_popselectedvar = pd.DataFrame.from_dict(pop_variable_dicts)
df_popselectedvar['pop_initial'] = df_popselectedvar['pop_initial'].replace('Good','good').replace('Fair','fair').replace('Poor','bad')
df_popselectedvar['pop_adjusted'] = df_popselectedvar['pop_adjusted'].replace('Good','good').replace('Fair','fair').replace('Bad','bad')
df_popselectedvar['pop_country'] = df_popselectedvar['pop_country'].replace('Belgium','BE').replace('Estonia','EE').replace('Finland','FI').replace('France','FR').replace('Greece','EL').replace('Romania','RO').replace('Serbia','RS')
df_popselectedvar['pop_age'] = df_popselectedvar['pop_age'].replace('55-64','55_64').replace('65-74','65_74').replace('75+','75_more')

print(df_popselectedvar)

pop_selected_money = app_tables.moneyvalues.search()
popmoney_dicts = [
    {'Housing': r['housing'], 'Transport': r['transport'], 'Nutrition': r['nutrition'], 'Clothing': r['clothing'], 'Laundry': r['laundry'], 'ChildCare': r['childcare'], 'AdultCare': r['adultcare'], 'Voluntary': r['voluntaryactivity']}
    for r in pop_selected_money
    ]
df_popselectedmoney = pd.DataFrame.from_dict(popmoney_dicts)
df_popselectedmoney = df_popselectedmoney.apply(pd.to_numeric, errors='coerce') / 60
df_popselectedmoney = df_popselectedmoney.transpose()
df_popselectedmoney.columns = ['hourly_value']
print(df_popselectedmoney)
pop_country = df_popselectedvar['pop_country'].iloc[0]
print(pop_country)
pop_age = df_popselectedvar['pop_age'].iloc[0]
print(pop_age)
pop_initial = df_popselectedvar['pop_initial'].iloc[0]
print(pop_initial)
pop_adjusted = df_popselectedvar['pop_adjusted'].iloc[0]
print(pop_adjusted)
pop_percent = df_popselectedvar['pop_percent'].iloc[0]
print(pop_percent)
pop_percentsuccess = df_popselectedvar['pop_percentsuccess'].iloc[0]
print(pop_percentsuccess)

df_pop_initial = df_pop[(df_pop['country'] == pop_country) & (df_pop['age_group'] == pop_age) & (df_pop['group_col'] == pop_initial)]
df_pop_initial = df_pop_initial.drop(['group_col'], axis=1).rename(columns={"predicted": "initial"}).set_index('activity')
df_pop_initial = df_pop_initial.reindex(["Housing",'Transport','Nutrition','Clothing','Laundry','ChildCare','AdultCare',"Voluntary"])
print(df_pop_initial)

df_pop_adjusted = df_pop[(df_pop['country'] == pop_country) & (df_pop['age_group'] == pop_age) & (df_pop['group_col'] == pop_adjusted)]
df_pop_adjusted = df_pop_adjusted.drop(['group_col', 'country', 'age_group'], axis=1).rename(columns={"predicted": "adjusted"}).set_index('activity')
df_pop_adjusted = df_pop_adjusted.reindex(["Housing",'Transport','Nutrition','Clothing','Laundry','ChildCare','AdultCare',"Voluntary"])
print(df_pop_adjusted)

df_pop_total = pd.merge(df_pop_initial, df_pop_adjusted, left_index=True, right_index=True)
df_pop_total['adjusted_value'] = df_pop_total['adjusted'] * df_popselectedmoney['hourly_value']
df_pop_total['initial_value'] = df_pop_total['initial'] * df_popselectedmoney['hourly_value']
df_pop_total['difference'] = df_pop_total['adjusted'] - df_pop_total['initial']
print(df_pop_total)


data = {
    'country': ['BE', 'EE', 'FI', 'FR', 'EL', 'RO', 'RS'],
    '55_64': [1427000, 187000, 743000, 8015000, 1342000, 2678000, 1146000],
    '65_74': [1038000, 128000, 629000, 6162000, 1101000, 1817000, 832000],
    '75+': [1011000, 119000, 478000, 6028000, 1147000, 1533000, 616000]
}

# Create a DataFrame
df_pop_country_num = pd.DataFrame(data)

def get_population(country, age_group):
    # Dictionary to map age group labels to DataFrame column names
    age_group_mapping = {
        '55_64': '55_64',
        '65_74': '65_74',
        '75+': '75+'
    }
    
    # Validate inputs
    if country not in df_pop_country_num['country'].values:
        return f"Error: Country '{country}' not found."
    if age_group not in age_group_mapping:
        return f"Error: Age group '{age_group}' not found."
    
    # Get the population value
    value = df_pop_country_num.loc[df_pop_country_num['country'] == country, age_group_mapping[age_group]].values[0]
    return value

country = pop_country
age_group = pop_age
scaler = get_population(country, age_group)

print(df_pop_total['initial'] )
df_pop_total['initial'] = df_pop_total['initial'].astype(int)
df_pop_total['adjusted'] = df_pop_total['adjusted'].astype(int)

df_pop_total['scaled_int'] = df_pop_total['initial'] * scaler
df_pop_total['scaled_adj'] = df_pop_total['adjusted'] * scaler
# df_pop_total = df_pop_total.drop(['initial', 'adjusted', 'adjusted_value', 'initial_value', 'difference'], axis=1)
df_pop_total['scaled_int_z'] = df_pop_total['scaled_int'].clip(lower=0)
df_pop_total['scaled_adj_z'] = df_pop_total['scaled_adj'].clip(lower=0)

df_pop_total['scaled_adj_value'] = df_pop_total['scaled_adj'] * df_popselectedmoney['hourly_value']
df_pop_total['scaled_int_value'] = df_pop_total['scaled_int'] * df_popselectedmoney['hourly_value']
df_pop_total['scaled_int_value_z'] = df_pop_total['scaled_int_value'].clip(lower=0)
df_pop_total['scaled_adj_value_z'] = df_pop_total['scaled_adj_value'].clip(lower=0)

pop_percent = float(pop_percent)
pop_percentsuccess = float(pop_percentsuccess)
df_pop_total['scaled_adj_a'] = df_pop_total['scaled_adj'] * (pop_percent / 100) * (pop_percentsuccess / 100)
df_pop_total['scaled_adj_u'] = df_pop_total['scaled_int'] - (df_pop_total['scaled_int']*(pop_percent / 100)*(pop_percentsuccess / 100))
df_pop_total['scaled_adj_f'] = df_pop_total['scaled_adj_a']+df_pop_total['scaled_adj_u']
df_pop_total = df_pop_total.drop(['country','age_group','initial','adjusted','adjusted_value','initial_value','difference','scaled_int','scaled_adj','scaled_adj_value', 'scaled_int_value', 'scaled_adj_a', 'scaled_adj_u'], axis=1)
print(df_pop_total)
df_pop_total = df_pop_total.astype(int)
df_pop_total[df_pop_total < 0] = 0
# df_pop_total['']
print(df_pop_total)

#----------------------------------------------------------------------------------------------------------------------------------
@anvil.server.callable
def create_barfig_initial_time():
  data = df_final
  fig_initial_time = px.bar(data, x=df_final.index,
                            y='initial_value',
                            title="Before Intervention Time Spent On Non-Market Productive Activities",
                            color_discrete_sequence=["red"],
                            labels={'index': 'Activity', 'initial_value':'Minutes Per Month'})
  return fig_initial_time

@anvil.server.callable
def create_barfig_adjusted_time():
  data = df_final
  fig_adjusted_time = px.bar(data, x=df_final.index,
                             y='adjusted_value',
                             title="After Intervention Time Spent On Non-Market Productive Activities",
                             color_discrete_sequence=["blue"],
                             labels={'index': 'Activity', 'adjusted_value':'Minutes Per Month'})
  return fig_adjusted_time
  
@anvil.server.callable
def create_barfig_difference_time():
  data = df_final
  fig_difference_time = px.bar(data, x=df_final.index,
                               y='difference_monthlytime',
                               title="Increase In Time Spent On<br>Non-Market Productive Activities",
                               color_discrete_sequence=["green"],
                               labels={'index': 'Activity', 'difference_monthlytime':'Minutes Per Month'})
  return fig_difference_time
  
@anvil.server.callable
def create_barfig_combo_time():
  data = df_final
  fig1 = go.Figure(data=[
        go.Bar(name="Before Intervention",
          x=df_final.index,
          y=data["initial_monthlytime"],
          offsetgroup=0,
          marker=dict(color='red')),
        go.Bar(name="After Intervention",
          x=df_final.index,
          y=data["adjusted_monthlytime"],
          offsetgroup=1,
          marker=dict(color='blue'))
        # go.Bar(name="Difference Values",
        #   x=df_final.index,
        #   y=data["difference_value"],
        #   offsetgroup=1,
        #   marker=dict(color='green'))
    ],
    layout=go.Layout(
        title="Time Spent On Non-Market Productive Activities",
        yaxis_title="Minutes Per Month",
        xaxis_title="Activity"
    )
  )
  fig1.update_xaxes(tickangle=90)
  return fig1

@anvil.server.callable
def create_piefig_time():
  data = [go.Pie(labels= df_final.index,
                 values=df_final.iloc[:,0],
                 domain={'x':[0.3,0.7], 'y':[0.2,0.8]}, 
                 hole=0.5,
                 direction='clockwise',
                 sort=False,
                 title=dict(text='Before',
                      position='top center')
                ),
           go.Pie(labels= df_final.index,
                 values=df_final.iloc[:,1],
                 domain={'x':[0.1,0.9], 'y':[0,1]},
                 hole=0.75,
                 direction='clockwise',
                 sort=False,
                 title=dict(text='After',
                     position='top center')
                 )
         ]
  figure=go.Figure(data=data, layout={'title':'Breakdown Of Time Spent<br>On Non-Market Productive Activities' + '<br>' +  '<span style="font-size: 12px;">Before Intervention (Inner Circle)</span>' + '<br>' +  '<span style="font-size: 12px;">After Intervention (Outer Circle)</span>'})  
  figure.update_traces(textposition='inside')
  figure.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
  return(figure)

@anvil.server.callable
def create_piefig_difference_time():
  trace = go.Pie(labels= df_final.index, values=df_final.iloc[:,2])
  data = [trace]
  fig = go.Figure(data = data, layout={'title':'Breakdown Of Increase In Time Spent<br>On Non-Market Productive Activities'})                                    
  return(fig)

@anvil.server.callable
def create_piefig_timecomp_initial():
  trace = go.Pie(labels= df_total_diff_trans.index,values=df_total_diff_trans.loc[:,"initial_times"],sort=False)
  data = [trace]
  fig = go.Figure(data = data, layout={'title':'Time Usage Before Intervention'})  
  fig.update_traces(marker=dict(colors=['blue', 'red']))
  return(fig)

@anvil.server.callable
def create_piefig_timecomp_adjusted():
  trace = go.Pie(labels= df_total_diff_trans.index,values=df_total_diff_trans.loc[:,"adjusted_times"],sort=False)
  data = [trace]
  fig = go.Figure(data = data, layout={'title':'Time Usage After Intervention'}) 
  fig.update_traces(marker=dict(colors=['blue', 'red']))
  return(fig)
    
@anvil.server.callable
def get_variables():
    return app_tables.selectedvariables_i.search()[0]

@anvil.server.callable
def get_money():
    return app_tables.moneyvalues.search()[0]

@anvil.server.callable
def get_inital_time():
  return int(total_initial_time)

@anvil.server.callable
def get_adjusted_time():
  return int(total_adjusted_time)

@anvil.server.callable
def get_difference_time():
  return int(total_difference_time)

@anvil.server.callable
def get_inital_value():
  return int(total_initial_value)

@anvil.server.callable
def get_adjusted_value():
  return int(total_adjusted_value)
  
@anvil.server.callable
def get_difference_value():
  return int(total_difference_value)

@anvil.server.callable
def get_popinfo():
  return app_tables.pop_info.search()

#----------------------------------------------------------------------------------------------------------------------------------------
 
@anvil.server.callable
def pop_create_barfig_difference_time():
    data = df_pop_total
    fig_difference_time = px.bar(data,
                               x=df_pop_total.index,
                               y='scaled_adj_f',
                               title="Increase In Economic Impact (€)<br>Due To Intervention",
                               color_discrete_sequence=["green"],
                               labels={'activity': 'Activity', 'scaled_adj_p':'Minutes Per Month'})
    return fig_difference_time

@anvil.server.callable
def pop_create_barfig_combo_time():
  data = df_pop_total
  fig1 = go.Figure(data=[
        go.Bar(name="Before Intervention",
          x=df_pop_total.index,
          y=data["scaled_int_z"],
          offsetgroup=0,
          marker=dict(color='red')),
        go.Bar(name="After Intervention",
          x=df_pop_total.index,
          y=data["scaled_adj_f"],
          offsetgroup=1,
          marker=dict(color='blue'))
        # go.Bar(name="Difference Values",
        #   x=df_final.index,
        #   y=data["difference_value"],
        #   offsetgroup=1,
        #   marker=dict(color='green'))
    ],
    layout=go.Layout(
        title="Time Spent On Non-Market Productive Activities",
        yaxis_title="Minutes Per Month",
        xaxis_title="Activity"
    )
  )
  fig1.update_xaxes(tickangle=90)
  return fig1


