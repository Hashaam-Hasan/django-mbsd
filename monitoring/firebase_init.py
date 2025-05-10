import firebase_admin
from firebase_admin import credentials, db, firestore, storage

# Initialize only once
if not firebase_admin._apps:
    cred = credentials.Certificate('E:/MyProjects/MBSD/fire_web/iot-web-c9f97-firebase-adminsdk-fbsvc-95ca970a67.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://iot-web-c9f97-default-rtdb.asia-southeast1.firebasedatabase.app'
    })




# Initialize Firestore
db = firestore.client()