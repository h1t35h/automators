import requests
import collections
import xml.etree.ElementTree as ElementTree

OTHER = 'OTHER'
MOBILE = 'MOBILE'

Device = collections.namedtuple('Device', ['mac', 'ip_address', 'device_type'])


def get_device_type(device_mac):
    if device_mac == 'e0:5f:45:5f:45:13':
        return MOBILE
    else:
        return OTHER


def get_connected_devices():
    devices_xml = requests.get('http://192.168.10.1/Status/wifi_assoc.asp')
    devices_root = ElementTree.fromstring(devices_xml.text)
    connected_devices = []
    for device in devices_root.findall('assoc'):
        device_mac = device.find('mac').text
        device_ip = device.find('ip_address').text
        device_type = get_device_type(device_mac)
        connected_devices.append(Device(mac=device_mac, ip_address=device_ip, device_type=device_type))
    return connected_devices


if __name__ == '__main__':
    wifi_connected_devices = get_connected_devices()
    for device in wifi_connected_devices:
        print(device)
