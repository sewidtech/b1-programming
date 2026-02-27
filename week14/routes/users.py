from fastapi import APIRouter, HTTPException
from week14.user_store import UserStore
from week14.schema import User, UserCreate

router = APIRouter()

store = UserStore("week14/users.txt")

@router.get("/", response_model=list[User])
def get_users():
    
    return store.load()

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = store.load()
    
    new_id = max([u["id"] for u in users], default=0) + 1
    new_user = user.model_dump()
    new_user["id"] = new_id
    
    users.append(new_user)
    
    store.save(users)
    return new_user

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