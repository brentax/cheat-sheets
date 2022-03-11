# Arrays
values = [1, 2, 3]
values.append(4)
value_count = len(values)

min_value = min(values)
pairs = zip(values, values[1:]) # slicing and zipping

values.sort(reverse=True) # in place sort
pairs_sorted = sorted(pairs, key=lambda pair: pair[1], reverse=True)

# Queues/stacks
stack = []
stack.append("pushing")
popped = stack.pop()

# Strings
string_val = "hello world   "
string_val = string_val.strip()
first, second = string_val.split(" ") # tokenizing/splitting
print(", ".join(values)) # stringifying

# Numbers and parsing
ten = int("1010", 2)

# Conditionals
for line in lines:
    command, value = line.split(" ")
    if command == "forward":
        horizontal += int(value)
        depth += aim * int(value)
    elif command == "down":
        aim += int(value)
    elif command == "up":
        aim -= int(value)

# List comprehensions
values = [i for i in range(3)]
count_of_increases = sum([1 for prev, next in sum_pairs if prev < next])

# Dicts
from collections import defaultdict
d = defaultdict(lambda: 0)
d["key"] += 1

for k, v in d.items():
    print(str(k) + str(v))


# Loops
for val in values:
    print(val)

for i in range(10):
    print(i)

# Classes, Members, and Functions

# Unit Testing
import unittest
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

# Memoization
from functools import lru_cache
@lru_cache(maxsize=None)
def hello_world():
    print("hello world")

# JSON
import json
data = json.loads("[{\"hello\": \"world\", \"2\": true}, 84.3]")
print(data[0]["hello"])

# Reading a file
import os
file_path = os.path.join(os.path.dirname(__file__), "filename")
file = open(file_path, 'r')
lines = file.readlines()