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


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.

# -----------------------CREATE SELECTED DATAFRAMES
df_europe = pd.read_csv(data_files['all_predicted_values_total.csv'])
df_belgium = pd.read_csv(data_files['BE_predicted_values_total.csv'])
df_estonia = pd.read_csv(data_files['EE_predicted_values_total.csv'])
df_finland = pd.read_csv(data_files['FI_predicted_values_total.csv'])
df_france = pd.read_csv(data_files['FR_predicted_values_total.csv'])
df_greece = pd.read_csv(data_files['EL_predicted_values_total.csv'])
df_romania = pd.read_csv(data_files['RO_predicted_values_total.csv'])
df_serbia = pd.read_csv(data_files['RS_predicted_values_total.csv'])
df_ukireland = pd.read_csv(data_files['UK_predicted_values_total.csv'])

selected_var = app_tables.selectedvariables_i.search()
variable_dicts = [{'initialrank':r['initialrank'], 'adjustedrank':r['adjustedrank'], 'age':r['age'],'sex':r['sex'],'maritalstatus':r['maritalstatus'], 'employment':r['employment'], 'education':r['education'], 'country':r['country']} for r in selected_var]
df_selectedvariables = pd.DataFrame.from_dict(variable_dicts)
selected_money = app_tables.moneyvalues.search()
money_dicts = [{'housing':r['housing'], 'transport':r['transport'], 'nutrition':r['nutrition'],'clothing':r['clothing'],'laundry':r['laundry'], 'childcare':r['childcare'], 'adultcare':r['adultcare'], 'voluntaryactivity':r['voluntaryactivity']} for r in selected_money]
df_selectedmoney = pd.DataFrame.from_dict(money_dicts)
# print(df_selectedvariables)
# print(df_selectedmoney)
#---------------------CREATED CSV DATAFRAMES
data_country = df_selectedvariables.at[0,'country']
# print(data_country)
df_predictedvalues = None
if data_country == 'Europe (all)': df_predictedvalues = df_europe
if data_country == 'Belgium': df_predictedvalues = df_belgium
if data_country == 'Estonia': df_predictedvalues = df_estonia
if data_country == 'Finland': df_predictedvalues = df_finland
if data_country == 'France': df_predictedvalues = df_france
if data_country == 'Greece': df_predictedvalues = df_greece
if data_country == 'Romania': df_predictedvalues = df_romania
if data_country == 'Serbia': df_predictedvalues = df_serbia
if data_country == 'United Kingdom of Great Britain and Northern Ireland': df_predicted_values = df_ukireland
# print(df_predictedvalues)
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
if selection_employment == 'Not Payed':
    selection_employment = 'not_paid'
if selection_education == 'Lower Than Secondary':
    selection_education = 'lower_than_secondary'
if selection_education == 'Secondary':
    selection_education = 'secondary_non_tertiary'
if selection_education == 'Tertiary':
    selection_education = 'tertiary'

#----------------------------------
initial_filter_criteria = (df_predictedvalues['sph_rec_rel']==selection_initialrank)&(df_predictedvalues['age_rec_10y']==selection_age)&(df_predictedvalues['sex_rec']==selection_sex)&(df_predictedvalues['marital_rec_rel']==selection_maritalstatus)&(df_predictedvalues['employment_rec']==selection_employment)&(df_predictedvalues['education_rec']==selection_education)
df_initial = df_predictedvalues[initial_filter_criteria]


adjusted_filter_criteria = (df_predictedvalues['sph_rec_rel']==selection_adjustedrank)&(df_predictedvalues['age_rec_10y']==selection_age)&(df_predictedvalues['sex_rec']==selection_sex)&(df_predictedvalues['marital_rec_rel']==selection_maritalstatus)&(df_predictedvalues['employment_rec']==selection_employment)&(df_predictedvalues['education_rec']==selection_education)
df_adjusted = df_predictedvalues[adjusted_filter_criteria]


df_initial.drop(['age_rec_10y','sph_rec_rel','sex_rec','marital_rec_rel','employment_rec','education_rec','COUNTRY'],axis=1,inplace=True)
df_initial.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
df_initial.drop(["a"], axis=1, inplace=True)

df_adjusted.drop(['age_rec_10y','sph_rec_rel','sex_rec','marital_rec_rel','employment_rec','education_rec','COUNTRY'],axis=1,inplace=True)
df_adjusted.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
df_adjusted.drop(["a"], axis=1, inplace=True)

df_initial.rename(columns={"link": "initial_value"},inplace = True)
df_adjusted.rename(columns={"link": "adjusted_value"},inplace = True)
print(df_initial)   
print(df_adjusted) 

df_combo = pd.merge(df_initial,df_adjusted, on='ACTIVITY')
df_combo.drop(['combination_x','SE_x','combination_y','SE_y'],axis=1,inplace=True)
df_combo.set_index('ACTIVITY',inplace=True)
print(df_combo)

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

df_hourlyvalue = DataFrame(data = hourly_data, columns = ['HourlyValue'])
df_hourlyvalue.index =['Housing','Transport','Nutrition','Clothing','Laundry','ChildCare','AdultCare','Voluntary']
print(df_hourlyvalue)


df_combo['difference_value'] = (df_combo.adjusted_value-df_combo.initial_value)
df_combo['initial_monthly'] = (((df_combo.initial_value * df_hourlyvalue.HourlyValue)/60)*12)
df_combo['adjusted_monthly'] = (((df_combo.adjusted_value * df_hourlyvalue.HourlyValue)/60)*12)

housing_difference = (df_combo.at['Housing',"adjusted_monthly"])-(df_combo.at['Housing',"initial_monthly"])
transport_difference = (df_combo.at['Transport',"adjusted_monthly"])-(df_combo.at['Transport',"initial_monthly"])
nutrition_difference = (df_combo.at['Nutrition',"adjusted_monthly"])-(df_combo.at['Nutrition',"initial_monthly"])
clothing_difference = (df_combo.at['Clothing',"adjusted_monthly"])-(df_combo.at['Clothing',"initial_monthly"])
laundry_difference = (df_combo.at['Laundry',"adjusted_monthly"])-(df_combo.at['Laundry',"initial_monthly"])
childcare_difference = (df_combo.at['ChildCare',"adjusted_monthly"])-(df_combo.at['ChildCare',"initial_monthly"])
adultcare_difference = (df_combo.at['AdultCare',"adjusted_monthly"])-(df_combo.at['AdultCare',"initial_monthly"])
voluntary_difference = (df_combo.at['Voluntary',"adjusted_monthly"])-(df_combo.at['Voluntary',"initial_monthly"])

list_difference = [housing_difference,transport_difference,nutrition_difference,clothing_difference,laundry_difference,childcare_difference,adultcare_difference,voluntary_difference]

df_difference = DataFrame(data = list_difference, columns = ['difference_monthly'])
df_difference.index =['Housing','Transport','Nutrition','Clothing','Laundry','ChildCare','AdultCare','Voluntary']
df_difference
df_final_raw= pd.merge(df_combo,df_difference, left_index=True, right_index=True)


df_final = df_final_raw.apply(lambda column: column.astype(int))
df_final[df_final < 0] = 0

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df_final)
print(df_final.dtypes)

total_initial_time = df_final['initial_value'].sum()
total_adjusted_time = df_final['adjusted_value'].sum()
total_difference_time = df_final['difference_value'].sum()
total_initial_value = df_final['initial_monthly'].sum()
total_adjusted_value = df_final['adjusted_monthly'].sum()
total_difference_value = df_final['difference_monthly'].sum()

totals = (total_initial_time,total_adjusted_time,total_difference_time,total_initial_value,total_adjusted_value,total_difference_value)

df_totals = DataFrame(data = totals, columns = ['HourlyValue'])
df_totals.index=['total_initial_time','total_adjusted_time','total_difference_time','total_initial_value','total_adjusted_value','total_difference_value']
print(df_totals)


total_initial_time_diff = 525600 - (total_initial_time*60)
total_adjusted_time_diff = 525600 - (total_adjusted_time*60)
total_difference_time_diff = 525600 - (total_difference_time*60)
total_time_diff = {'activity_time':[total_initial_time*60,total_adjusted_time*60,total_difference_time*60],'nonactivity_time':[total_initial_time_diff,total_adjusted_time_diff,total_difference_time_diff]}
df_total_diff = pd.DataFrame(data=total_time_diff)
df_total_diff.index = ['initial_times','adjusted_times','diiference_times']
df_total_diff_trans = df_total_diff.T
print(df_total_diff_trans)

#display(df_final)

@anvil.server.callable
def create_barfig_initial_time():
  data = df_final
  fig_initial_time = px.bar(data, x=df_final.index, y='initial_value',title="Monthly Value Before Intervention",color_discrete_sequence=["red"],labels={'x': 'Activity', 'y':'Hours Spent (Monthly)'})
  return fig_initial_time

@anvil.server.callable
def create_barfig_adjusted_time():
  data = df_final
  fig_adjusted_time = px.bar(data, x=df_final.index, y='adjusted_value',title="Monthly Value After Intervention")
  return fig_adjusted_time
  
@anvil.server.callable
def create_barfig_difference_time():
  data = df_final
  fig_difference_time = px.bar(data, x=df_final.index, y='difference_value',title="Difference In Monthly Value",color_discrete_sequence=["green"])
  return fig_difference_time
  
@anvil.server.callable
def create_barfig_combo_time():
  data = df_final
  fig1 = go.Figure(data=[
        go.Bar(name="Initial Values",
          x=df_final.index,
          y=data["initial_value"],
          offsetgroup=0),
        go.Bar(name="Adjusted Values",
          x=df_final.index,
          y=data["adjusted_value"],
          offsetgroup=1),
        go.Bar(name="Difference Values",
          x=df_final.index,
          y=data["difference_value"],
          offsetgroup=1)
    ],
    layout=go.Layout(
        title="Comparative Values (monthly time)",
        yaxis_title="Value",
        xaxis_title="Activities"
    )
  )
  return fig1

@anvil.server.callable
def create_piefig_time():
  data = [go.Pie(labels= df_final.index,
                 values=df_final.iloc[:,0],
                 domain={'x':[0.3,0.7], 'y':[0.2,0.8]}, 
                 hole=0.5,
                 direction='clockwise',
                 sort=False,
                 title = "Time (monthly)"),
           go.Pie(labels= df_final.index,
                 values=df_final.iloc[:,1],
                 domain={'x':[0.1,0.9], 'y':[0,1]},
                 hole=0.75,
                 direction='clockwise',
                 sort=False)
         ]
  figure=go.Figure(data=data, layout={'title':'Activity Percent By Time' + '<br>' +  '<span style="font-size: 12px;">Before (Inner Circle)</span>' + '<br>' +  '<span style="font-size: 12px;">After (Outer Circle)</span>'})  
  figure.update_traces(textposition='inside')
  figure.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
  return(figure)

@anvil.server.callable
def create_piefig_difference_time():
  trace = go.Pie(labels= df_final.index, values=df_final.iloc[:,2],title= 'Time (Difference)')
  data = [trace]
  fig = go.Figure(data = data, layout={'title':'Additional Time Spent In Activity'})                                    
  return(fig)

@anvil.server.callable
def create_piefig_timecomp_initial():
  trace = go.Pie(labels= df_total_diff_trans.index,values=df_total_diff_trans.loc[:,"initial_times"])
  data = [trace]
  fig = go.Figure(data = data, layout={'title':'Time Spent in Activities Vs. Whole (Before)'})  
  return(fig)

@anvil.server.callable
def create_piefig_timecomp_adjusted():
  trace = go.Pie(labels= df_total_diff_trans.index,values=df_total_diff_trans.loc[:,"adjusted_times"])
  data = [trace]
  fig = go.Figure(data = data, layout={'title':'Time Spent in Activities Vs. Whole (After)'}) 
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

