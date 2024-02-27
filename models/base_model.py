#!/usr/bin/python3
""" Class that defines all common attributes/methods for other classes. """
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    Class that defines all common attributes/methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """ Initialization of the model class. """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    time_format = '%Y-%m-%dT%H:%M:%S.%f'
                    self.__dict__[key] = datetime.strptime(value, time_format)
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a string representation of BaseModel. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Converts the object to a dictionary representation. """
        obj_dict = self.__dict__.copy
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
