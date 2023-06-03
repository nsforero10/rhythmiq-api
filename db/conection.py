import firebase_admin
from firebase_admin import firestore, credentials
from uuid import uuid4

cred = credentials.Certificate('serviceAccountKey.json')

app = firebase_admin.initialize_app()
db = firestore.client()


def getAllSubgenresFromDB():
    subgenre_ref = db.collection('genre')
    subgenres = subgenre_ref.stream()

    subgenre_list = []

    for subgenre in subgenres:
        subgenre_list.append(subgenre.to_dict())

    return subgenre_list

