import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore 

#use a service account
cred = credentials.Certificate('trivia-web-app-651a1-firebase-adminsdk-6cgid-564cb084e2.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
#creating a new collection and a document

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

django_resource = {
    "url" : "https://docs.djangoproject.com/en/3.2/intro/tutorial01/"
}

db.collection("resources").document("django_resource").set(django_resource)


jacob_morgan = {
    "middle name" : "David",
    "married" : True,
    "candy" : True
}

db.collection("users").document("jacob_morgan").set(jacob_morgan)
