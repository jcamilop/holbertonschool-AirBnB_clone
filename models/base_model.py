from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        return f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        dict["updated_at"] = self.created_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        return dict


if __name__ == "__main__":
    obgeto1 = BaseModel()
    print(obgeto1)
    print(obgeto1.to_dict())
