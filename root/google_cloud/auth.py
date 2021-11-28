import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': "blockchain-analytics-chainlink",
})

db = firestore.client()


# #Write data
# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })

# #read data
users_ref = db.collection(u'ethereum')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
