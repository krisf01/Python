from itertools import combinations

example_set = {-1,4,6}
super_set = set()

for x in range(len(example_set)):
  for perm in combinations(example_set,x+1):
    super_set.add(perm)

super_set.add(())
print(super_set,'length:',len(super_set))
