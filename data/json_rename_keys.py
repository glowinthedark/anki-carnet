#!/usr/bin/env python3

import json
from pathlib import Path
from argparse import ArgumentParser

def strip_dots(obj):
    if isinstance(obj, dict):
        return {k.rstrip('.'): strip_dots(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [strip_dots(item) for item in obj]
    return obj

parser = ArgumentParser()
parser.add_argument('--glob', default='*.json')
args = parser.parse_args()

for path in Path('.').glob(args.glob):
    data = json.loads(path.read_text(encoding='utf-8'))
    path.write_text(
        json.dumps(strip_dots(data), ensure_ascii=False, separators=(',', ':')),
        encoding='utf-8'
    )
    print(f"✓ {path.name}")