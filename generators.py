def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return 
        counter += 1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
    yield item
    seen.add(item)

def run_pipline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, list(distinct(items))):
        print(item)

run_pipline()

# sum(x*x for x in range(1, 10000001))

# sum(x for x in range(1001) if is_prime(x))

# from itertools import count, islice
# thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

# Zip
sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 23, 21, 19, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print("average =", (sun + mon) / 2)

# Zipping lists together and them producing metrics
for temps in zip(sunday, monday, tuesday):
    print(f"min = {min(temps):4.1f}, max={max(temps):4.1f}, average={sum(temps) / len(temps):4.1f}")  

from itertools import chain
temperatures = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatures))