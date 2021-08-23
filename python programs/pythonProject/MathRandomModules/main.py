import random

# Random sample doesnt allow duplication
print(random.sample(population=range(100),k=50))

# Random choices allow duplication
print(random.choices(population=range(100),k=50))