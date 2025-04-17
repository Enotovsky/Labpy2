import re
from datetime import datetime

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

date_pattern = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'
dates = re.findall(date_pattern, text)

conv_dates = []
for day, month, year in dates:
    try:
        datetime.strptime(f"{day}.{month}.{year}", "%d.%m.%Y")
        conv_dates.append(f"{year}-{month}-{day}")
    except ValueError:
        pass

with open('dates.txt', 'w', encoding='utf-8') as file:
    for date in conv_dates:
        file.write(date + '\n')

sorted_dates = sorted(conv_dates, key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1]), int(x.split('-')[2])))

print(sorted_dates)