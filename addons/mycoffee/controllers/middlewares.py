from functools import wraps
from odoo.http import request
import json

class AuthUtility:
    @staticmethod
    def authenticate():
        """Perform custom authentication logic."""
        token = request.httprequest.headers.get('Authorization')
        if token == "your_custom_token":
            return request.env['res.users'].browse(1)  # Replace with actual user ID
        else:
            return None

def custom_auth_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        user = AuthUtility.authenticate()
        if user:
            request.env.user = user
            return method(*args, **kwargs)
        else:
            return request.make_response(json.dumps({'error': 'Authentication failed'}), status=401)
    return wrapper
