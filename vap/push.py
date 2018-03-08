from pywebpush import webpush

webpush(
        subscription_info={
            "endpoint": "https://fcm.googleapis.com/fcm/send/cVWIU5ahCfg:APA91bEaaDWYqAKAwZoaSPSQxMujb9Dzd5bK_6VNZX-OJhJSKqjog48a3uEcEa7vLzqTQ9zN6KYhqg7KB1LnGZnghmY2cyiEkyTMky9BvTgyDpJ4pRa-8qFFqY0GzsmCLQM1a0QGZNjh",
            "keys": {
                "p256dh": "BAlEd7I2B7RllG8kx3fbWv5fnfIV4kt_W6LC62lIYH2vLAI49_mLARaM5zSktDr2eAQH33Dysh2FTPj0wzALxaU=",
                "auth": "0vw5-Iy1SES-dyrtwXpZng=="
            }},
        data="Mary had a little lamb, with a nice mint jelly",
        vapid_private_key="/Users/taojy123/workspace/SlowPay/vap/private_key.pem",
        # vapid_claims={
        #         "sub": "YourNameHere@example.org",
        #     }
    )
