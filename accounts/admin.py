from django.contrib import admin
from django.urls import path
from pages.views import PageCreationView, PageUpdateView, PageDeleteView


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-page/', self.admin_view(PageCreationView.as_view()), name="create-page"),
            path('edit-page/<slug:slug>/', self.admin_view(PageUpdateView.as_view()), name="edit-page"),
            path('delete-page/<slug:slug>/', self.admin_view(PageDeleteView.as_view()), name="delete-page"),
        ]
        return urls + custom_urls


custom_admin = CustomAdminSite(name='custom-admin')
