from clint.textui import puts, indent, colored
import shutil, errno
from clint import arguments
import os

args = arguments.Args()

def new(target=None):
    base_path = os.path.dirname(os.path.realpath(__file__))
    src = os.path.join(base_path, 'template')
    dst = os.path.join(os.path.dirname(os.path.abspath('__file__')),target)
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)

def main():
    if args.get(0) == 'new':
        dst = args.get(1)
        if dst:
            new(dst)

if __name__ == '__main__':
    main()
