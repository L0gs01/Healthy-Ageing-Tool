from ._anvil_designer import HomepageTemplate
from anvil import *
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

    # Any code you write here will run before the form opens.

  def is_button_select_click(self, **event_args):
    """This method is called when the button is clicked"""
    global variables
    variables= {}
    self.homepage_buttons.visible = False
    save_clicked = alert(
      content = Individual_InitialSelection(item=variables),
      title = "Select Variables For Individual",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
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

  def is_edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(
      content = Individual_InitialSelection(item=variables),
      title = "Edit Variables For Individual",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('get_variables')
    anvil.server.call('get_money')
    self.plots_card.visible=True
    fig = anvil.server.call('create_fig_combo') 
    self.combo_plot.figure = fig



