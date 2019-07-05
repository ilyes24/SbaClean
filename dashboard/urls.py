from django.urls import path, include
from dashboard import views as dash_views


app_name = "dashboard"

urlpatterns = [
    path('dashboard', dash_views.dashboard_index, name="dashboard_index")
]
