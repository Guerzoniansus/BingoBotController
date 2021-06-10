import unittest
from parts.remote import RemoteControl

class IpTester(unittest.TestCase):

    def right_ip(self):
        """With this function the found IP address must be equal to the known IP address"""
        real_ip = '192.168.137.100'
        returned_ip = RemoteControl.get_ip_address('wlan0')
        self.assertEqual(real_ip, returned_ip)

if __name__ == '__main__':
    unittest.main()
