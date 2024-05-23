from ._anvil_designer import Population_EditSelectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Population_EditSelection(Population_EditSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def pop_percent_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.percent_label.text = self.pop_percent_slider.level

  def pop_percentsuccess_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.percentsuccess_label.text = self.pop_percentsuccess_slider.level
