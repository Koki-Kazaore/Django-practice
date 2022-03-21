from django.shortcuts import render

from .models import Room, Post

# Create your views here.
def index(request):
  return render(request, "rooms/index.html", {
    "rooms": Room.objects.all()
  })


def room(request, room_id):
  room = Room.objects.get(pk=room_id)
  post = Post.objects.get(where=room_id)
  return render(request, "rooms/room.html", {
    "room": room,
    "post": post
  })


def post(request, room_id):
  return render(request, "rooms/post.html")