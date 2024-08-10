from functools import wraps
from odoo.http import request
import json
import logging
logger = logging.getLogger(__name__)
class AuthUtility:
    @staticmethod
    def authenticate():
        """Perform custom authentication logic."""
        token = request.httprequest.headers.get('Authorization')
        if not token:
            return None
        
        user = request.env['res.users'].sudo().search([
            ('token', '=', token)
        ])
        
        logger.info(f"Token: {token}, User: {user}")
        return user if user else None


def custom_auth_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        user = AuthUtility.authenticate()
        if user:
            request.env.user = user
            return method(*args, **kwargs)
        else:
            return request.make_response(json.dumps({'message': 'Unauthorized'}), status=401)
    return wrapper
