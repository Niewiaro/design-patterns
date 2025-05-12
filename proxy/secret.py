from abc import ABC, abstractmethod


class ISensitiveInfo(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add(self, user):
        pass


class SensitiveInfo(ISensitiveInfo):
    __instance = None

    def __init__(self):
        if not getattr(self, '_created_by_proxy', False):
            raise RuntimeError("Use Info proxy to access SensitiveInfo")
        self.users = ['nick', 'tom', 'ben', 'mike']

    @classmethod
    def _create(cls):
        if cls.__instance is None:
            obj = cls.__new__(cls)
            obj._created_by_proxy = True
            cls.__init__(obj)
            cls.__instance = obj
        return cls.__instance

    def read(self):
        print(f"There are {len(self.users)} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')


class Info(ISensitiveInfo):
    """Protection Proxy to SensitiveInfo"""

    def __init__(self):
        self.secret = '0xdeadbeef'
        self.protected = SensitiveInfo._create()

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        if sec == self.secret:
            self.protected.add(user)
        else:
            print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == "__main__":
    main()
