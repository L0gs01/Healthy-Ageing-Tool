from ._anvil_designer import Population_InitialSelectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Population_InitialSelection(Population_InitialSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  # def slider__change(self, **event_args):
  #   """This method is called when the slider is moved"""
  #   self.label_20.text = self.slider_20.level

  def pop_percent_slider_change(self, level, **event_args):
    """This method is called when the slider is moved"""
    self.percent_label.text = self.pop_percent_slider.level

 
  



 
