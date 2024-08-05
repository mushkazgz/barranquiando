import mongoengine as me

# Conectar a la base de datos MongoDB
me.connect('testdb')

# Definir un documento
class User(me.Document):
    name = me.StringField(required=True)
    fullname = me.StringField()
    nickname = me.StringField()

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

    def __str__(self):
        return self.__repr__()

# Crear una instancia de User y guardarla en la base de datos
new_user = User(name='john', fullname='John Doe', nickname='johnny')
new_user.save()

# Consultar todos los usuarios
for user in User.objects:
    print(user)

# Consultar usuarios por nombre
user = User.objects(name='john').first()
print(user)
