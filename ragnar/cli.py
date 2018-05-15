import argparse
import sys


def build_kernel(args):
    print("foo")


def rekernel_rootfs(args):
    pass


def bisect_lava(args):
    pass


def cli(args):
    parser = argparse.ArgumentParser(
        description="Linaro build and bisect tool",
    )
    subparsers = parser.add_subparsers()

    parser_build_kernel = subparsers.add_parser(
        'build-kernel',
        help='Build a kernel for a given architecture or board',
    )
    parser_build_kernel.add_argument(
        '--clean',
        '-c',
        help="Clean output and staging directory before building"
    )
    parser_build_kernel.add_argument(
        '--machine',
        '-m',
        help="Machine name to build: [hikey|db410c|x15]"
    )
    parser_build_kernel.set_defaults(func=build_kernel)

    parser_rekernel_rootfs = subparsers.add_parser(
        'rekernel-rootfs',
        help='Rebuild and then replace the kernel in a given rootfs',
    )
    parser_rekernel_rootfs.set_defaults(func=rekernel_rootfs)

    parser_bisect_lava = subparsers.add_parser(
        'bisect-lava',
        help='Bisect a kernel using an OE image and a lava job',
    )
    parser_bisect_lava.set_defaults(func=bisect_lava)

    if len(args) == 0:
        parser.print_help()
        parser.exit()

    parsed_args = parser.parse_args(args)
    parsed_args.func(parsed_args)


def main():
    cli(sys.argv[1:])
