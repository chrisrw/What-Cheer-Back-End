from django.urls import path
from .views import current_user, UserList

# any time a user revisits the site, reloads the page, or does anything that causes React to forget its state. React will check if the user has a token stored in the browser, if a token is found, it'll make a request to this view.
urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]