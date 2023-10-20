#!/usr/bin/env python3
"""
The module that contains the CITY class
"""
from models.base_model import BaseModel
import models


class City(BaseModel):
    """
    The class City that inherits the BaseModel class
    """
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        Initialises the class with values and sets it for storage
        """
        super().__init__(*args, **kwargs)