from clint.textui import puts, indent, colored
import shutil, errno
from clint import arguments
import os

args = arguments.Args()

def new(target=None):
    base_path = os.path.dirname(os.path.abspath('__file__'))
    src = os.path.join(base_path, 'template/')
    dst = os.path.join(base_path, target)
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


if args.get(0) == 'new':
    dst = args.get(1)
    if dst:
        new(dst)
    else:
        raise
