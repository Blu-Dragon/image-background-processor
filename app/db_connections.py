# Used to establish db connections for CRUD operations
# app(__init__.py) will import stuff from here
from firebase_init import initialize_firebase, get_database_reference, close_firebase_app

# Initialize Firebase
initialize_firebase()

# Initialize Firebase Admin SDK
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred), {
    'databaseURL': 'https://flask-test-database-default-rtdb.firebaseio.com/'
})

# Reference to the root of your database
ref = get_database_reference('/')

# Add data to the database
data_to_add = {
    'exampleKey': 'exampleValue',
    'nestedData': {
        'nestedKey': 'nestedValue'
    }
}

ref.update(data_to_add)

# Read data from the database
data = ref.get()
print("Data from the database:", data)

# Update data in the database
ref.update({'exampleKey': 'newValue'})

# Delete data from the database
ref.child('nestedData/nestedKey').delete()

# Close the connection
close_firebase_app()
