class show:
    version = 1.0
    @classmethod
    def shown(cls):
        return f"version is {cls.version}"
print(show.shown())