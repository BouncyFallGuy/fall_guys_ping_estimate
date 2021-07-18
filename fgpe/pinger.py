# Standard Library
import subprocess
from enum import Enum
from typing import Optional
from statistics import mean


class PingConnect(Enum):
    CONNECTED = 1
    NOT_CONNECTED = 2


class Stats:
    def __init__(self):
        self.pings = []

    def add(self, time: int):
        self.pings.append(time)

    def stats_string(self):
        return (f'Ping={self.pings[-1]}ms, '
                f'Max Ping={max(self.pings)}ms, '
                f'Min Ping={min(self.pings)}ms, '
                f'Avg Ping={float(mean(self.pings)):.2f}ms')


class Pinger:
    def __init__(self, ip_address: str):
        if ':' in ip_address:
            self.ip_address, self.port = ip_address.split(':')
        else:
            self.ip_address = ip_address
            self.port = None
    
    def get_ping_time(self) -> tuple[PingConnect, Optional[int]]:
        response = subprocess.run(
            ['ping', '-n', '1', '-w', '1000', self.ip_address],
            capture_output=True,
            encoding='ascii'
            )
        if response.returncode != 0:
            return PingConnect.NOT_CONNECTED, None
        
        for line in response.stdout.splitlines():
            if 'Reply from' in line:
                time_equals = line.strip().split()[4]
                time_ms = time_equals.split('=')[1]
                time = int(time_ms[:-2])
                break
        else:
            return PingConnect.NOT_CONNECTED, None
        
        return PingConnect.CONNECTED, time
