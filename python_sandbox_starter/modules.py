# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
from datetime import date as dt
from time import time
import camelcase
import validator as vd

# today = datetime.date.today()
today = dt.today()
now = time()

# print(today)
# print(now)

camel = camelcase.CamelCase()
text = 'hello world'
print(camel.hump(text))

myemail = '1212|estcom'
if vd.validate_email(myemail):
  print(True)
else:
  print(False)