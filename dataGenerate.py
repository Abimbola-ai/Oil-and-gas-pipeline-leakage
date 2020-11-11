# import relevant packages
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from faker import Faker

# initialize faker
fake = Faker()
# Detecting external corrosion
timestamp = []
length = []
Temperature = []
Humidity = []
pipewall_thickness = []
corrosion_level = ['Minor', 'Medium', 'Severe']