#!/usr/bin/python3
"""Doc
"""
#unresolved: why would there be models.tmp_user if none was created?
from models.tmp_user import *
from models.tmp_user import User


class User(User):
    """Doc
    """
    email = None
