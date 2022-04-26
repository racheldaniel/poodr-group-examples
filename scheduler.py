

from typing import Callable

class Runnable:
  def run(schedule):
    pass
  
  def is_ready():
     pass


class Job(Runnable):
  run: Callable = None
  is_hourly: bool = False

  def run(self, schedule):
    # some specific run thing
    pass
  def is_ready(self):
      pass


class Dispatcher:
  def __init__(self):
    self.jobs = []

  def add_runnable(self, runnable):
    self.jobs.append(runnable)

  def get_jobs(self):
    ready_jobs = []
    for job in self.jobs():
      if job.is_ready():
        ready_jobs.append(job)


class Scheduler:
  def __init__(self, dispatcher=None):
    self.dispatcher = dispatcher or Dispatcher()
    self.dispatcher.add_runnable(...)

  def trigger(self):
    for job in self.dispatcher.get_jobs():
      job.run()

"""
  def trigger_hourly():
    for job in self.jobs:
      if job.is_hourly:
        job.func()

  def trigger_daily():
    for job in self.jobs:
      if not job.is_hourly:
        job.func()
"""