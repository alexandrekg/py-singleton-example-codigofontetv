class HostgatorInfluenciadores:
    _instance = None
    members = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_members(self, member) -> []:
        self.members.append(member)
