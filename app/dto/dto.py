from utils.utils import generate_uuid, get_date



class UserDTO():

  def __init__(self, userid: str, date:str, items:any):

    self.userid = userid
    self.date = date
    self.items = items

  @classmethod
  def from_dict(cls, item: dict):
    
    return cls(item.get("userId", generate_uuid()), item.get("date", get_date()), {k : v for k, v in item.items() if k not in ["userId", "date"]})
  
  def to_dict(self):
    return {"userId":self.userid, "time": self.date, **self.items}