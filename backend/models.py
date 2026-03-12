class TodoModel:
    def __init__(self, id: int, title: str, is_done: bool = False):
        self.id = id
        self.title = title
        self.is_done = is_done

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "is_done": self.is_done
        }