from django.contrib.admin.decorators import action
from django.utils.translation import gettext_lazy as _

svg_yes_icon = '''
<svg
  width="13"
  height="13"
  viewBox="0 0 1792 1792"
  xmlns="http://www.w3.org/2000/svg"
>
  <path
    fill="#70bf2b"
    d="
      M1412 734q0-28-18-46l-91-90q-19-19-45-19t-45 19l-408
      407-226-226q-19-19-45-19t-45 19l-91 90q-18 18-18 46 0 27 18
      45l362 362q19 19 45 19 27 0 46-19l543-543q18-18 18-45zm252 162q0
      209-103 385.5t-279.5 279.5-385.5 103-385.5-103-279.5-279.5-103-385.5
      103-385.5 279.5-279.5 385.5-103 385.5 103 279.5 279.5 103 385.5z
    "
  />
</svg>
'''

svg_no_icon = '''
<svg
  width="13"
  height="13"
  viewBox="0 0 1792 1792"
  xmlns="http://www.w3.org/2000/svg"
>
  <path
    fill="#dd4646"
    d="
      M1277 1122q0-26-19-45l-181-181 181-181q19-19 19-45
      0-27-19-46l-90-90q-19-19-46-19-26 0-45 19l-181
      181-181-181q-19-19-45-19-27 0-46 19l-90 90q-19
      19-19 46 0 26 19 45l181 181-181 181q-19 19-19 45 0 27 19
      46l90 90q19 19 46 19 26 0 45-19l181-181 181 181q19 19 45
      19 27 0 46-19l90-90q19-19 19-46zm387-226q0 209-103 385.5t-279.5
      279.5-385.5 103-385.5-103-279.5-279.5-103-385.5 103-385.5
      279.5-279.5 385.5-103 385.5 103 279.5 279.5 103 385.5z
    "
  />
</svg>
'''


@action(permissions=['delete'], description=_('hard delete'))
def hard_delete(modeladmin, request, queryset):
    if hasattr(queryset, 'hard_delete'):
        return queryset.hard_delete()

    return queryset.delete()


@action(permissions=['change'], description=_('soft delete'))
def soft_delete(modeladmin, request, queryset):
    assert hasattr(queryset, 'soft_delete')
    return queryset.soft_delete()


@action(permissions=['change'], description=_('restore'))
def restore(modeladmin, request, queryset):
    assert hasattr(queryset, 'restore')
    return queryset.restore()
