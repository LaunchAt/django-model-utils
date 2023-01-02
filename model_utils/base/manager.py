from django.db.models.manager import BaseManager

from .query import BaseModelQuerySet, SoftDeletableModelQuerySet


class SoftDeletableModelManager(
    BaseManager.from_queryset(SoftDeletableModelQuerySet),  # type: ignore
    BaseManager,
):
    pass


class BaseModelManager(
    BaseManager.from_queryset(BaseModelQuerySet),  # type: ignore
    BaseManager,
):
    pass
