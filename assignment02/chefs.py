#!/usr/bin/env python

import numpy as np

a_times = np.random.randint(100, size=10)
b_times = np.random.randint(100, size=10)
order =  unique(sorted(b_times, reverse=True))

queue_id = []
queue_time = []
time = 0

for o in order:
    chef_id = 0

    for t in b_times:

        if o == t:
            queue_id.append(chef_id)
            queue_time.append(time)
            time += a_times[chef_id] # a entry times
            continue

        else:
            chef_id += 1

print(queue_id)
print(queue_time)

