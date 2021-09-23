import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore 

#use a service account
cred = credentials.Certificate('scotts-totts-firebase-ce5beb7102d0.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
#creating a new collection and a document
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})
#creating another document to the 'users' collection
doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})
# verify that I added data to the cloud firestore
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')


print("Firebase") 
