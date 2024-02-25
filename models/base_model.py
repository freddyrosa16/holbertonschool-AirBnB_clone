#!/usr/bin/python3
''' Class that defines all common attributes/methods for other classes. '''
import uuid
import datetime


class BaseModel():
    ''' Class that defines all common attributes/methods for other classes. '''

    def __init__(self):
        ''' Initializes a BaseModel instance with a unique ID,
        creation timestamp,and update timestamp. '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        ''' Returns a string representation of the BaseModel instance. '''
        return (f'[BaseModel] ({self.id}) {self.__dict__}')

    def save(self):
        ''' Updates the 'updated_at' attribute with the current datetime. '''
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        ''' Returns a dictionary representation of the BaseModel instance. '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['update_at'] = self.updated_at.isoformat()
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict
