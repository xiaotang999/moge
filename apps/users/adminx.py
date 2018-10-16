import xadmin

from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _
from xadmin.views import ListAdminView

from .models import User, UserSetting


class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'group', 'ip',"add_time")
    list_filter = ('username', 'group', 'ip')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # search_fields = ('username', 'first_name', 'last_name', 'email', 'group', 'ip')
    list_editable = ["group"]
    ordering = ('-add_time','username')
    model_icon = 'fa fa-users'
    get_add = ["ip"]
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()

xadmin.site.unregister(User)
xadmin.site.register(User, UserProfileAdmin)

class UserSettingAdmin(object):
    """会员组别"""
    list_display = ["name", "limit_speak_no", "open_speak","add_time"]
    ordering = ["name"]

xadmin.site.register(UserSetting, UserSettingAdmin)

    