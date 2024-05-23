from ._anvil_designer import Population_ViewSelectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.designer import in_designer
from anvil.designer import in_designer


class Population_ViewSelection(Population_ViewSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.pop_repeating_panel.items = app_tables.pop_info.search(q.all_of())

  def pop_percent_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.pop_viewpercent_label.text = self.pop_percent_slider.level
  
  def pop_percentsuccess_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.pop_viewpercent_label.text = self.pop_percentsuccess_slider.level

  def pop_addgroup_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    save_clicked = alert(
      content = Population_ViewSelection(item=variable),
      title = "Define the person’s characteristics:",
      large=True,
      buttons=[("Next", True), ("Cancel", False)],
    )
    if save_clicked:
        print(variables)
