import base64
import uuid
from abc import ABC, abstractmethod


def generate_id() -> str:
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip(b'=').decode('ascii')


class BaseSqlAlchemyModelRepository(ABC):
    def __init__(self, session) -> None:
        self.session = session

    def commit(self):
        self.session.commit()

    @property
    def _query_read(self):
        return self.session.query(self._model_cls)

    @property
    def _query_write(self):
        return self.session.query(self._model_cls)

    def count(self, filters=None) -> int:
        return self._query_read.filter_by(**(filters or {})).count()

    @property
    @abstractmethod
    def _model_cls(self):
        raise NotImplementedError()


class SqlAlchemyModelRepository(BaseSqlAlchemyModelRepository, ABC):

    def get(self, id: int):
        return self._query_read.filter(self._model_cls.id == id).first()

    def list_all(self, order_by='id', filters=None):
        return self._query_read \
            .filter_by(**(filters or {})) \
            .order_by(order_by) \
            .all()

    def list(self, page_size: int, page: int, order_by='id', filters=None):
        return self._query_read \
            .filter_by(**(filters or {})) \
            .order_by(order_by) \
            .offset(page * page_size) \
            .limit(page_size) \
            .all()

    def create(self, obj) -> int:
        obj = self._model_cls(**obj.dict())
        self.session.add(obj)
        self.session.flush()
        assert obj.id is not None
        return obj.id

    def update(self, id: int, **kwargs):
        self._query_write \
            .filter(self._model_cls.id == id) \
            .update(kwargs)

    def delete(self, id):
        result = self._query_write \
            .filter(self._model_cls.id == id) \
            .first()
        self.session.delete(result)

    def exists(self, id) -> bool:
        records = self._query_read.filter(self._model_cls.id == id).count()
        return records > 0
