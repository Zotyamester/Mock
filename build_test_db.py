from mock import *

print('Check')
print('City count=%d' % City.query.count())
print('Question count=%d' % Question.query.count())

# Admin
# TODO

# Cities
with open('cities.txt', 'r', encoding='utf8') as f:
    existing = set()
    for line in f.read().split('\n')[:-1]:
        fields = line.split('\t')[1:]
        if fields[0] in existing:
            continue
        city = City(name=fields[0], latitude=int(float(fields[2])), longitude=int(float(fields[3])))
        db.session.add(city)
        existing.add(fields[0])

# Questions
for i in range(1, 12 + 1):
    db.session.add(Question(label='Kérdés %d' % i))

db.session.commit()
