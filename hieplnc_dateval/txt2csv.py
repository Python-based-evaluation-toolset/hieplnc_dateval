import argparse
import csv, sys, os

global ctx
ctx = {
    'loop': True, # repeat map-reduce process
    'dat': [],
    'user': {}, # user-space states
}

def txt2csv(args=None):
    parser = argparse.ArgumentParser(description='Text to csv2')
    parser.add_argument("--engine", help="python consists of parser engine.", required=True)
    parser.add_argument("--logs", help="text folder holds log data.", required=True)
    parser.add_argument("--csvout", help="output csv file.")
    parser.add_argument("--stdout", help="write to stdout", action=argparse.BooleanOptionalAction)
    args = parser.parse_args(args)

    engine = {}
    with open(args.engine, 'r') as file:
        contents = file.read()
        exec(contents, engine)

    files = os.listdir(args.logs)
    for file in files:
        with open(f'{args.logs}/{file}', 'r') as f:
            ctx['dat'].append(f'{args.logs}/{file}')
            ctx['dat'] = ctx['dat'] + f.readlines()

    engine['init_func'](ctx)

    while ctx['loop']:
        ctx['loop'] = False
        
        # map state
        m_temp = []
        for line in ctx['dat']:
            key, val = engine['map_func'](ctx, line)
            if key is not None:
                m_temp.append({key: val})
        # reduce state
        r_temp = {}
        for item in m_temp:
            for k, v in item.items():
                if k not in r_temp:
                    r_temp[k] = []
                r_temp[k].append(v)
        ctx['dat'] = engine['reduce_func'](ctx, r_temp)

    engine['clean_func'](ctx)

    if not args.stdout:
        with open(args.csvout, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in ctx['dat']:
                writer.writerow(row)
    else:
        writer = csv.writer(sys.stdout)
        for row in ctx['dat']:
            writer.writerow(row)


if __name__ == "__main__":
    txt2csv()