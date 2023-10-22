use = 0
for xx in dir():
    exec(f'use += int(sys.getsizeof({xx}))')
Output('used memory: ' + str(use) + ' bytes, number of variables: ' + str(len(dir())))
