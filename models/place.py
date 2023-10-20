#!/usr/bin/env python3
"""
The module that contains the PLACE class
"""
from models.base_model import BaseModel
import models


class Place(BaseModel):
    """
    The class State that inherits the BaseModel class
    """
    city_id = ""
    user_id = ""
    description = ""
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """
        Initialises the class with values and sets it for storage
        """
        super().__init__(*args, **kwargs)