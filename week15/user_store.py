import os
import sqlite3
import json

class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def _get_connection(self):
        
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    data TEXT
                )
            """)
            conn.commit()

    def load(self):
        
        with self._get_connection() as conn:
            cursor = conn.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            
            return [dict(row) for row in rows]

    def save(self, user_dict):
        
        with self._get_connection() as conn:
            conn.execute("""
                INSERT INTO users (id, name, email) 
                VALUES (?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    name=excluded.name,
                    email=excluded.email
            """, (user_dict['id'], user_dict['name'], user_dict['email']))
            conn.commit()

    def find_by_id(self, user_id):
       
        with self._get_connection() as conn:
            cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    
    def update_user(self, user_id, updated_data):
       
        if not updated_data:
            return False
            
        keys = updated_data.keys()
        set_clause = ", ".join([f"{key} = ?" for key in keys])
        values = list(updated_data.values())
        values.append(user_id)

        with self._get_connection() as conn:
            cursor = conn.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id):
        
        with self._get_connection() as conn:
            cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0