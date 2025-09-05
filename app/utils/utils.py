from datetime import date
import uuid
from decimal import Decimal

def convert_decimal(obj):
    if isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        return float(obj)

def get_date():
  today_date = date.today()
  return today_date.strftime("%d/%m/%Y")

def generate_uuid():
  return str(uuid.uuid4())