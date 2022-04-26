from enum import Enum


class Transport(Enum):
  BUS = "bus"
  PLANE = "plane"



class Guide():
  def __init__(self, **kwargs):
    self.name = kwargs["name"]
    self.location = kwargs["location"]


class Excursion:

  def __init__(self, **kwargs):
    self.guide = kwargs["guide"]
    self.transport = kwargs.get("transport") or self.default_transport()
    self.activity = kwargs.get("activity") or self.default_activity()
    self.activities =  kwargs.get("activities") 
    self.hours = kwargs.get("hours") or self.default_hours()
  
    self.post_initialize(kwargs)
  
  def total_price(self):
    pass

  def default_transport():
    raise NotImplementedError

  def default_activity():
    raise NotImplementedError

  def default_hours():
    raise NotImplementedError

  def post_initialize(**kwargs):
    pass


class MiniExcursion(Excursion):

  def default_activity():
    1

  def default_hours():
    2

  def default_transport():
    Transport.BUS


class AllDayExcursion(Excursion):

  def post_initialize(self, **kwargs):
      self.meals = kwargs["meals"]

  def default_activity():
    2

  def default_hours():
    2

  def default_transport():
    Transport.BUS



class OvernightExcursion(Excursion):
  def post_initialize(self, **kwargs):
      self.meals = kwargs["meals"]
      self.lodging = kwargs["lodging"]

  def default_activity():
    3

  def default_hours():
    24
  
  def default_transport():
    Transport.BUS



class WeeklongExcursion(Excursion):
  def post_initialize(self, **kwargs):
      self.meals = kwargs["meals"]
      self.lodging = kwargs["lodging"]
      self.transport = kwargs["transport"]

  def default_activity():
    10

  def default_hours():
    24 * 7
  
  def default_transport():
    Transport.PLANE

