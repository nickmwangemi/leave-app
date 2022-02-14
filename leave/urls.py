from django.urls import path

from .views import (
    LeaveRequestCreateView,
    LeaveRequestDeleteView,
    LeaveRequestDetailView,
    LeaveRequestsView,
    LeaveRequestUpdateView,
)

app_name = "leave"


urlpatterns = [
    path("", LeaveRequestsView.as_view(), name="leave_request_list"),
    path(
        "leave_request/new/", LeaveRequestCreateView.as_view(), name="leave_request_new"
    ),
    path(
        "leave_request/<int:pk>/",
        LeaveRequestDetailView.as_view(),
        name="leave_request_detail",
    ),
    path(
        "leave_request/<int:pk>/edit/",
        LeaveRequestUpdateView.as_view(),
        name="leave_request_edit",
    ),
    path(
        "leave_request/<int:pk>/delete/",
        LeaveRequestDeleteView.as_view(),
        name="leave_request_delete",
    ),
]
