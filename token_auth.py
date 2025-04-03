import os
from dotenv import load_dotenv
from flask import request
import jwt
import werkzeug.exceptions

load_dotenv()

def check_token(route_handler):
    def wrapper(*args, **kwargs):
        # First we get the Authorization header
        header_token = request.headers.get("Authorization")

        if header_token is None:
            raise werkzeug.exceptions.Unauthorized
        
        # We then split the token and check if it consist of two parts and
        # if the first part is Bearer
        auth_header_split = header_token.split(" ")

        if len(auth_header_split) != 2:
            raise werkzeug.exceptions.Unauthorized
        if auth_header_split[0] != "Bearer":
            raise werkzeug.exceptions.Unauthorized
        
        # After that we decode the token and get the contents. Raises unauthorized exceptions 
        # if decoded message doesn't contain key "authorized" with value "yes"
        try:
            decoded =  jwt.decode(auth_header_split[1], key=os.environ.get("SECRET_KEY"),algorithms=["HS512"])
            if "authorized" not in decoded.keys():
                raise werkzeug.exceptions.Unauthorized
            if decoded["authorized"] != "yes":
                raise werkzeug.exceptions.Unauthorized
        except Exception:
            raise werkzeug.exceptions.Unauthorized
                    
        return route_handler(*args, **kwargs)
    return wrapper
