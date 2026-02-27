import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                
                return [json.loads(line) for line in f]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, users):
        
        with open(self.file_path, "w") as f:
            for user in users:
                f.write(json.dumps(user) + "\n")

    def find_by_id(self, user_id):
        
        users = self.load()
        return next((u for u in users if u.get("id") == user_id), None)

    def update_user(self, user_id, updated_data):
        
        users = self.load()
        for i, user in enumerate(users):
            if user.get("id") == user_id:
                users[i].update(updated_data)
                self.save(users)
                return True
        return False

    def delete_user(self, user_id):
        
        users = self.load()
        initial_count = len(users)
        users = [u for u in users if u.get("id") != user_id]
        if len(users) < initial_count:
            self.save(users)
            return True
        return False