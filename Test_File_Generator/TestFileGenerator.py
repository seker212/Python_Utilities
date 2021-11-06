from random import choice
from string import ascii_letters, digits, punctuation
from os.path import exists, splitext
from argparse import ArgumentParser, Namespace
from re import fullmatch
from typing import Any, Dict

def generate_text_file(filename: str, size: int) -> None:
    if exists(filename):
        raise FileExistsError
    with open(filename, 'w', encoding='ascii') as testfile:
        for _ in range(size):
            char = choice(ascii_letters + digits + punctuation+' \t')
            testfile.write(char)

def check_filename(filename: str) -> str:
    if exists(filename):
        i = 1
        name, ext = splitext(filename)
        while exists(filename):
            filename = name + f'({i})' + ext
            i += 1
    return filename

def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('size', type=str, help='The size of the generated test file. Accepted units: [B, KB, MB, GB] Example: 32KB')
    return parser.parse_args()

def prase_size(size_str: str) -> int:
    match = fullmatch(r"(\d+)([GMK]{0,1}B)", size_str)
    base_size = int(match.group(1))
    unit = match.group(2)
    if unit == 'B':
        return base_size
    elif unit == 'KB':
        return base_size * 1024
    elif unit == 'MB':
        return base_size * 1048576
    elif unit == 'GB':
        return base_size * 1073741824

def prase_namespace(namespace: Namespace) -> Dict[str, Any]:
    args = {}
    args['size'] = prase_size(namespace.size)
    return args

if __name__ == '__main__':
    size = prase_namespace(parse_arguments())['size']
    generate_text_file(check_filename('testfile.txt'), size)