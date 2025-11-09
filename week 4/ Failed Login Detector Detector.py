#desired result


print("checking login attempts...")  


#tracking login attempts




login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]

#failed attempts dictionary

failed_attempts = {}

for user , status in login_attempts:
    if status == "failed" :
   
     failed_attempts[user] = failed_attempts.get(user , 0) + 1

     if failed_attempts[user] == 3:
        print(f"ALERT: {user} has 3 failed attempts")
        print("security check complete")