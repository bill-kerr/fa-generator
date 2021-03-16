from sqlalchemy import Column, String, Time

from database.base import BaseModel
from database.common import generate_id


class ForceAccountPackage(BaseModel):
    __tablename__ = 'force_account_package'

    id = Column(String, primary_key=True, default=generate_id)
    uploaded_file = Column(String)
    package_file = Column(String)
    task_id = Column(String)
    created_at = Column(Time)
