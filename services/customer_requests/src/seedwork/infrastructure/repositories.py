from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    def get_by_id(self):
        pass

    def list_all(self):
        pass

    def delete(self):
        pass
