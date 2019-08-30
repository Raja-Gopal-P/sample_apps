from django.contrib import admin
from django.urls import path
from pages.views import PageCreationView, PageUpdateView, PageDeleteView, reorder_page
from places.views import PlaceCreateView


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-page/', self.admin_view(PageCreationView.as_view()), name="create-page"),
            path('edit-page/<slug:slug>/', self.admin_view(PageUpdateView.as_view()), name="edit-page"),
            path('delete-page/<slug:slug>/', self.admin_view(PageDeleteView.as_view()), name="delete-page"),
            path('reorder-pages/', self.admin_view(reorder_page), name="reorder-pages"),
            path('create-place/', self.admin_view(PlaceCreateView.as_view()), name="create-place"),
        ]
        return urls + custom_urls


custom_admin = CustomAdminSite(name='custom-admin')
