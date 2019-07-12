from django.urls import path, include
from dashboard import views as dash_views


app_name = "dashboard"

urlpatterns = [
    path('dashboard', dash_views.dashboard_index, name="dashboard"),
    path('dashboard/anomalies', dash_views.dashboard_anomalies, name="dashboard_anomalies"),
    path('dashboard/anomalies/edit/<int:pid>', dash_views.dashboard_anomalie_edit, name="dashboard_anomalie_edit"),
    path('dashboard/users', dash_views.dashboard_users, name="dashboard_users"),
]
