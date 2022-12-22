def try_operations(operations, numbers, wontdo):
    for opm in operations.copy():
        op = operations[opm]
        for wd in wontdo:
            if wd in op.split(' '):
                wontdo.append(opm)
                break
        else:
            try:
                v = eval(op, numbers)
                numbers[opm] = v
                del operations[opm]
            except:
                pass

def make_function(operations, numbers):
    changed = False
    for opm in operations:
        new_op = []
        for v in operations[opm].split(' '):
            if v in numbers:
                new_op.append(str(numbers[v]))
            elif v in operations:
                new_op += ['(', operations[v], ')']
            else:
                new_op.append(v)
        new_op = ' '.join(new_op)
        if new_op != operations[opm]:
            changed = True
            operations[opm] = new_op
    return changed

def start(line, lines):
    operations = {}
    numbers = {}
    for r in lines:
        cmd = r.split(': ')
        if cmd[1].isnumeric():
            numbers[cmd[0]] = int(cmd[1])
        else:
            operations[cmd[0]] = cmd[1]
    r = operations['root'].split(' ')
    operations['root'] = r[0] + " == " + r[2]
    wontdo = ['humn']
    del numbers['humn']
    while True:
        for op in operations:
            if not op in wontdo:
                break
        else:
            break
        try_operations(operations, numbers, wontdo)
    while make_function(operations, numbers):
        pass
    root_op = operations['root'].replace(' ', '')
    print(root_op) # Interestingly, this question seems to be ALOT easier than 
    # it is presented, at this point we see humn is only used once in the function.
    comparator = root_op.replace('==', '<') # Let's do a binary search in that case!
    i = 0
    min_i = -99999999999999999
    max_i =  99999999999999999
    new_direction = False
    while True:
        i = int((min_i + max_i)/2.0) # Seems like it's always integers
        if eval(root_op, {'humn': i}):
            print(i)
            break
        if eval(comparator, {'humn': i}):
            if new_direction:
                max_i = i
            else:
                min_i = i
        else: # Smaller
            if not new_direction:
                max_i = i
            else:
                min_i = i
        if abs(abs(i) - 99999999999999999) < 1000:
            print(abs(i) - 99999999999999999)
            # Switch direction if you get too close to max bound.
            i = 0
            min_i = -99999999999999999
            max_i =  99999999999999999
            new_direction = True
