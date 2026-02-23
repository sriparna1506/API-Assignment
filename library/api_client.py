from utils.config import BASE_URL
from utils.retry import retry

class APIClient:
    def __init__(self, session):
        self.session = session
    @retry
    def get_all_posts(self):
        return self.session.get(f"{BASE_URL}/posts")
    @retry
    def get_post_by_id(self, post_id):
        return self.session.get(f"{BASE_URL}/posts/{post_id}")
    @retry
    def create_post(self, data):
        return self.session.post(f"{BASE_URL}/posts", json=data)
    @retry
    def update_post(self, post_id, data):
        return self.session.put(f"{BASE_URL}/posts/{post_id}", json=data)
    @retry
    def delete_post(self, post_id):
        return self.session.delete(f"{BASE_URL}/posts/{post_id}")
    @retry
    def get_all_users(self):
        return self.session.get(f"{BASE_URL}/users")
    @retry
    def get_all_comments(self):
        return self.session.get(f"{BASE_URL}/comments")
    @retry
    def get_post_comments(self, post_id):
        return self.session.get(f"{BASE_URL}/posts/{post_id}/comments")