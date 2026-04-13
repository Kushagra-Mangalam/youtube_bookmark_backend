from config.db import db
from django.contrib.auth.hashers import make_password,check_password

users_collection = db["users"]

def create_user(name,email,password):
    if users_collection.find_one({"email":email}):
        return None
    user={
        "name":name,
        "email":email,
        "password":make_password(password)
    }

    users_collection.insert_one(user)
    return user


def authenticate_user(email,password):
    user=users_collection.find_one({"email":email})

    if user and check_password(password,user["password"]):
        return user
    return None

    