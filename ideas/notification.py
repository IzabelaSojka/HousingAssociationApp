from django.http import HttpResponse

registration_ids = ['cyPwQCcB4nJhQDTIoEzWYu:APA91bE2Jg6_aQH4zTlrDsGtfDFbxLLw68OY4TD0leNM0mKmLI7lDqv_0FF5U-4VXnbABKcCJnsikBBLWbKqzoOKO3by7UeXD8yY3_Z0fWVZLig9fcSQXKKONFWSKEjUv6idVXpXvvhU']

def send_notification(data, status):
    fcm_api = "AAAAz54T37A:APA91bGngLlZjyBOZJ3KGVsYuRgllzbZaxhMjVbhEa3FaFdTVV6q3zVv2VRnDdDdH2uvOSp5V6G3OLfkKr0AqXMBB5ZDQWIhkGlWwHQAobkauBg5wNSSSC8hrtFEYobhW0N8mBtcCujF"
    url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'key=' + fcm_api}

    if status == 'nieoplacone':
        payload = {
            "registration_ids": registration_ids,
            "priority": "high",
            "notification": {
                "body": data,
                "title": 'Minął termin płatności',
            }
        }
    else:
        payload = {
            "registration_ids": registration_ids,
            "priority": "high",
            "notification": {
                "body": data,
                "title": 'Zbliża się termin płatności',
            }
        }

def showFirebaseJS(request):
    data = 'importScripts("https://www.gstatic.com/firebasejs/9.15.0/firebase-app-compat.js");' \
           'importScripts("https://www.gstatic.com/firebasejs/9.15.0/firebase-messaging-compat.js"); ' \
           'var firebaseConfig = {' \
           '        apiKey: "AIzaSyDWdvXJNjEkbi9X96gF_kiwSgsbFK72zzs",' \
           '        authDomain: "housingassociationapp.firebaseapp.com",' \
           '        projectId: "housingassociationapp",' \
           '        storageBucket: "housingassociationapp.appspot.com",' \
           '        messagingSenderId: "891710332848",' \
           '        appId: "1:891710332848:web:0d51e28a88405c87e7c075",' \
           ' };' \
           'firebase.initializeApp(firebaseConfig);' \
           'const messaging=firebase.messaging();' \
           'messaging.onMessage((payload) => {' \
           '    console.log( payload);' \
           '    const notification=JSON.parse(payload);' \
           '    const notificationOption={' \
           '        body:notification.body,' \
           '        icon:notification.icon' \
           '    };' \
           '    self.registration.showNotification(payload.notification.title,notificationOption);' \
           '});'

    return HttpResponse(data, content_type="text/javascript")