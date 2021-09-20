import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from multiprocessing.dummy import Pool as ThreadPool
from Host import Host as Host


def ping_host(host):
    check_host = Host(host)
    check_host.check_alive()
    return host.is_alive()


class HostRange(object):

    def __init__(self, start: str, stop: str):
        self._start = start
        self._stop = stop

        self._mac_vendor: dict = {}

        self._hosts = []

        ip_address_start = self._start.split('.')
        ip_address_start = [int(i) for i in ip_address_start]

        ip_address_stop = self._stop.split('.')
        ip_address_stop = [int(i) for i in ip_address_stop]

        if len(ip_address_start) != 4 or len(ip_address_stop) != 4:
            print("Invalid IP address input")

        for i in range(3):
            if ip_address_start[i] > 255 or ip_address_stop[i] > 255 or ip_address_start[i] > ip_address_stop[i]:
                print("Invalid IP range")

        for a in range(ip_address_start[0], ip_address_stop[0] + 1):
            for b in range(ip_address_start[1], ip_address_stop[1] + 1):
                for c in range(ip_address_start[2], ip_address_stop[2] + 1):
                    for d in range(ip_address_start[3], ip_address_stop[3] + 1):
                        current_host = Host((str(a) + "." + str(b) + "." + str(c) + "." + str(d)))
                        current_host.set_range(self)
                        self._hosts.append(current_host)

    def ping_hosts(self):
        threads_amount = 30
        pool = ThreadPool(threads_amount)
        pool.map(Host.check_alive, self._hosts)
        pool.close()
        pool.join()

    def get_mac_addresses(self):
        pass

    def get_hosts(self):
        return self._hosts
