from intersight import intersight_api_client
from intersight.apis import equipment_device_summary_api

# Create an Intersight API Client instance
API_INSTANCE = IntersightApiClient(host="https://intersight.com/api/v1",private_key="/home/e.sebert/Documents/Python/DevNet/Scripts/Data\ Center\ and\ Compute\ Management/Intersight-SecretKey.txt",api_key_id="602e8e407564612d3359029a/602e8e407564612d3359029e/602fdd007564612d3350d159")

# Create an equipment device handle
D_HANDLE = equipment_device_summary_api.EquipmentDeviceSummaryApi(API_INSTANCE)

DEVICES = D_HANDLE.equipment_device_summaries_get().results

print('{0:35s}{1:40s}{2:13s}{3:14s}'.format("DN","MODEL","SERIAL","OBJECT TYPE"))
print('-'*105)

# Loop through devices and extract data
for DEVICE in DEVICES:
    print('{0:35s}{1:40s}{2:13s}{3:14s}'.format(DEVICE.dn,DEVICE.model,DEVICE.serial,DEVICE.source_object_type))
