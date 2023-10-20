#!/usr/bin/env python3
"""
The module that contains the AMENITY class
"""
from models.base_model import BaseModel
import models


class Amenity(BaseModel):
    """
    The class State that inherits the BaseModel class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialises the class with values and sets it for storage
        """
        super().__init__(*args, **kwargs)