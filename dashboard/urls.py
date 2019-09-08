from django.urls import path, include
from dashboard import views as dash_views


app_name = "dashboard"

urlpatterns = [
    path('dashboard/', dash_views.dashboard_index, name="dashboard"),
    path('dashboard/anomalies', dash_views.dashboard_anomalies, name="dashboard_anomalies"),
    path('dashboard/anomalies/edit/<int:pid>', dash_views.dashboard_anomalie_edit, name="dashboard_anomalie_edit"),
    path('dashboard/anomalies/archive/<int:pid>', dash_views.dashboard_anomalie_archive, name="dashboard_anomalie_archive"),
    path('dashboard/archives', dash_views.dashboard_archives, name="dashboard_archives"),
    path('dashboard/users', dash_views.dashboard_users, name="dashboard_users"),
    path('dashboard/users/edit/<int:pid>', dash_views.dashboard_users_edit, name="dashboard_users_edit"),
    path('dashboard/comments', dash_views.dashboard_comments, name="dashboard_comments"),
    path('dashboard/comments/edit/<int:pid>', dash_views.dashboard_comments_edit, name="dashboard_comments_edit"),
    path('dashboard/reports', dash_views.dashboard_reports, name="dashboard_reports"),
    path('dashboard/reports/edit/<int:pid>', dash_views.dashboard_reports_edit, name="dashboard_reports_edit"),
    path('dashboard/events', dash_views.dashboard_events, name="dashboard_events"),
    path('dashboard/event/approve/<int:eid>', dash_views.dashboard_event_approve, name="dashboard_event_approve"),
    path('dashboard/events/edit/<int:pid>', dash_views.dashboard_events_edit, name="dashboard_events_edit"),            
]
