# Base Model

## Abstract Model Class

### `UuidPrimaryKeyModel`

* `id (UUIDField)`: Primary key field. A random UUID v4 key is set as default.

### `TimeStampedModel`

* `created_at (DateTimeField)`: Created date-time field. It is automatically saved when adding a record.
* `updated_at (DateTimeField)`: Updated date-time field. It is automatically saved when updating a record.

### `SoftDeletableModel`

* `deleted_at (DateTimeField)`: Soft-deleted date-time field. The default is `None` and it is not editable on the admin site.
* `is_deleted (property)`: The property that returns `True` when `deleted_at` is `not None` and returns `False` when that is `None`.
* `hard_delete (function)`: Do hard-delete (Django default delete function) of the `self` instance.
* `soft_delete (function)`: Do soft-delete of the `self` instance. It is the same as saving `deleted_at` as `django.utils.timezone.now()`.
* `delete (function)`: Overrided Django default delete function as `soft_delete`.
* `restore (function)`: Restore the deleted `self` instance. It is the same as saving `deleted_at` as `None`.

### `BaseModel`

The abstract model class inherited `UuidPrimaryKeyModel`, `TimeStampedModel`, and `SoftDeletableModel`.

It can be used for the abstract base model for the general models.

* `objects (Manager)`: `BaseModel` has the `BaseModelManager` instance as its manager.

## Query Set and Manager Class

### `SoftDeletableModelQuerySet`

* `hard_delete (function)`: Do hard-delete (Django default delete function) of the query set.
* `soft_delete (function)`: Do soft-delete of the query set. It is the same as saving their `deleted_at` as `django.utils.timezone.now()`.
* `delete (function)`: Overrided Django default delete function as `soft_delete`.
* `restore (function)`: Restore the deleted instances of the query set. It is the same as saving their `deleted_at` as `None`.

### `BaseModelQuerySet`

The base query set class inherited `SoftDeletableModelQuerySet`.

It can be used for the base query set class for the general models which inherited `BaseModel`.

### `SoftDeletableModelManager`

The manager class is created from `SoftDeletableModelQuerySet`.

It supports soft deletion.

### `BaseModelManager`

The manager class is created from `BaseModelQuerySet`.

It can be used for the base manager for the general models which inherited `BaseModel`.

## Model Admin Class

### `HardDeletableModelAdminMixin`

The model admin mixin class overwrites admin site actions.

It removes the `delete_selected` and adds the `hard_delete` action.

Only the staff user who has `delete` permission can do the `hard_delete` action.

### `SoftDeletableModelAdminMixin`

The model admin mixin class supports soft deletion.

It adds the `soft_delete` action and add `is_active`,
which show the record is not deleted, to the display column list.

Only the staff user who has `change` permission can do the `soft_delete` action.

### `RestorableModelAdminMixin`

The model admin mixin class supports restore of the soft-deleted instances.

It adds the `restore` action, and this action can be done by only the staff user who has `change` permission.

### `UndeletableModelAdminMixin`

The model admin mixin class disallows to delete a instance and some `delete` permission actions.

And it removes the `delete_selected`.

### `UneditableModelAdminMixin`

The model admin mixin class disallows to update a instance and some `change` permission actions.

### `UnaddableModelAdminMixin`

The model admin mixin class disallows to create a instance and some `add` permission actions.

### `BaseModelAdmin`

The model admin class inherited `RestorableModelAdminMixin`, `UndeletableModelAdminMixin`, `SoftDeletableModelAdminMixin`, and `ModelAdmin`.

It disabled hard-delete of instances and enabled soft-delete and restore.

It can be used for the base model admin class for the general models which inherited `BaseModel`.
