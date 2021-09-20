import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from multiprocessing.pool import ThreadPool

from ping3 import ping
import xml.dom.minidom as xml
# import scapy.all as scapy
from scapy.layers.l2 import getmacbyip
import Context as Context


class Host(object):

    def __init__(self, ip_addr):
        self._ip_addr: str = ip_addr
        self._mac_addr: str = str()
        self._alive: bool = False
        self._range = None
        self._response_time: int = 0
        self._vendor: str = str()

    def set_ip(self, ip_addr):
        self._ip_addr = ip_addr

    def get_ip(self):
        return self._ip_addr

    def set_mac(self, mac_addr):
        self._mac_addr = mac_addr

    def get_mac(self):
        return self._mac_addr

    def set_range(self, ip_range):
        self._range = ip_range

    def get_range(self):
        return self._range

    def check_alive(self):
        response = ping(self._ip_addr)
        if response is None:
            self._alive = False
        else:
            self._mac_addr = getmacbyip(self._ip_addr)
            mac_addr = self._mac_addr
            Context.get_mv()
            vendor = Context.get_mv().get(mac_addr)
            while vendor == "" or vendor is None:
                mac_addr = mac_addr[:-1].upper()
                vendor = Context.get_mv().get(mac_addr)
            self._alive = True
            self._vendor = vendor
        return self._alive

    def is_alive(self):
        return self._alive

    def to_string(self):
        host_string = \
            "IP-address: " + self.get_ip() + \
            "\t Alive: " + str(self.is_alive())

        host_string += "\t MAC-address: "
        if self._mac_addr != "":
            host_string += self.get_mac()
        else:
            host_string += "N/A \t \t \t"

        host_string += "\t Vendor: "
        if self._vendor != "" and self._vendor is not None:
            host_string += self._vendor
        else:
            host_string += "N/A \t \t"

        host_string += "\t Response time: "
        if self.is_alive():
            host_string += str(self._response_time)[:7] + " ms"
        else:
            host_string += "N/A"

        return host_string
