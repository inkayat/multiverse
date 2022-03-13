from django.contrib import admin
from django.urls import path
from multiverse import apis,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    #path('multiverse/data/', views.data_page, name='data_page'),
    path('multiverse/create', views.AddData.as_view(), name='add-data'),
    path('api/data/create', apis.add_data, name='api-add-data'),
    path('api/data/list/', apis.data_list, name='view-data'),
    path('api/data/<int:id>/', apis.data_details, name='data-details'),
    path('api/data/last/', apis.last, name='last-data'),
    path('api/compute/mean', apis.compute_mean, name='compute-mean'),
    path('api/compute/feature-importance', apis.feature_importance_list, name="feature-importance-list"),
    path('api/compute/feature-importance/<int:order>/', apis.feature_importance, name='feature-importance'),
]