# LogData Connection Analyzer 

This tool analyzes network connection logs to determine various statistics about the host connections. It parses files of a specific format, i.e., each line contains a space-separated text, formatted as `<unix_timestamp> <hostname> <hostname>`. The purpose of this tool is to understand links and relations between different hosts over different periods. 

## Use Cases

### **Time-bound Parsing**
    
Given a file name, an `init_datetime`, an `end_datetime` and a `Hostname`, it outputs a list of hostnames that were connected to the given host during that period.

This use case is solved by the method `get_hostnames_connected` from [LogParser](/src/LogParser.py) that returns the sum of result (connections made plus connection received) from the main function get_hostname_stats.

The use case can be tasted with [parser.py](/src/parser.py)

### **Unlimited Input Parser**

The tool is capable of parsing logs coming in real-time and provides updated statistics every hour. It gives the following information:
* A list of hostnames connected to a given host
* A list of hostnames that received connections from a given host
* The hostname that generated the most connections in the last hour, with the following assumption:
  * This implies that the "most connected host" is identified only within the outgoing connections made by that given hostname and not across all the hosts present in the log for the last hour. So, for example, if a execution with "hostname": "Host1", we are only checking the connections made by "Host1" to other hosts, and identifying which host was connected to the most by "Host1" during the given hour.

Other assumptions about the file:
* The log file doesn't reset or does not get rotated.
* No log lines are being removed or overwritten.
* All new entries are always appended at end of file.
* The timestamps in the log file are in order.

These assumptions are important to use the last position processed of the file in the executions scheduled.

This use case would be solved with an Airflow DAG. [Input Parser](/dags/input_parser.py) is a proposal with the following capabilities:
- The main function, `get_hostname_stats` method, from [LogParser](/src/LogParser.py), returns the necessary values.
- The DAG will employ a variable for the last position of the file to prevent processing the entire file during each execution.
- The DAG will use the first execution's current timestamp as the execution date. The subsequent execution date will be one hour later than the execution date, and this next execution value will serve as the execution date during the DAG's next execution.
- The results will be pushed using XCOM as a dictionary with these keys: `connections_made`, `connections_received`, `most_connected_host`.



