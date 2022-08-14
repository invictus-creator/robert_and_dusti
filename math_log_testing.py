import math
large = int(input("blah: "))
small = int(input("gogo: "))
max_tries = math.ceil(math.log2(large-small))
print(max_tries)