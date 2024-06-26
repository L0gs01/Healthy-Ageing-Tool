from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from anvil.designer import in_designer
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Individual_InitialSelection import Individual_InitialSelection
from ..Individual_EditSelection import Individual_EditSelection
from ..Individual_MoneyValue import Individual_MoneyValue
from ..Individual_ViewSelection import Individual_ViewSelection
from ..Population_InitialSelection import Population_InitialSelection
from ..Population_ViewSelection import Population_ViewSelection
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
    # self.refresh_popinfo()
    # Any code you write here will run before the form opens.

  def refresh_popinfo(self):
    self.popinfo_panel.items = anvil.server.call('get_popinfo')
  
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
      if variables['country'] == (' United Kingdom') and variables['education'] == ('Lower Than Secondary'):
          alert('There is no data for people with education "lower than secondary" in the United Kindgom. Please choose a different country and/or education level.')

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
        if variables['country'] == (' United Kingdom') and variables['education'] == ('Lower Than Secondary'):
          alert('There is no data for individuals that are "Lower Than Secondary" in educaton AND from the "UK". Please make a different selection')


  def is_money_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    global money_val
    housing='15.4'
    transport='6.86'
    nutrition='3.56'
    clothing='0.91'
    laundry='12.29'
    childcare='4.9'
    adultcare='4.46'
    voluntaryactivity='11.63'
    money_val={'housing':housing,'transport':transport,'nutrition':nutrition,'clothing':clothing,'laundry':laundry,'childcare':childcare,'adultcare':adultcare,'voluntaryactivity':voluntaryactivity}
    save_clicked = alert(
      content = Individual_MoneyValue(item=money_val),
      title = "Edit Monetary Value For Activities",
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
    # else:
    #   app_tables.moneyvalues.delete_all_rows()

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
    self.name_4.content = self.name_label.text
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
    # difference_value_text = anvil.server.call('get_difference_value')
    difference_value_text = (adjusted_value_text - initial_value_text)
    if difference_value_text < 0:
      difference_value_text = 0
    self.difference_value1.content = difference_value_text
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

  def pop_button_select_click(self, **event_args):
    """This method is called when the button is clicked"""
    global pop_variables
    self.homepage_buttons.visible = False
    pop_variables= {}
    save_clicked = alert(
      content = Population_InitialSelection(item=pop_variables),
      title = "Define the populations’s characteristics:",
      large=True,
      buttons=[("Next", True), ("Cancel", False)],
    )
    if save_clicked:
      app_tables.pop_info.delete_all_rows()
      app_tables.pop_info.add_row(pop_country=str(pop_variables['country']),
                                 pop_name = str(pop_variables['name']),
                                 pop_age=str(pop_variables['age']),
                                 pop_initial=str(pop_variables['initial']),
                                 pop_percent=(pop_variables['percent']),
                                 pop_percentsuccess=(pop_variables['percent_s']),
                                 pop_adjusted=str(pop_variables['adjusted']))
      self.refresh_popinfo()
      print(pop_variables)
      self.populationhome_card.visible = True

  def pop_add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pop_variables= {}
    save_clicked = alert(
      content = Population_InitialSelection(item=pop_variables),
      title = "Define the populations’s characteristics:",
      large=True,
      buttons=[("Next", True), ("Cancel", False)],
    )
    if save_clicked:
      print(pop_variables)
      #app_tables.pop_info.delete_all_rows()
      app_tables.pop_info.add_row(pop_country_dd=str(pop_variables['country']),
                                 pop_name_text = str(pop_variables['name']),
                                 pop_age_dd=str(pop_variables['age']),
                                 pop_initial_dd=str(pop_variables['initial']),
                                 pop_percent_slider=(pop_variables['percent']),
                                 pop_percentsuccess_slider=(pop_variables['percent_s']),
                                 pop_adjusted_dd=str(pop_variables['adjusted']))
      self.refresh_popinfo()
      self.populationhome_card.visible = True

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.pop_plots_card.visible=True
    pop_stacked_bar_val= anvil.server.call('pop_create_barfig_combo_time') 
    self.pop_stacked_bar.figure = pop_stacked_bar_val
    pop_diff_bar_val= anvil.server.call('pop_create_barfig_difference_time') 
    self.pop_dif_bar.figure = pop_diff_bar_val
    self.pop_int_bar_val= anvil.server.call('pop_create_barfig_initial_time') 
    self.pop_int_bar.figure = self.pop_int_bar_val
    self.pop_adj_bar_val= anvil.server.call('pop_create_barfig_adjusted_time') 
    self.pop_adj_bar.figure = self.pop_adj_bar_val
    self.pop_stacked_pie.figure = anvil.server.call('pop_create_piefig_time')
    self.pop_difference_pie.figure = anvil.server.call('pop_create_piefig_difference_time')
    self.pop_intyear_pie.figure = anvil.server.call('pop_create_piefig_timecomp_initial')
    self.pop_adjyear_pie.figure = anvil.server.call('pop_create_piefig_timecomp_adjusted')  
    #sentence stuff  
    pop_initial_value_text = anvil.server.call('pop_get_inital_value')
    self.pop_initial_box.content = pop_initial_value_text
    pop_adjusted_value_text = anvil.server.call('pop_get_adjusted_value')
    self.pop_adjusted_box.content = pop_adjusted_value_text
    pop_difference_value_text = (pop_adjusted_value_text - pop_initial_value_text)
    if pop_difference_value_text < 0:
      pop_difference_value_text = 0
    self.pop_difference_box.content = pop_difference_value_text

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.homepage_buttons.visible =True
    self.individualhome_card.visible = False 
    self.plots_card.visable = False
    self.populationhome_card.visible = False 
    self.pop_plots_card.visible = False

  def general_nav_card_hide(self, **event_args):
    """This method is called when the column panel is removed from the screen"""
    self.homepage_buttons.visible = True
    
    






