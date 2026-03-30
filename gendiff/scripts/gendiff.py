import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')

    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )

    args = parser.parse_args()

    print(f"First file: {args.first_file}")
    print(f"Second file: {args.second_file}")
    print(f"Format: {args.format}")


if __name__ == '__main__':
    main()
