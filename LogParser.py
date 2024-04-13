from datetime import datetime
from collections import defaultdict


class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.connections = defaultdict(list)
        self.incoming = defaultdict(list)

    def parse(self, init_datetime, end_datetime, hostname):
        init_timestamp = datetime.strptime(init_datetime, "%Y-%m-%d %H:%M:%S").timestamp() * 1000
        end_timestamp = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M:%S").timestamp() * 1000

        try:
            connected_hosts = set()
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.split(' ')
                    timestamp = int(data[0])
                    if data[1] == hostname:
                        if init_timestamp <= timestamp <= end_timestamp:
                            connected_hosts.add(data[2].rstrip())

            return list(connected_hosts)

        except FileNotFoundError:
            print("The given file does not exist.")
        except PermissionError:
            print("You do not have the right permissions to open this file.")
        except ValueError:
            print("There was an issue with converting the timestamp.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
