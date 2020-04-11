"""drf_hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_api.views import HelloWorldAPIView, hello_world_api
from drf_api.movie_list_api_view import MovieListAPIView
from drf_api.movie_retrieve_api_view import MovieRetrieveAPIView
from drf_api.movie_destroy_api_view import MovieDestroyAPIView
from drf_api.movie_update_api_view import MovieUpdateAPIView
from drf_api.movie_retrieve_update_api_view import MovieRetrieveUpdateAPIView
from drf_api.movie_list_create_api_view import MovieListCreateAPIView
from drf_api.movie_retrieve_destroy_api_view import MovieRetrieveDestroyAPIView
from drf_api.movie_retrieve_update_destroy_view import MovieRetrieveUpdateDestroyAPIView
from drf_api.movie_create_api_view import MovieCreateAPIView
from drf_api.movie_viewset_api import MovieViewSet
from drf_api.movie_generic_viewset_api import MovieGenericViewSet
from drf_api.movie_model_view_set_api import MovieModelViewSet
from drf_api.movie_read_only_model_view_set_api import MovieReadOnlyModelViewSet
from drf_api.movie_custom_actions_api import MovieCustomActionsView
from drf_api.csv_download_api_view import CSVDownloadViewSet, FileDownloadAPIView
from drf_api.file_upload_api import FileUploadUsingDBModel
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hello-world-api-func/', hello_world_api),
    path('hello-world-api/', HelloWorldAPIView.as_view()),
    url('^movie-list-api/$', MovieListAPIView.as_view()),
    url('^movie-retrieve-api/(?P<pk>\d+)/$', MovieRetrieveAPIView.as_view()),
    url('^movie-destroy-api/(?P<pk>\d+)/$', MovieDestroyAPIView.as_view()),
    url('^movie-update-api/(?P<pk>\d+)/$', MovieUpdateAPIView.as_view()),
    url('^movie-retrieve-update-api/(?P<pk>\d+)/$', MovieRetrieveUpdateAPIView.as_view()),
    url('^movie-list-create-api/$', MovieListCreateAPIView.as_view()),
    url('^movie-retrieve-destroy-api/(?P<pk>\d+)/$', MovieRetrieveDestroyAPIView.as_view()),
    url('^movie-retrieve-update-destroy-api/(?P<pk>\d+)/$', MovieRetrieveUpdateDestroyAPIView.as_view()),
    url('^movie-create-api/$', MovieCreateAPIView.as_view()),
    url('^csv-download-api/$', CSVDownloadViewSet.as_view()),
    url('^file-download-api/$', FileDownloadAPIView.as_view()),
    url('^file-upload-using-db-model-api/$', FileUploadUsingDBModel.as_view()),
    path('admin/', admin.site.urls)
]

router = DefaultRouter()
router.register(r'movies-viewset', MovieViewSet, basename='movies-viewset')
router.register(r'movies-generic-viewset', MovieGenericViewSet, basename='movies-generic-viewset')
router.register(r'movies-model-viewset', MovieModelViewSet, basename='movies-model-viewset')
router.register(r'movies-read-only-model-viewset', MovieReadOnlyModelViewSet,
                basename='movies-read-only-model-viewset')
router.register(r'movies-custom-actions-viewset', MovieCustomActionsView,
                basename='movies-custom-actions-viewset')
urlpatterns = urlpatterns + router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
