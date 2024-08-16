from abc import ABC, abstractmethod

from ..models.models import Models
from ..repositories.user_repository import IUserRepository, UserPayload
from typing import List
from dataclasses import dataclass
from ..helpers.encode_decode import bin_to_base64
    
class IUserService(ABC):
    @abstractmethod
    def authenticate(self, login):
        pass
    
    
class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def authenticate(self, login) -> UserPayload:
        try:
            user = self.user_repository.authenticate(login=login)
        except Exception as e:
            raise e

        # Convert the user model to a DTO
        return user