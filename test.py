from datetime import datetime, timedelta

d = datetime(2021, 5, 31)
print(d)
d2 = d + timedelta(days=6)
print(d2)
print(d <= d)

st = "2021-05-31"
re = datetime.strptime(st, "%Y-%m-%d")
print(re)
