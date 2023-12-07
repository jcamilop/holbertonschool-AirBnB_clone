from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        
        if len(kwargs) > 0:
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict


if __name__ == "__main__":
    print("--obgeto1--")
    obgeto1 = BaseModel()
    print(obgeto1)
    print(obgeto1.to_dict())
    
    print("--obgeto2--")
    
    obgeto2 = BaseModel(created_at="2022-10-15T10:30:00.000", updated_at="2022-12-25T11:40:35.125")
    print(obgeto2)
    print(obgeto2.to_dict())
    
    
    
