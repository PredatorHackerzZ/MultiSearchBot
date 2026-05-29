# (c) MrAbhi2k3 and PredatorHackerzz
# https://github.com/PredatorHackerzZ/MultiSearchBot

import asyncio
from datetime import datetime
from typing import Optional, List, Dict

class UserDatabase:
    def __init__(self):
        self.users = {}
        self.search_history = {}
    
    async def add_user(self, user_id: int, username: str, chat_id: int, chat_type: str):
        if user_id not in self.users:
            self.users[user_id] = {
                "user_id": user_id,
                "username": username,
                "chat_id": chat_id,
                "chat_type": chat_type,
                "joined_at": datetime.now(),
                "searches": []
            }
    
    async def add_search(self, user_id: int, query: str, search_type: str, chat_id: int):
        if user_id not in self.search_history:
            self.search_history[user_id] = []
        
        self.search_history[user_id].append({
            "query": query,
            "type": search_type,
            "chat_id": chat_id,
            "timestamp": datetime.now()
        })
    
    async def get_user_searches(self, user_id: int, limit: int = 10) -> List[Dict]:
        if user_id in self.search_history:
            return self.search_history[user_id][-limit:]
        return []
    
    async def get_total_searches(self) -> int:
        total = 0
        for searches in self.search_history.values():
            total += len(searches)
        return total
    
    async def get_total_users(self) -> int:
        return len(self.users)

db = UserDatabase()
