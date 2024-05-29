# Guide to Using the Python AdMob Server Side Verifying (SSV)

Based on the params sent by Google Admob, we will get the values ​​of **data_to_verify**, **signature** and **key_id**.

Example callback params:
```
/callback?ad_network=54....55&ad_unit=12...90&reward_amount=1&reward_item=Token&timestamp=17....37&transaction_id=12...89&user_id=12..21&signature=ME....J8vfw&key_id=33...09
```

Code for verify:
```python
from admob_ssv import verify_admob_request

data_to_verify = "ad_network=545.......9855&ad_unit=12...90&reward_amount=1&reward_item=Token&timestamp=17...73&transaction_id=12...89&user_id=12..21"
signature = "ME....J8vfw"
key_id = "33...09"

is_valid = verify_admob_request(data_to_verify, key_id, signature)
print(is_valid)
```
