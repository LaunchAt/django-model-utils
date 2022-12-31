import uuid

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .manager import BaseModelManager


class UuidPrimaryKeyModel(models.Model):
    id = models.UUIDField(_('uuid'), primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_('created date-time'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated date-time'), auto_now=True)

    class Meta:
        abstract = True


class SoftDeletableModel(models.Model):
    deleted_at = models.DateTimeField(
        _('deleted date-time'),
        null=True,
        default=None,
        editable=False,
    )

    class Meta:
        abstract = True

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def hard_delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    def soft_delete(self):
        if self.deleted_at is None:
            self.deleted_at = now()
            self.save(update_fields=['deleted_at'])
            return 1, {self._meta.label: 1}

        return 0, {}

    def delete(self, *args, **kwargs):
        return self.soft_delete()

    def restore(self):
        if self.deleted_at is not None:
            self.deleted_at = None
            self.save(update_fields=['deleted_at'])


class BaseModel(UuidPrimaryKeyModel, TimeStampedModel, SoftDeletableModel):
    objects = BaseModelManager()

    class Meta:
        abstract = True
