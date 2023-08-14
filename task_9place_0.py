#!/usr/bin/python3
"""Doc
"""
#unresolved: why would there be models.tmp_place if none was created?
from models.tmp_place import *
from models.tmp_place import Place


class Place(Place):
    """Doc
    """
    city_id = None
    user_id = None
    name = None
    description = None
    number_rooms = None
    number_bathrooms = None
    max_guest = None
    price_by_night = None
    latitude = None
    longitude = None
    amenities = None
