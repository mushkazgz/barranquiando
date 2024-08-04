from pymongo import MongoClient

# Conectar al servidor MongoDB
client = MongoClient('localhost', 27017)

# Acceder a la base de datos 'barranquiando'
db = client['barranquiando']

# Acceder a la colección 'barrancos'
collection = db['barrancos']

# Insertar documentos en la colección 'barrancos'
barrancos = [
    {"nombre": "Oscuros de Balced", "rapeles": 4},
    {"nombre": "Barranco de Mascún", "rapeles": 10},
    {"nombre": "Barranco de Vero", "rapeles": 8},
    {"nombre": "Barranco de Formiga", "rapeles": 5},
    {"nombre": "Barranco de Gorgas Negras", "rapeles": 12},
    {"nombre": "Barranco de Peonera", "rapeles": 6},
    {"nombre": "Barranco de Furco", "rapeles": 3},
    {"nombre": "Barranco de Litro", "rapeles": 7},
    {"nombre": "Barranco de Aigüeta de Barbaruens", "rapeles": 9},
    {"nombre": "Barranco de Otal", "rapeles": 2}
]

# Insertar múltiples documentos
result = collection.insert_many(barrancos)

# Mostrar los IDs de los documentos insertados
print(f"Documentos insertados con _ids: {result.inserted_ids}")
