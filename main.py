import firebase_admin
from firebase_admin import credentials, messaging

# Initializing the SDK
# default_app = firebase_admin.initialize_app()

# cred = credentials.RefreshToken('path/to/refreshToken.json')
cred = credentials.Certificate('C:\\Users\\ASUS\\Documents\\DrPaw\\FCMBackend\\serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)


# This registration token comes from the client FCM SDKs.
# registration_token = 'c_RjnD-ZQIuBegUTYeAE3K:APA91bE-oGyhi3PmBOUN9dLBDDYiJcN_v7IbYPEtztTB0LeIptQNpWtUmLDWTPaubF4BQ6MM_MKSCd_kPoay85SEkM_ahxcnbJJ_CqGggrN4Um7lC1XGZZVD0AWeXQzvnGiVmaBv7jkz'
topic = 'test'

message = messaging.Message(
    notification=messaging.Notification(
        title='Notification',
        body='Hey!',
    ),
    # token=registration_token,
    topic=topic,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
