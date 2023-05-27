from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from chat.models import RolePlayingRoom


# Create your views here.
@method_decorator(staff_member_required, name="dispatch")
class RolePlayingRoomDetailView(DetailView):
    model = RolePlayingRoom

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


role_playing_room_detail = RolePlayingRoomDetailView.as_view()
