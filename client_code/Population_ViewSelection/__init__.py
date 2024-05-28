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
    # self.pop_repeating_panel.items = app_tables.pop_info.search(q.all_of())

  def pop_viewpercent_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.pop_viewpercent_label.text = self.pop_viewpercent_slider.level

  def pop_viewpercent_s_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.pop_viewpercent_s_label.text = self.pop_viewpercent_s_slider.level

  def pop_delete_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.remove_from_parent()




 
