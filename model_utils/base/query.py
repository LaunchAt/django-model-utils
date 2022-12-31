from django.db.models.query import QuerySet
from django.utils.timezone import now


class SoftDeletableModelQuerySet(QuerySet):
    def hard_delete(self):
        return super().delete()

    def soft_delete(self):
        return super().update(deleted_at=now())

    def delete(self):
        return self.soft_delete()

    def restore(self):
        return super().update(deleted_at=None)


class BaseModelQuerySet(SoftDeletableModelQuerySet):
    pass
