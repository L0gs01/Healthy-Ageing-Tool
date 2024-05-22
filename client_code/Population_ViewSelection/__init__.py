from ._anvil_designer import Population_ViewSelectionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Population_ViewSelection(Population_ViewSelectionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.pop_info.search()
    # Any code you write here will run before the form opens.
