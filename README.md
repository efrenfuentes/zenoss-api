# zenoss-api
Zenoss JSON API Python Library

Usage
=============

### List all devices in Zenoss
```python
from zenoss import ZenossAPI

zenoss = ZenossAPI('http://zenoss:8080/', 'admin', 'password')

for device in zenoss.get_devices()['devices']:
    print(device['name'])
