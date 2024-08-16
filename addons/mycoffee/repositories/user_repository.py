from abc import ABC, abstractmethod
from ..models.models import Models
from dataclasses import dataclass
from ..helpers.encode_decode import encode_object
@dataclass
class UserPayload:
    token: str
    
class IUserRepository(ABC):
    @abstractmethod
    def authenticate(self, login):
        pass
    
class UserRepository(IUserRepository):
    def __init__(self, env):
        self.env = env
    
    def authenticate(self, login) -> UserPayload:
        user = Models.User(env=self.env).search([
            ('login', '=', login)
        ],limit=1)
        if not user:
            raise Exception("User tidak ditemukan")
        return UserPayload(token=encode_object({'user_id': user.id, 'user_login': user.login}))