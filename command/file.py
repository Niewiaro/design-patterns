import os

verbose = True


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if not os.path.exists(self.src):
            raise FileNotFoundError(f"Source file '{self.src}' does not exist")
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}']")
        try:
            os.rename(self.src, self.dest)
        except PermissionError:
            raise PermissionError(f"No permission to rename file '{self.src}'")

    def undo(self):
        if not os.path.exists(self.dest):
            raise FileNotFoundError(f"File '{self.dest}' does not exist")
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        try:
            os.rename(self.dest, self.src)
        except PermissionError:
            raise PermissionError(f"No permission to rename file '{self.dest}'")

    def can_be_undone(self):
        return True


def delete_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{path}' does not exist")
    if verbose:
        print(f"deleting file {path}")
    try:
        os.remove(path)
    except PermissionError:
        raise PermissionError(f"No permission to delete file '{path}'")


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        try:
            with open(self.path, mode='w', encoding='utf-8') as out_file:
                out_file.write(self.txt)
        except PermissionError:
            raise PermissionError(f"No permission to create file '{self.path}'")

    def undo(self):
        delete_file(self.path)

    def can_be_undone(self):
        return True


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File '{self.path}' does not exist")
        if verbose:
            print(f"[reading file '{self.path}']")
        try:
            with open(self.path, mode='r', encoding='utf-8') as in_file:
                print(in_file.read(), end='')
        except PermissionError:
            raise PermissionError(f"No permission to read file '{self.path}'")

    def can_be_undone(self):
        return False


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = (CreateFile(orig_name),
                ReadFile(orig_name),
                RenameFile(orig_name, new_name))
    try:
        [c.execute() for c in commands]
        answer = input('reverse the executed commands? [y/n] ')
        if answer not in 'yY':
            print(f"the result is {new_name}")
            exit()
        for c in reversed(commands):
            if c.can_be_undone():
                try:
                    c.undo()
                except (FileNotFoundError, PermissionError) as e:
                    print(f"Error during undo: {str(e)}")
            else:
                print(f"Command {c.__class__.__name__} cannot be undone")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    main()
