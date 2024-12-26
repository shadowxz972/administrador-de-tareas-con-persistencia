from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuracion de la base de datos
DATABASE_URL = 'sqlite:///base.db'

# Crea la base para los modelos
Base = declarative_base()

# Crea el motor de conexion
engine = create_engine(DATABASE_URL, echo=False)

# Fabrica de sesiones
Session = sessionmaker(bind=engine)
