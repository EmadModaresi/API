from django.urls import path
from API.views import GetALLData, GetFavData, UpgradeFavData, GetNotFavData, PostModelData, SearchData, DeleteData, \
    allApi , SetData

urlpatterns = [
    path('get-all-data/', GetALLData.as_view()),
    path('all-data/', allApi),
    path('get-fav-data/', GetFavData.as_view()),
    path('get-not-fav-data/', GetNotFavData.as_view()),
    path('post-model/', PostModelData.as_view()),
    path('post-fun/', SetData),
    path('search/', SearchData.as_view()),
    path('delete/<int:pk>/', DeleteData.as_view()),
    path('updata-fav-data/<int:pk>/', UpgradeFavData.as_view()),
    # path('find-books/<str:name>/', UserGetApi.as_view()),

]
