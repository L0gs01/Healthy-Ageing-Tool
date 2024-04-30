from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Individual_InitialSelection import Individual_InitialSelection
from ..Individual_EditSelection import Individual_EditSelection
from ..Individual_MoneyValue import Individual_MoneyValue
from ..Individual_ViewSelection import Individual_ViewSelection
import anvil.media

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    app_tables.moneyvalues.delete_all_rows()
    app_tables.moneyvalues.add_row(housing='15.4',
                            transport='6.86',
                            nutrition='3.56',
                            clothing='0.91',
                            laundry='12.29',
                            childcare='4.9',
                            adultcare='4.46',
                            voluntaryactivity='11.63')
    # Any code you write here will run before the form opens.

  def is_button_select_click(self, **event_args):
    """This method is called when the button is clicked"""
    global variables
    variables= {}
    self.homepage_buttons.visible = False
    save_clicked = alert(
      content = Individual_InitialSelection(item=variables),
      title = "Define the person’s characteristics:",
      large=True,
      buttons=[("Next", True), ("Cancel", False)],
    )
    if save_clicked:
        self.individualhome_card.visible = True
        app_tables.selectedvariables_i.delete_all_rows()
        app_tables.selectedvariables_i.add_row(initialrank=variables['initialrank'],
                                            sex=variables['sex'],
                                            age=variables['age'],
                                            maritalstatus=variables['maritalstatus'],
                                            employment=variables['employment'],
                                            education=variables['education'],
                                            country=variables['country'],
                                            adjustedrank=variables['adjustedrank'],
                                            name=variables['name'])
        self.name_label.text = variables['name']
        self.initialrank_label.text = variables['initialrank']
        self.adjustedrank_label.text = variables['adjustedrank']
        self.age_label.text = variables['age']
        self.sex_label.text = variables['sex']
        self.maritalstatus_label.text = variables['maritalstatus']
        self.employment_label.text = variables['employment']
        self.education_label.text = variables['education']
        self.country_label.text = variables['country'] 
        print(variables)
        if variables['country'] == ('United Kingdom') and variables['education'] == ('Lower Than Secondary'):
          alert('Your selection criteria results in no data. Please make a different selection')

  def is_edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(
      content = Individual_InitialSelection(item=variables),
      title = "Define the person’s characteristics:",
      large=True,
      buttons=[("Next", True), ("Cancel", False)],
    )
    if save_clicked:
        print(variables)
        app_tables.selectedvariables_i.delete_all_rows()
        app_tables.selectedvariables_i.add_row(initialrank=variables['initialrank'],
                                            sex=variables['sex'],
                                            age=variables['age'],
                                            maritalstatus=variables['maritalstatus'],
                                            employment=variables['employment'],
                                            education=variables['education'],
                                            country=variables['country'],
                                            adjustedrank=variables['adjustedrank'],
                                            name=variables['name'])
                                            #datetime = anvil.server.call('get_datetime'))
        self.name_label.text = variables['name']
        self.initialrank_label.text = variables['initialrank']
        self.adjustedrank_label.text = variables['adjustedrank']
        self.age_label.text = variables['age']
        self.sex_label.text = variables['sex']
        self.maritalstatus_label.text = variables['maritalstatus']
        self.employment_label.text = variables['employment']
        self.education_label.text = variables['education']
        self.country_label.text = variables['country'] 
        if variables['country'] == ('United Kingdom') and variables['education'] == ('Lower Than Secondary'):
          alert('Your selection criteria results in no data. Please make a different selection')


  def is_money_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    global money_val
    money_val = {}
    save_clicked = alert(
      content = Individual_MoneyValue(item=money_val),
      title = "Edit Monatary Value For Activities",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
    )
    if save_clicked:
        print(money_val)
        app_tables.moneyvalues.delete_all_rows()
        app_tables.moneyvalues.add_row(housing=money_val['housing'],
                                              transport=money_val['transport'],
                                              nutrition=money_val['nutrition'],
                                              clothing=money_val['clothing'],
                                              laundry=money_val['laundry'],
                                              childcare=money_val['childcare'],
                                              adultcare=money_val['adultcare'],
                                              voluntaryactivity=money_val['voluntaryactivity'])
    else:
      app_tables.moneyvalues.delete_all_rows()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('get_variables')
    anvil.server.call('get_money')
    self.plots_card.visible=True
    #bar graphs
    # barfig_initial_time = anvil.server.call('create_barfig_initial_time') 
    # self.initial_time_bar.figure = barfig_initial_time
    barfig_combo_time = anvil.server.call('create_barfig_combo_time') 
    self.combo_bar_time.figure = barfig_combo_time
    # barfig_adjusted_time = anvil.server.call('create_barfig_adjusted_time')
    # self.adjusted_time_bar.figure = barfig_adjusted_time
    barfig_difference_time = anvil.server.call('create_barfig_difference_time')
    self.difference_time_bar.figure = barfig_difference_time
    #pie charts
    self.time_pie.figure = anvil.server.call('create_piefig_time')
    self.difference_time_pie.figure = anvil.server.call('create_piefig_difference_time')
    self.time_comparison_pie_initial.figure = anvil.server.call('create_piefig_timecomp_initial')
    self.time_comparison_pie_adjusted.figure = anvil.server.call('create_piefig_timecomp_adjusted')
    #sentence stuff
    self.name_1.content = self.name_label.text
    self.name_2.content = self.name_label.text
    self.name_3.content = self.name_label.text
    self.initial_rank1.content = self.initialrank_label.text
    self.initial_rank2.content = self.initialrank_label.text
    self.adjusted_rank1.content = self.adjustedrank_label.text
    self.adjusted_rank2.content = self.adjustedrank_label.text
    initial_value_text = anvil.server.call('get_inital_value')
    self.initial_box.content = initial_value_text
    self.initial_value.content = initial_value_text
    adjusted_value_text = anvil.server.call('get_adjusted_value')
    self.adjusted_value.content = adjusted_value_text
    self.adjusted_box.content = adjusted_value_text
    difference_value_text = anvil.server.call('get_difference_value')
    self.difference_value.content = difference_value_text
    self.difference_box.content = difference_value_text


    

  def homepage_navbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def individual_navbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def population_navbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def initial_time_bar_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def adjusted_time_bar_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def combo_bar_time_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass





