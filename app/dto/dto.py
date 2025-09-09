from utils.utils import generate_uuid, get_date



class UserDTO():

  def __init__(self, userid: str, date:str, items:any):

    self.userid = userid
    self.date = date
    self.items = items

  @classmethod
  def from_dict(cls, item: dict):
    uuid = generate_uuid()
    date = get_date()
    return cls(item.get("userId", f"USERID#{uuid}"), item.get("date", f"DATE#{date}"), {k : v for k, v in item.items() if k not in ["userId", "date"]})
  
  def to_dict(self):
    return {"userId":self.userid, "time": self.date, **self.items}