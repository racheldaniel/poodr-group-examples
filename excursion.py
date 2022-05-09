from enum import Enum
from activity import (all_day_excursion, ActivitiesFactory)

class Transport(Enum):
  BUS = "bus"
  PLANE = "plane"



class Guide():
  def __init__(self, **kwargs):
    self.name = kwargs["name"]
    self.location = kwargs["location"]


class Excursion:

  def __init__(self, **kwargs):
    self.guide = kwargs.get("guide")
    self.transport = kwargs.get("transport") or self.default_transport()
    self.activity = kwargs.get("activity") or self.default_activity()
    self.activities = ActivitiesFactory.build(kwargs.get("activities_config", all_day_excursion))
    self.hours = kwargs.get("hours") or self.default_hours()

    self.post_initialize(**kwargs)
  
  def total_price(self):
    pass

  def default_transport(self):
    raise NotImplementedError

  def default_activity(self):
    raise NotImplementedError

  def default_hours(self):
    raise NotImplementedError

  def post_initialize(self, **kwargs):
    pass

class MiniExcursion(Excursion):

  def default_activity(self):
    1

  def default_hours(self):
    2

  def default_transport(self):
    Transport.BUS


class AllDayExcursion(Excursion):

  def post_initialize(self, **kwargs):
      self.meals = kwargs["meals"]

  def default_activity(self):
    2

  def default_hours(self):
    2

  def default_transport(self):
    Transport.BUS



class OvernightExcursion(Excursion):
  def post_initialize(self, **kwargs):
      self.meals = kwargs["meals"]
      self.lodging = kwargs["lodging"]

  def default_activity(self):
    3

  def default_hours(self):
    24
  
  def default_transport(self):
    Transport.BUS



class WeeklongExcursion(Excursion):
  def post_initialize(self, **kwargs):
      self.meals = kwargs["meals"]
      self.lodging = kwargs["lodging"]
      self.transport = kwargs["transport"]

  def default_activity(self):
    10

  def default_hours(self):
    24 * 7
  
  def default_transport(self):
    Transport.PLANE

