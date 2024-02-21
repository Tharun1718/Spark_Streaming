# Spark Streaming Application with TCP Server

This repository contains two files:

1. `streaming_application.py`: This file contains the code for a Spark Streaming application that receives stock data from a TCP server, processes it, and prints filtered data in real-time.

2. `tcp_server.py`: This file contains the code for a TCP server that generates random stock data and sends it to the Spark Streaming application.

## Files

### `streaming_application.py`

This Python script sets up a Spark Streaming application to receive stock data from a TCP server, perform filtering based on previous maximum prices, and print the filtered data.

#### Usage

To run the streaming application:

```bash
python streaming_application.py
