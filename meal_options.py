from ortools.sat.python import cp_model
import numpy as np
from src.person import Person

NUM_MEALS = 5
MEAL_TYPES = ['breakfast', 'dinner', 'lunch']
REQUIRED_MEALS = [3, 3, 2,]
TARGET_CAL = 2_000
CAL_TOLERANCE = 400
TARGET_P = 70
P_TOLERANCE = 10





