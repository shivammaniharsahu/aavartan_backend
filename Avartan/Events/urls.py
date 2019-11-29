from django.urls import include, path
from . import views


from . import views
urlpatterns = [
    path('', views.EventListView.as_view()),
    path('<int:pk>/', views.EventDetailView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]