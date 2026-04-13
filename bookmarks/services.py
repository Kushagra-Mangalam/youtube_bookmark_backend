from config.db import db 
bookmarks_collection=db["bookmarks"]
videos_collection=db["videos"]


def save_bookmark(user_email , video_id, time , desc):
    bookmark_data={
        "user_email":user_email,
        "videoId":video_id,
        "time":time,
        "desc":desc
    }

    result = bookmarks_collection.insert_one(bookmark_data)
    return str(result.inserted_id)


def get_user_bookmarks(user_email, video_id=None):
    query = {"user_email": user_email}
    if video_id:
        query["videoId"] = video_id

    bookmarks=list(bookmarks_collection.find(query))
    for bm in bookmarks:
        bm["_id"]=str(bm["_id"])
    return bookmarks


def delete_user_bookmark(user_email, video_id, time):
    bookmarks_collection.delete_one({
        "user_email": user_email,
        "videoId": video_id,
        "time": float(time) if isinstance(time, (int, float, str)) else time
    })

def edit_user_bookmark(user_email, video_id, time, desc):
    bookmarks_collection.update_one({
        "user_email": user_email,
        "videoId": video_id,
        "time": float(time) if isinstance(time, (int, float, str)) else time
    }, {"$set": {"desc": desc}})