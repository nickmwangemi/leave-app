from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import LeaveRequest


class LeaveRequestsView(ListView):
    model = LeaveRequest
    template_name = "leave/leave_request_list.html"


class LeaveRequestCreateView(SuccessMessageMixin, CreateView):
    model = LeaveRequest
    template_name = "leave/leave_request_new.html"
    fields = ("name", "start_date", "end_date", "type_of_leave")
    success_message = "Leave request created successfully."


class LeaveRequestDetailView(DetailView):
    model = LeaveRequest
    template_name = "leave/leave_request_detail.html"


class LeaveRequestUpdateView(SuccessMessageMixin, UpdateView):
    model = LeaveRequest
    fields = ("name", "start_date", "end_date", "type_of_leave")
    template_name = "leave/leave_request_update.html"
    success_message = "Leave request updated successfully."


class LeaveRequestDeleteView(SuccessMessageMixin, DeleteView):
    model = LeaveRequest
    template_name = "leave/leave_request_delete.html"
    success_url = reverse_lazy("leave:leave_request_list")
    success_message = "Leave request deleted successfully."
