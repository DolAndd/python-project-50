#!/usr/bin/env python3
from gendiff.generate_diff.cli import parser_args
from gendiff.generate_diff.generate_diff import generate_diff


def main():
    args = parser_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
