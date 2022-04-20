#Mac: >>> pip3 install pandas
#Windows: >>> python3 -m pip install pandas

import pandas as pd

data_set = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

data = pd.DataFrame(data_set)

print(data)

