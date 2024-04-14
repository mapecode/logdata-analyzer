from datetime import datetime
from collections import defaultdict, Counter


class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.connections = defaultdict(list)
        self.incoming = defaultdict(list)

    def get_hostname_stats(self, init_datetime, end_datetime, host, file_last_position=0):
        connections = defaultdict(list)
        incoming = defaultdict(list)

        try:
            start = datetime.strptime(init_datetime, "%Y-%m-%d %H:%M:%S").timestamp() * 1000
            end = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M:%S").timestamp() * 1000

            with open(self.file_name, "r") as file:
                file.seek(file_last_position)
                for line in file:
                    parts = line.split(" ")
                    timestamp = int(parts[0])

                    if timestamp < start:
                        # skip previous timestamps
                        continue
                    elif timestamp > end:
                        # skip post timestamps
                        break
                    else:
                        if start <= timestamp < end:
                            source, dest = parts[1], parts[2].rstrip()
                            if source == host:
                                connections[source].append(dest)
                            if dest == host:
                                incoming[dest].append(source)

            outgoing_cnt = Counter(connections[host])
            most_connected_host = outgoing_cnt.most_common(1)[0][0] if outgoing_cnt else 'No connections'

            results = {
                "connections_made": connections[host],
                "connections_received": incoming[host],
                "most_connected_host": most_connected_host
            }

            return results, \
                file.tell()  # returning last position in the file processed

        except FileNotFoundError:
            print("The given file does not exist.")
        except PermissionError:
            print("You do not have the right permissions to open this file.")
        except ValueError:
            print("There was an issue with converting the timestamp.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def get_hostnames_connected(self, init_datetime, end_datetime, host):
        results, _ = self.get_hostname_stats(init_datetime, end_datetime, host)

        return results['connections_made'] + results['connections_received']
