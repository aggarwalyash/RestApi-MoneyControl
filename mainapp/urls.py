from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('users/',views.UserListView.as_view()),
    path('wallets/',views.WalletListView.as_view()),
    path('wallets/<int:pk>/',views.WalletDetailView.as_view()),
    path('contactbook/',views.ContactBookList.as_view()),
    path('contactbook/<int:pk>/',views.ContactBookDetail.as_view()),
    path('lendingbook/',views.LendingBookList.as_view()),
    path('lendingbook/<int:pk>/',views.LendingBookDetail.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
