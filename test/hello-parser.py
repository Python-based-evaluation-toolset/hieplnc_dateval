def init_func(ctx):
    ctx['user']['collect'] = 0

def clean_func(ctx):
    pass

def map_func(ctx, line):
    line = line.strip()

    if 'part 1' in line:
        ctx['user']['collect'] = 1
        return None, None
    elif 'part 2' in line:
        ctx['user']['collect'] = 2
        return None, None

    if line.isdigit():
        return ctx['user']['collect'], line
    else:
        return None, None

def reduce_func(ctx, my_map):
    out = []
    for k, v in my_map.items():
        out.append([k, sum([int(i) for i in v])])
    return out
