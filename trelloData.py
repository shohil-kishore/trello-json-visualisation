from urllib.request import urlopen
import json

# Reading in the JSON generated by Trello's API.
student1Data = urlopen("https://trello.com/b/uaCT48b5/chronospatial.json").read()

# Data is in bytes, needs to be decoded so it's JSON serializable.
student1Decode = student1Data.decode("utf-8")

# Backslashes from the data need to be removed.
