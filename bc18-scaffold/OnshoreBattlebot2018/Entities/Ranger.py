import random
import sys
import traceback

from .IRobot import IRobot

class Ranger(IRobot):
	def __init__(self, gameController):
		self.gameController = gameController