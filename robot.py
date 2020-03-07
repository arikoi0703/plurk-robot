# Plurk robot
# Plurk API list: https://www.plurk.com/API
# plurk-oauth: https://github.com/clsung/plurk-oauth
import re
import json
import urllib3
from plurk_oauth import PlurkAPI

# api.keys for authen
plurk = PlurkAPI.fromfile('./api.keys')
print(plurk.callAPI('/APP/Profile/getOwnProfile'))

# the user channel can get the new plurk for the user's timeline
# only new plurk, no re-plurk, response, or the other
# only fetch new messages from a given offset. You'll get offset when a response is returned.
# offset = -1, waiting for data to be posted.
# offset = -3, offset is wrong and you need to resync your data.
comet = plurk.callAPI('/APP/Realtime/getUserChannel')
comet_channel = comet.get('comet_server') + '&new_offset=%d'
json_re = re.compile('CometChannel.scriptCallback\((.+)\);\s')
new_offset = -1

while True:
	url_get = urllib3.PoolManager()
	request = url_get.request(comet_channel % new_offset)

# get new response, 



