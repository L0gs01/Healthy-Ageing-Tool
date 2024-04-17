from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

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
      content = individualinitial
      
      (item=variables),
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
