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

  def slider_1_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_1.text = self.slider_1.level

  def slider_2_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_2.text = self.slider_2.level

  def slider_3_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_3.text = self.slider_3.level

  def slider_4_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_4.text = self.slider_4.level

  def slider_5_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_5.text = self.slider_5.level

  def slider_6_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_6.text = self.slider_6.level

  def textbox_6_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.label_6.text = self.textbox_6.text

  def slider_8_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_8.text = self.slider_8.level

  def slider_9_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_9.text = self.slider_9.level

  def dropdown_10_change(self, **event_args):
    """This method is called when an item is selected"""
    self.label_10.text = self.dropdown_10.selected_value

  def slider_11_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_11.text = self.slider_11.level

  def slider_12_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_12.text = self.slider_12.level

  def slider_13_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_13.text = self.slider_13.level

  def slider_13_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_13.text = self.slider_13.level

  def slider_14_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_14.text = self.slider_14.level

  def slider_15_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_15.text = self.slider_15.level

  def slider_16_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_16.text = self.slider_16.level

  def slider_17_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_17.text = self.slider_17.level

  def slider_18_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_18.text = self.slider_18.level

  def slider_19_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_19.text = self.slider_19.level

  def slider_20_change(self, **event_args):
    """This method is called when the slider is moved"""
    self.label_20.text = self.slider_20.level

  def dropdown_10_change(self, **event_args):
    """This method is called when an item is selected"""
    self.label_10.text = self.dropdown_10.selected_value

  def textbox_7_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
