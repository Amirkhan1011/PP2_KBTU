import datetime

today = datetime.datetime.now()

diff = today.microsecond - today.second 
print(diff)