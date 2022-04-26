class Activity():
  def __init__(self, **kwargs) -> None:
      self.name = kwargs.get('name')
      self.hours = kwargs.get('hours')
      self.price = kwargs.get('price')
      self.description = kwargs.get('description')
    
  def get_price(self):
    return self.price


all_day_excursion = [
  ['sailboat ride', 3, '10.00', 'ride on a boat'],
  ['horseback ride', 2, '15.00', 'ride a horse'],
  ['museum', 5, '0.00', 'see some art']
]


class ActivitiesFactory():
  def __init__(self, activity_class: Activity) -> None:
      pass