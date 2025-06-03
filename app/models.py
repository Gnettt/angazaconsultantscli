from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    program_id = Column(Integer, ForeignKey('programs.id'))
    date_enrolled = Column(String)


    user = relationship("User", back_populates="enrollments")
    program = relationship("Program", back_populates="enrollments")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    
   
    enrollments = relationship("Enrollment", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

class Program(Base):
    __tablename__ = 'programs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

   
    enrollments = relationship("Enrollment", back_populates="program", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Program(id={self.id}, title='{self.title}')>"

