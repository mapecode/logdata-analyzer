import argparse
from LogParser import LogParser

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='parse log file.')
    args_parser.add_argument('-f', '--file', help='Input file name', required=True)
    args_parser.add_argument('-i', '--init_datetime', help='Start date time', required=True)
    args_parser.add_argument('-e', '--end_datetime', help='End date time', required=True)
    args_parser.add_argument('-host', '--hostname', help='Host name', required=True)
    args = args_parser.parse_args()

    parser = LogParser(args.file)

    print(parser.get_hostnames_connected(args.init_datetime, args.end_datetime, args.hostname))
