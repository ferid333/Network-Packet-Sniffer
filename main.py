import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff, get_if_list, TCP, UDP, ICMP
import threading
import time

class PacketSniffer:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Packet Sniffer")
        self.root.geometry("800x600")
        
        self.filter_protocol = tk.StringVar()
        self.running = False
        
        self.setup_widgets()
        
    def setup_widgets(self):
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        tk.Label(filter_frame, text="Filter by Protocol:").pack(side=tk.LEFT, padx=5)
        filter_entry = tk.Entry(filter_frame, textvariable=self.filter_protocol)
        filter_entry.pack(side=tk.LEFT, padx=5)
        start_button = tk.Button(filter_frame, text="Start Sniffing", command=self.start_sniffing)
        start_button.pack(side=tk.LEFT, padx=5)
        
        stop_button = tk.Button(filter_frame, text="Stop Sniffing", command=self.stop_sniffing)
        stop_button.pack(side=tk.LEFT, padx=5)

        self.packet_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=25)
        self.packet_display.pack(fill=tk.BOTH, expand=True)

    def start_sniffing(self):
        if not self.running:
            self.running = True
            self.sniff_thread = threading.Thread(target=self.sniff_packets)
            self.sniff_thread.start()

    def stop_sniffing(self):
        if self.running:
            self.running = False
            self.sniff_thread.join()

    def sniff_packets(self):
        iface = 'Wi-Fi'
        
        sniff(prn=self.process_packet, stop_filter=lambda x: not self.running, iface=iface, lfilter=self.lfilter)

    def lfilter(self, packet):
        protocol = self.filter_protocol.get().lower()
        if protocol == "":
            return True
        if protocol == "tcp" and TCP in packet:
            return True
        if protocol == "udp" and UDP in packet:
            return True
        if protocol == "icmp" and ICMP in packet:
            return True
        return False

    def process_packet(self, packet):
        if not self.running:
            return

        packet_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        packet_summary = f"{packet_time} - {packet.summary()}\n"
        self.packet_display.insert(tk.END, packet_summary)
        self.packet_display.see(tk.END)
root = tk.Tk()
app = PacketSniffer(root)
root.mainloop()
