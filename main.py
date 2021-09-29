import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore 

#use a service account
cred = credentials.Certificate('trivia-web-app-651a1-firebase-adminsdk-6cgid-564cb084e2.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
#creating a new collection and a document
'''
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

'''
print("Firebase") 

doc_ref = db.collection(u'test').document(u'bob')

doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')


data = {
    "id" : 4,
    "email" : "yebassabiya@gmail.com",
    "married" : False
}

db.collection("users").document("biya_yebassa").set(data)

j_mname = {
    "middle name" : "Frank",
    "id" : 1,
    "married" : False,
    "email" : "jbetzsold@gmail.com"
}

db.collection("users").document("josh_betzsold").set(j_mname)


