from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models

from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, ListAdminView

GETADD_VAR = '_getadd'

class GetAddPlugin(BaseAdminPlugin):

    get_add = []
   


    def result_item(self, item, obj, field_name, row):
        if (field_name in self.get_add):
            rel_obj = None
            if hasattr(item.field, 'rel') and isinstance(item.field.rel, models.ManyToOneRel):
                rel_obj = getattr(obj, field_name)
            elif field_name in self.get_add:
                rel_obj = obj
        
            if rel_obj:
                if rel_obj.__class__ in site._registry:
                    try:
                        model_admin = site._registry[rel_obj.__class__]
                        has_view_perm = model_admin(self.admin_view.request).has_view_permission(rel_obj)
                    except:
                        has_view_perm = self.admin_view.has_model_perm(rel_obj.__class__, 'view')
                else:
                    has_view_perm = self.admin_view.has_model_perm(rel_obj.__class__, 'view')
            
            if rel_obj and has_view_perm:
                opts = rel_obj._meta
                try:
                    
                    # /xadmin/zl955/ipapp/5/detail/
                    item_res_uri = ('%s' % (getattr(rel_obj, 'ip'),))
                    
                    # item_res_uri = reverse('%s:%s_%s_detail' % (self.admin_site.app_name,opts.app_label, opts.model_name),args=(getattr(rel_obj, opts.pk.attname),))
                    if item_res_uri:

                        edit_url = ''
                        item.btns.append('<a data-res-uri="%s" class="get-add" rel="tooltip" title="%s"><i class="fa fa-globe" style="font-size: 2rem;"></i></a>'
                                         % (item_res_uri, _(u'Details of %s') % str(rel_obj)))
                except NoReverseMatch:
                    pass
        return item

    # Media
    def get_media(self, media):
        if self.get_add or self.get_add:
            media = media + self.vendor('xadmin.plugin.getadd.js', 'xadmin.form.css')
        return media

site.register_plugin(GetAddPlugin, ListAdminView)
