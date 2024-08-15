def init_func(ctx):
    ctx['user']['collect'] = None
    ctx['user']['file'] = None
    ctx['user']['mapper'] = map_func_1
    ctx['user']['reducer'] = reduce_func_1

def clean_func(ctx):
    pass

def map_func(ctx, line):
    return ctx['user']['mapper'](ctx, line)

def reduce_func(ctx, val):
    return ctx['user']['reducer'](ctx, val)

def map_func_1(ctx, line):
    line = line.strip()

    if 'input' in line:
        ctx['user']['file'] = 'input'
        return None, None
    elif 'output' in line:
        ctx['user']['file'] = 'output'
        return None, None

    if 'part 1' in line:
        ctx['user']['collect'] = 1
        return None, None
    elif 'part 2' in line:
        ctx['user']['collect'] = 2
        return None, None

    if line.isdigit():
        collect = ctx['user']['collect']
        file = ctx['user']['file']
        return  f"{collect},{file}", line
    else:
        return None, None

def map_func_2(ctx, line):
    return line[0], {line[1]: line[2]}

def reduce_func_1(ctx, val):
    out = []
    for k, v in val.items():
        collect = k.split(',')[0]
        file = k.split(',')[1]
        out.append([collect,file,sum([int(i) for i in v])])
    ctx['user']['mapper'] = map_func_2
    ctx['user']['reducer'] = reduce_func_2
    ctx['loop'] = True
    return out

def reduce_func_2(ctx, val):
    out = [['collect', 'input', 'output']]
    for k, v in val.items():
        input = None
        output = None
        for item in v:
            if 'input' in item:
                input = item['input']
            if 'output' in item:
                output = item['output']
        out.append([k, input, output])
    return out