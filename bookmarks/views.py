from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import (
    save_bookmark, 
    get_user_bookmarks, 
    delete_user_bookmark, 
    edit_user_bookmark
)

def get_user_email(request):
    # request.user is populated by MongoJWTAuthentication
    return request.user.email

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_bookmark(request):
    user_email = get_user_email(request)
    data = request.data
    
    video_id = data.get("videoId")
    time = data.get("time")
    desc = data.get("desc", f"Bookmark at {time}")

    if not video_id or time is None:
        return Response({"error": "Missing videoId or time"}, status=400)

    save_bookmark(user_email, video_id, time, desc)
    return Response({"message": "Bookmark added successfully"}, status=201)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_bookmarks(request):
    user_email = get_user_email(request)
    video_id = request.query_params.get("videoId")
    
    # If no videoId is provided, it returns all bookmarks for that user
    bookmarks = get_user_bookmarks(user_email, video_id)
    return Response(bookmarks)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_bookmark(request):
    user_email = get_user_email(request)
    video_id = request.data.get("videoId")
    time = request.data.get("time")

    if not video_id or time is None:
        return Response({"error": "Missing videoId or time"}, status=400)

    delete_user_bookmark(user_email, video_id, time)
    return Response({"message": "Bookmark deleted"})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def edit_bookmark(request):
    user_email = get_user_email(request)
    video_id = request.data.get("videoId")
    time = request.data.get("time")
    desc = request.data.get("desc")

    if not video_id or time is None or not desc:
        return Response({"error": "Missing videoId, time or desc"}, status=400)

    edit_user_bookmark(user_email, video_id, time, desc)
    return Response({"message": "Bookmark edited"})