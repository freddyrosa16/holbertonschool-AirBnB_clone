#!/usr/bin/python3
''' Class that defines all common attributes/methods for other classes. '''
import models
import uuid
from datetime import datetime


class BaseModel():
    '''
    Class that defines all common attributes/methods
    for other classes.
    '''

    def __init__(self,  *args, **kwargs):
        ''' Initializes model class. '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' Returns a string representation of the BaseModel instance. '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' Updates the 'updated_at' attribute with the current datetime. '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Returns a dictionary representation of the BaseModel instance. '''
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
