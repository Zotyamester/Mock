from mock import *

# Admin
# TODO

# Cities
with open('cities.txt', 'r', encoding='utf8') as f:
    for line in f.read().split('\n')[:-1]:
        fields = line.split('\t')[1:]
        city = City(name=fields[0], latitude=int(float(fields[2])), longitude=int(float(fields[3])))
        db.session.add(city)

# Questions
for i in range(1, 12 + 1):
    db.session.add(Question(label='Kérdés %d' % i))

db.session.commit()
