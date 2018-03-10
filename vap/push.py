#coding=utf8
from urlparse import urlparse

import os

import requests
from py_vapid import Vapid
from pywebpush import webpush, WebPusher

# webpush(
#         subscription_info={
#             "endpoint": "https://fcm.googleapis.com/fcm/send/duHjPCRYDC0:APA91bGciB7SJPPc2lEVynONxSWtdT-9GQltSDxcPPlA63RYzx5SNnsZth6bplHFsNq2KIwKds0sTT6DDZv-FenlWvCeWfJ0nv63ujxnXO5OBf-XTkd2hGcehc3s4gZjLwVJqVHSJK2X",
#             "keys": {
#                 "p256dh": "BDzxFBM5d_L5LSSYFpyyerRyjKRxUOEdrVP7bG69HTt-gedRHzdOzCul2jDKaNWR9wrcimbR9RGnolmCu7XsuO0=",
#                 "auth": "Q8xHPxVA8AmMJSjSkp_IEQ=="
#             }
#         },
#         data=u'哈哈',
#         vapid_private_key="/Users/taojy123/workspace/SlowPay/vap/private_key.pem",
#         vapid_claims={
#             "sub": "mailto:taojy123@163.com"
#         }
#     )



requests_session = requests.Session()
requests_session.proxies = {'https': '127.0.0.1:1087'}

subscription_info = {
    "endpoint": "https://fcm.googleapis.com/fcm/send/d1-ZTtIbxCM:APA91bEbQ7HE8u_XDLNKQZJ4bqiey_EiGZjZcjauv49KU-1uF0CEukKYgcWDWTxhSByJuDLmZOwMl8xmK2YkCobB81AwCexNW4bw9FVCkcUX7K-meghbZ5UyGe2VS1jQ_uzE6n64i4xK",
    "keys": {
        "p256dh": "BK7h-R0UgDeT89jhWi76-FlTtlEr3DbVBnrr34qmK91Husli_Fazu7vo7kW1mg9F_qhNzrs2glbrc6wfqGFsXks=",
        "auth": "CyOHiGNXPcT5Slo9UMx2uA=="
    }
}
data = 'aaaaaa'
vapid_private_key = PRIVATE_KEY = '''
MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQg2xyYpqQhOaIdSbqH
UwM3+ySvF47MoJyAFUNaHM7g/zOhRANCAAT554ztzCpjiIFOxNfEIicSzNPOZTIB
Y1+CGl+LDfM5RlUNERFdfZYRqMmwvX7ydq7UiASkspWqdVVKZnLCzPD3  
'''.strip()
vapid_claims = {
    "sub": "mailto:taojy123@163.com"
}

vapid_headers = None
if vapid_claims:
    if not vapid_claims.get('aud'):
        url = urlparse(subscription_info.get('endpoint'))
        aud = "{}://{}".format(url.scheme, url.netloc)
        vapid_claims['aud'] = aud
    if os.path.isfile(vapid_private_key):
        vv = Vapid.from_file(private_key_file=vapid_private_key)  # pragma no cover
    else:
        vv = Vapid.from_string(private_key=vapid_private_key)
    vapid_headers = vv.sign(vapid_claims)

result = WebPusher(subscription_info, requests_session).send(data, vapid_headers)

print result.text
