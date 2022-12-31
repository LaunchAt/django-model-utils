from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .utils import hard_delete, restore, soft_delete, svg_no_icon, svg_yes_icon


class HardDeletableModelAdminMixin:
    def get_actions(self, request):
        self.admin_site.add_action(hard_delete)  # type: ignore
        actions = super().get_actions(request)  # type: ignore

        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions


class SoftDeletableModelAdminMixin:
    def get_actions(self, request):
        self.admin_site.add_action(soft_delete)  # type: ignore
        return super().get_actions(request)  # type: ignore

    def get_list_display(self, request):
        return super().get_list_display(request) + ('is_active',)  # type: ignore

    @admin.display(description=_('active'))
    def is_active(self, obj):
        return mark_safe(svg_no_icon if obj.is_deleted else svg_yes_icon)


class RestorableModelAdminMixin:
    def get_actions(self, request):
        self.admin_site.add_action(restore)  # type: ignore
        return super().get_actions(request)  # type: ignore


class UndeletableModelAdminMixin:
    def get_actions(self, request):
        actions = super().get_actions(request)  # type: ignore

        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions

    def has_delete_permission(self, *args, **kwargs):
        return False


class UneditableModelAdminMixin:
    def has_change_permission(self, *args, **kwargs):
        return False


class UnaddableModelAdminMixin:
    def has_add_permission(self, *args, **kwargs):
        return False


class BaseModelAdmin(
    RestorableModelAdminMixin,
    UndeletableModelAdminMixin,
    SoftDeletableModelAdminMixin,
    ModelAdmin,
):
    pass
