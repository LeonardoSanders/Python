from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('Asia/Tokyo'))
print(data)