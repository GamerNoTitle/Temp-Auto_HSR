import requests
import json
ver_info = requests.get('https://api-launcher-static.mihoyo.com/hkrpg_cn/mdk/launcher/api/resource?channel_id=1&key=6KcVuOkbcqjJomjZ&launcher_id=33&sub_channel_id=2', timeout=60).text
version = json.loads(ver_info)['data']['game']['latest']['version']

if version != '2.1.0':
    print(f'Current Version: {version}')
    with open('hsr.apk', 'wb') as f:
        f.write(requests.get('https://api-takumi.mihoyo.com/event/download_porter/link/hkrpg_cn/official/android_default').content)