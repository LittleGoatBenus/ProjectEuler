values = []

for a in range(2,101,1):

    for b in range(2,101,1):

        value = a**b


        values.append(value)

sorted = sorted(values)

nodups = []

for value in sorted:
    if value not in nodups:
        nodups.append(value)
