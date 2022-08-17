#! /usr/bin/env python
import sys
import acitoolkit.acitoolkit as aci

APIC_URL = 'https://sandboxapicdc.cisco.com'
USERNAME = 'admin'
PASSWORD = '!v3G@!4@Y'

# Login to APIC
SESSION = aci.Session(APIC_URL, USERNAME, PASSWORD)
RESP = SESSION.login()
if not RESP.ok:
    print('Could not login to APIC')
    sys.exit()

TENANTS = aci.Tenant.get(SESSION)
print('#################')
print('List all tenants')
print('#################')

for Tenant in TENANTS:
        print(Tenant.name)