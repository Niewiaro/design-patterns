from abc import ABC, abstractmethod
from pathlib import Path
import hashlib
import hmac
import os  # needed for os.urandom


def hash_password(password: str, salt: bytes = None) -> tuple[bytes, bytes]:
    """
    Hashes a password using PBKDF2-HMAC with SHA-256 and a salt.

    Args:
        password: The plaintext password.
        salt: Optional salt value. If not provided, generates a new 16-byte salt.

    Returns:
        A tuple of (salt, hashed_password).
    """
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        200_000
    )
    return salt, hashed


def save_password(salt: bytes, hashed: bytes, filename: str = 'password.dat'):
    """
    Saves the salt and hashed password to a file.

    Args:
        salt: The salt used for hashing.
        hashed: The hashed password.
        filename: The file to store the combined data.
    """
    Path(filename).write_bytes(salt + hashed)


def load_password(filename: str = 'password.dat') -> tuple[bytes, bytes]:
    """
    Loads the salt and hashed password from a file.

    Args:
        filename: The file to read the data from.

    Returns:
        A tuple of (salt, hashed_password).
    """
    data = Path(filename).read_bytes()
    return data[:16], data[16:]


def verify_password(input_password: str, salt: bytes, hashed: bytes) -> bool:
    """
    Verifies that the input password, when hashed with the same salt,
    matches the stored hash.

    Args:
        input_password: The password entered by the user.
        salt: The salt used during original hashing.
        hashed: The stored hashed password.

    Returns:
        True if the hashes match, False otherwise.
    """
    new_hash = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 200_000)
    return hmac.compare_digest(new_hash, hashed)


class ISensitiveInfo(ABC):
    """
    Abstract base class defining an interface for sensitive operations.
    """

    @abstractmethod
    def read(self):
        """Reads the current user list."""
        pass

    @abstractmethod
    def add(self, user):
        """Adds a new user to the list."""
        pass

    @abstractmethod
    def remove(self, user):
        """Removes a user from the list."""
        pass


class SensitiveInfo(ISensitiveInfo):
    """
    Class that holds sensitive user information. Access is protected via proxy.
    Implements Singleton pattern and blocks direct instantiation.
    """
    __instance = None

    def __init__(self):
        if not getattr(self, '_created_by_proxy', False):
            raise RuntimeError("Use Info proxy to access SensitiveInfo")
        self.users = ['nick', 'tom', 'ben', 'mike']

    @classmethod
    def _create(cls):
        """
        Factory method to create a singleton instance, only allowed internally.
        """
        if cls.__instance is None:
            obj = cls.__new__(cls)
            obj._created_by_proxy = True
            cls.__init__(obj)
            cls.__instance = obj
        return cls.__instance

    def read(self):
        """Prints the current list of users."""
        print(f"There are {len(self.users)} users: {' '.join(self.users)}")

    def add(self, user):
        """Adds a new user to the list."""
        self.users.append(user)
        print(f'Added user {user}')

    def remove(self, user):
        """Removes a user from the list."""
        if user in self.users:
            self.users.remove(user)
            print(f'Removed user {user}')
        else:
            print(f'User {user} not found')



class Info(ISensitiveInfo):
    """
    Protection Proxy class for accessing SensitiveInfo.
    Verifies password before allowing sensitive operations.
    """

    def __init__(self):
        self.protected = SensitiveInfo._create()
        self.password_file = Path("password.dat")

        if not self.password_file.exists():
            print("No password set. Please create a new one.")
            pw = input("New password: ")
            salt, hashed = hash_password(pw)
            save_password(salt, hashed)
            print("Password saved.")
        self.salt, self.hashed = load_password()

    def read(self):
        """Delegates read operation to the protected SensitiveInfo object."""
        self.protected.read()

    def add(self, user):
        """
        Requests password verification before adding a new user.
        """
        pw = input('Enter password: ')
        if verify_password(pw, self.salt, self.hashed):
            self.protected.add(user)
        else:
            print("Incorrect password!")

    def remove(self, user):
        """
        Requests password verification before removing a user.
        """
        pw = input('Enter password: ')
        if verify_password(pw, self.salt, self.hashed):
            self.protected.remove(user)
        else:
            print("Incorrect password!")


def main():
    """
    Entry point for the application. Offers a simple CLI menu to access info.
    """
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. remove user |==| 4. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            name = input('enter username to remove: ')
            info.remove(name)
        elif key == '4':
            print("Bye!")
            break
        else:
            print(f'unknown option: {key}')


if __name__ == "__main__":
    main()
