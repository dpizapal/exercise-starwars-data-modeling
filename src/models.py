import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique = True, nullable=False)
    description = Column(String(200))
    birth = Column(DateTime, nullable=False)
    eye_color = Column(String(15))
    skin_color = Column(String(15))
    hair_color = Column(String(15))
    height = Column(Float, nullable = False)
    natal_planet = Column(Integer, ForeignKey("planet.id"), nullable = False )
    
    

    

class Planet(Base):

    __tablename__ = "planet"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique = True, nullable=False)
    description = Column(String(200))
    population = Column(Integer, nullable = False)
    gravity = Column(Integer, nullable = False)
    climate = Column(Integer, nullable = False)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer, nullable = False)
    


     

class Vehicle(Base):
     
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique = True, nullable=False)
    model = Column(String(200))
    manufacturer = Column(String(200))
    lenghth = Column(Integer)
    max_atmosphering_speed = Column(Float)
    crew = Column(Float)
    passengers = Column(Float)
    
    


class Favorite_Character(Base):

    __tablename__ = "favorite_character"

    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey("character.id"), nullable = False)
    user_id = Column(Integer, ForeignKey("username.id"), nullable = False)

class Favorite_Vehicle(Base):

    __tablename__ = "favorite_vehicle"

    id = Column(Integer, primary_key = True)
    ship_id = Column(Integer, ForeignKey("vehicle.id"), nullable = False)
    user_id = Column(Integer, ForeignKey("username.id"), nullable = False)

class Favorite_Planet(Base):

    __tablename__ = "favorite_planet"

    id = Column(Integer, primary_key = True)
    planet_id = Column(Integer, ForeignKey("planet.id"), nullable = False)
    user_id = Column(Integer, ForeignKey("username.id"), nullable = False)


class Username(Base):

    __tablename__ = "username"

    id = Column(Integer, primary_key = True)
    username = Column(String(20), unique = True, nullable=False)
     


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
