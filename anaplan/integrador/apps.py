from django.apps import AppConfig


class IntegradorConfig(AppConfig):
    name = 'integrador'

    def ready(self):
        from django.contrib import admin
        from django.contrib.admin import sites

        '''
        class FornoAdminSite(admin.AdminSite):
            pass

        mysite = FornoAdminSite()
        admin.site = mysite
        sites.site = mysite
        admin.AdminSite.enable_nav_sidebar = False
        '''