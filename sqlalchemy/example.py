from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de la conexión a la base de datos SQLite en memoria
DATABASE_URI = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URI)

# Declarar una base de datos
Base = declarative_base()

# Definir una clase que represente una tabla en la base de datos
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear una instancia de User
new_user = User(name='john', fullname='John Doe', nickname='johnny')

# Añadir el nuevo usuario a la sesión y confirmar los cambios
session.add(new_user)
session.commit()

# Consultar todos los usuarios
for user in session.query(User).all():
    print(user)

# Consultar usuarios por nombre
user = session.query(User).filter_by(name='john').first()
print(user)
