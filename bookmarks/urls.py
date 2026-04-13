from django.urls import path
from .views import add_bookmark , get_bookmarks , delete_bookmark, edit_bookmark

urlpatterns = [
    path("",get_bookmarks),
    path("add/",add_bookmark),
    path("delete/",delete_bookmark),
    path("edit/",edit_bookmark),

]