from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def pop_viewpercent_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.pop_viewpercent_label.text = self.pop_viewpercent_slider.level

  def pop_viewpercent_s_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.pop_viewpercent_s_label.text = self.pop_viewpercent_s_slider.level

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item.delete()
    self.remove_from_parent()
