from fastapi import APIRouter, HTTPException
import json
import os
from week13.schema import User, UserCreate

router = APIRouter()
FILE_PATH = "users.txt"



def read_users():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def write_users(users):
    with open(FILE_PATH, "w") as f:
        json.dump(users, f, indent=4)


def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = read_users()

    new_user = user.dict()
    new_user["id"] = get_next_id(users)

    users.append(new_user)
    write_users(users)

    return new_user



@router.get("/", response_model=list[User])
def get_users():
    return read_users()



@router.get("/search", response_model=list[User])
def search_users(q: str):
    users = read_users()
    results = [u for u in users if q.lower() in u["name"].lower()]
    return results


@router.get("/{id}", response_model=User)
def get_user(id: int):
    users = read_users()

    for user in users:
        if user["id"] == id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{id}", response_model=User)
def update_user(id: int, updated_user: UserCreate):
    users = read_users()

    for user in users:
        if user["id"] == id:
            user.update(updated_user.dict())
            write_users(users)
            return user

    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()

    for user in users:
        if user["id"] == id:
            users.remove(user)
            write_users(users)
            return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")
