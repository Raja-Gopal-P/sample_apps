from django.contrib import admin
from django.urls import path
from pages.views import PageCreationView


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-page/', self.admin_view(PageCreationView.as_view()), name="create-page"),
        ]
        return urls + custom_urls


custom_admin = CustomAdminSite(name='custom-admin')
