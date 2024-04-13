# LogData Connection Analyzer 

This tool analyzes network connection logs to determine various statistics about the host connections. It parses files of a specific format, i.e., each line contains a space-separated text, formatted as `<unix_timestamp> <hostname> <hostname>`. The purpose of this tool is to understand links and relations between different hosts over different periods. 

## Features

1. **Time-bound Parsing:**
    Given a file name, an `init_datetime`, an `end_datetime` and a `Hostname`, it outputs a list of hostnames that were connected to the given host during that period.

2. **Unlimited Input Parser:**
    The tool is capable of parsing logs coming in real-time and provides updated statistics every hour. It gives the following information:
    * A list of hostnames connected to a given host
    * A list of hostnames that received connections from a given host
    * The hostname that generated the most connections in the last hour

## Getting Started

```bash
# clone the repository to your local machine
$ git clone https://github.com/mapecode/logdata-analyzer.git

# navigate to the project's directory
$ cd logdata-analyzer
```

## Usage



## Requirements



