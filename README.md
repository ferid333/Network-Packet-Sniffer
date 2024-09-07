# Network Packet Sniffer

A simple network packet sniffer built using Python, Tkinter, and Scapy. This application captures and displays network traffic, filtered by protocol (TCP, UDP, ICMP) in a user-friendly graphical interface.

## Features

- **Protocol Filtering**: Allows filtering captured packets by protocol (TCP, UDP, ICMP).
- **Real-Time Packet Display**: Shows network packet information in real-time.
- **Start/Stop Sniffing**: Ability to start and stop packet capturing with a button click.
- **Scrolled Text**: Captured packets are displayed in a scrollable text widget.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- [Scapy](https://scapy.net/)
  
To install Scapy, run the following command:
```bash
pip install scapy
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ferid333/Network-Packet-Sniffer.git
   cd network-packet-sniffer
   ```

2. Run the sniffer:
   ```bash
   python main.py
   ```

3. Use the GUI to start or stop sniffing. You can also filter packets by protocol (TCP, UDP, ICMP) by entering the desired protocol name in the input field.

## How It Works

- **Start Sniffing**: Click the "Start Sniffing" button to start capturing network packets. 
- **Stop Sniffing**: Click the "Stop Sniffing" button to stop the packet capturing process.
- **Protocol Filter**: Enter a protocol name (TCP, UDP, or ICMP) in the filter box to filter the captured packets based on the protocol.

### Example

Once sniffing starts, captured packets are displayed with their timestamp and summary in the text area. For example:
```
2024-09-07 12:34:56 - IP src=192.168.1.10 dst=192.168.1.1 TCP 80 > 4000 [SYN]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to open issues or submit pull requests to contribute to this project!
