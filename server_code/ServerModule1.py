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
import plotly.graph_objects as go


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.

# -----------------------CREATE SELECTED DATAFRAMES
#df_europe = pd.read_csv(data_files[''])
df_belgium = pd.read_csv(data_files['BE_predicted_values.csv'])
df_estonia = pd.read_csv(data_files['EE_predicted_values.csv'])
df_finland = pd.read_csv(data_files['FI_predicted_values.csv'])
df_france = pd.read_csv(data_files['FR_predicted_values.csv'])
df_greece = pd.read_csv(data_files['EL_predicted_values.csv'])
df_romania = pd.read_csv(data_files['RO_predicted_values.csv'])
df_serbia = pd.read_csv(data_files['RS_predicted_values.csv'])
df_ukireland = pd.read_csv(data_files['UK_predicted_values.csv'])

selected_var = app_tables.selectedvariables_i.search()
variable_dicts = [{'initialrank':r['initialrank'], 'adjustedrank':r['adjustedrank'], 'age':r['age'],'sex':r['sex'],'maritalstatus':r['maritalstatus'], 'employment':r['employment'], 'education':r['education'], 'country':r['country']} for r in selected_var]
print(variable_dicts)
df_selectedvariables = pd.DataFrame.from_dict(variable_dicts)
selected_money = app_tables.moneyvalues.search()
money_dicts = [{'housing':r['housing'], 'transport':r['transport'], 'nutrition':r['nutrition'],'clothing':r['clothing'],'laundry':r['laundry'], 'childcare':r['childcare'], 'adultcare':r['adultcare'], 'voluntaryactivity':r['voluntaryactivity']} for r in selected_money]
print(money_dicts)
df_selectedmoney = pd.DataFrame.from_dict(money_dicts)

#---------------------CREATED CSV DATAFRAMES
df_selectedvariable = pd.DataFrame.from_dict(variable_dicts)
data_country = df_selectedvariable.at[0,'country']
print(data_country)

df_predictedvalues = None
# if data_country == 'Europe (all)': df_predicted_values = df_europe
if data_country == 'Belgium': df_predictedvalues = df_belgium
if data_country == 'Estonia': df_predictedvalues = df_estonia
if data_country == 'Finland': df_predictedvalues = df_finland
if data_country == 'France': df_predictedvalues = df_france
if data_country == 'Greece': df_predictedvalues = df_greece
if data_country == 'Romania': df_predictedvalues = df_romania
if data_country == 'Serbia': df_predictedvalues = df_serbia
if data_country == 'United Kingdom of Great Britain and Northern Ireland': df_predicted_values = df_ukireland
print(df_predictedvalues)
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
if selection_adjustedrank == 'Bad':
    selection_adjustedrank = 'bad'
if selection_adjustedrank == 'Fair':
    selection_adjustedrank = 'fair'
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
print(selection_adjustedrank)

df_initial.drop(['age_rec_10y','sph_rec_rel','sex_rec','marital_rec_rel','employment_rec','education_rec','COUNTRY'],axis=1,inplace=True)
df_adjusted.drop(['age_rec_10y','sph_rec_rel','sex_rec','marital_rec_rel','employment_rec','education_rec','COUNTRY'],axis=1,inplace=True)

print(df_initial)
print(df_adjusted)

df_initial.rename(columns={"link": "initial_value"},inplace = True)
df_adjusted.rename(columns={"link": "adjusted_value"},inplace = True)

df_combo = pd.merge(df_initial,df_adjusted, on='ACTIVITY')
df_combo.drop(['combination_x','SE_x','combination_y','SE_y'],axis=1,inplace=True)
print(df_combo)


housing_difference = (df_combo.at[0,"adjusted_value"])-(df_combo.at[0,"initial_value"])
transport_difference = (df_combo.at[1,"adjusted_value"])-(df_combo.at[1,"initial_value"])
nutrition_difference = (df_combo.at[2,"adjusted_value"])-(df_combo.at[2,"initial_value"])
clothing_difference = (df_combo.at[3,"adjusted_value"])-(df_combo.at[3,"initial_value"])
laundry_difference = (df_combo.at[4,"adjusted_value"])-(df_combo.at[4,"initial_value"])
childcare_difference = (df_combo.at[5,"adjusted_value"])-(df_combo.at[5,"initial_value"])
adultcare_difference = (df_combo.at[6,"adjusted_value"])-(df_combo.at[6,"initial_value"])
voluntary_difference = (df_combo.at[7,"adjusted_value"])-(df_combo.at[7,"initial_value"])

list_difference = [housing_difference,
                  transport_difference,
                  nutrition_difference,
                  clothing_difference,
                  laundry_difference,
                  childcare_difference,
                  adultcare_difference,
                  voluntary_difference]
df_difference = DataFrame(data = list_difference, columns = ['difference_value'])
df_difference

df_final= pd.merge(df_combo,df_difference, left_index=True, right_index=True)
print(df_final)


@anvil.server.callable
def create_fig_initial():
  fig = px.bar(df_final, x='ACTIVITY', y='initial_value')
  fig.show()
@anvil.server.callable
def create_fig_adjusted():
  data = df_final
  fig1 = go.Figure(
    data = [go.Bar(
            name="Adjusted Values",
            x=data["ACTIVITY"],
            y=data["adjusted_value"],
        ),
    ],
    layout=go.Layout(
        title="Adjusted Values",
        yaxis_title="Value"
    )
    )
  fig1.show()
@anvil.server.callable
def create_fig_combo():
  data = df_final
  fig1 = go.Figure(
    data = [
        go.Bar(
            name="Initial Values",
            x=data["ACTIVITY"],
            y=data["initial_value"],
            offsetgroup=0,
        ),
        go.Bar(
            name="Adjusted Values",
            x=data["ACTIVITY"],
            y=data["adjusted_value"],
            offsetgroup=1,
        ),
        go.Bar(
            name="Difference",
            x=data["ACTIVITY"],
            y=data["difference_value"],
            offsetgroup=1,
        ),
    ],
    layout=go.Layout(
        title="Comparative Values",
        yaxis_title="Value"
    )
    )
  fig1.show()

@anvil.server.callable
def get_variables():
    return app_tables.selectedvariables_i.search()[0]

@anvil.server.callable
def get_money():
    return app_tables.moneyvalues.search()[0]