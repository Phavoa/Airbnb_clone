#!/usr/bin/env python3
"""
The module that contains the REVIEW class
"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """
    The class State that inherits the BaseModel class
    """
    user_id = ""
    place_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initialises the class with values and sets it for storage
        """
        super().__init__(*args, **kwargs)