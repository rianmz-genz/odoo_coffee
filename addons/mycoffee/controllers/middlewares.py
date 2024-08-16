from functools import wraps
from odoo.http import request
import json
import logging
from ..helpers.encode_decode import decode_object
logger = logging.getLogger(__name__)
class AuthUtility:
    @staticmethod
    def authenticate():
        """Perform custom authentication logic."""
        token = request.httprequest.headers.get('Authorization')
        if not token:
            return None
        
        user_id = False
        try:
            user_id = decode_object(token)
        except Exception as e:
            raise Exception("Invalid token")
        
        logger.info(f"Token: {token}, User: {user_id}")
        return user_id if user_id else None


def custom_auth_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        try:
            user = AuthUtility.authenticate()
            if user:
                request.env.user = user
                return method(*args, **kwargs)
            else:
                return request.make_response(json.dumps({'message': 'Unauthorized'}), status=401)
        except Exception as e:
            return request.make_response(json.dumps({'message': f'{e}'}), status=401)
    return wrapper
