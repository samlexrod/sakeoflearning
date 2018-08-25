str = 'Samuel starts with Sa'
print(str.startswith('Sa')) #Out[1]: True
print(str.startswith('Sa', 2, 4)) #Out[1]: False
print(str.startswith('Sa', -2, len(str))) #Out[1]: True