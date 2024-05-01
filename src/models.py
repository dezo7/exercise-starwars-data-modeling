import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    favoritos = relationship("Favorito", back_populates="usuario")

class Planeta(Base):
    __tablename__ = 'planetas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    diametro = Column(Integer)
    clima = Column(String)

    favoritos = relationship("Favorito", back_populates="planeta")

class Personaje(Base):
    __tablename__ = 'personajes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    especie = Column(String)
    genero = Column(String)

    favoritos = relationship("Favorito", back_populates="personaje")

class Favorito(Base):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    usuario = relationship("Usuario", back_populates="favoritos")
    planeta = relationship("Planeta", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
