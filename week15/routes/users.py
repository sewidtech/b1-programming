from fastapi import APIRouter, HTTPException
from week15.user_store import UserStore
from week15.schema import User, UserCreate

router = APIRouter()


store = UserStore("week15/users.db")

@router.get("/", response_model=list[User])
def get_users():
   
    return store.load()

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    
    users = store.load()
    new_id = max([int(u["id"]) for u in users], default=0) + 1
    
    new_user_data = user.model_dump()
    new_user_data["id"] = new_id
    
   
    store.save(new_user_data)
    return new_user_data

@router.get("/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
   
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user(user_id: int, updated_data: UserCreate):
    
    success = store.update_user(user_id, updated_data.model_dump())
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
   
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}