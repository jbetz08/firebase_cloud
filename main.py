import firebase_admin
from firebase_admin import credentials
from firebase_admin import firebase 

#use a service account
cred = credentials.Certificate('scotts-totts-firebase-ce5beb7102d0.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


print("Firebase") 
