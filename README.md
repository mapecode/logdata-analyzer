# LogData Connection Analyzer 

This tool analyzes network connection logs to determine various statistics about the host connections. It parses files of a specific format, i.e., each line contains a space-separated text, formatted as `<unix_timestamp> <hostname> <hostname>`. The purpose of this tool is to understand links and relations between different hosts over different periods. 

## Capabilities

### **Time-bound Parsing**
    
Given a file name, an `init_datetime`, an `end_datetime` and a `Hostname`, it outputs a list of hostnames that were connected to the given host during that period.

### **Unlimited Input Parser**

The tool is capable of parsing logs coming in real-time and provides updated statistics every hour. It gives the following information:
* A list of hostnames connected to a given host
* A list of hostnames that received connections from a given host
* The hostname that generated the most connections in the last hour, with the following assumption:
  * This implies that the "most connected host" is identified only within the outgoing connections made by that given hostname and not across all the hosts present in the log for the last hour. So, for example, if a execution with "hostname": "Host1", we are only checking the connections made by "Host1" to other hosts, and identifying which host was connected to the most by "Host1" during the given hour.


## Getting Started

```bash
# clone the repository to your local machine
$ git clone https://github.com/mapecode/logdata-analyzer.git

# navigate to the project's directory
$ cd logdata-analyzer
```

## Usage



## Requirements



