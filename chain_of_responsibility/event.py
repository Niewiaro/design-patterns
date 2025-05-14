class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = f'handle_{event}'
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent is not None:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        from win32api import MessageBox
        from win32con import MB_YESNO, MB_ICONQUESTION
        from win32con import IDYES

        print(f'MainWindow: {event}')
        result = MessageBox(
            0,
            "Do you really want to quit?",
            "Are you sure?",
            MB_YESNO | MB_ICONQUESTION
        )
        if result == IDYES:
            import sys
            sys.exit(0)

    def handle_default(self, event):
        print(f'MainWindow Default: {event}')


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f'SendDialog: {event}')


class MsgText(Widget):
    def handle_down(self, event):
        print(f'MsgText: {event}')


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print(f'Sending event -{evt}- to MainWindow')
        mw.handle(evt)
        print(f'Sending event -{evt}- to SendDialog')
        sd.handle(evt)
        print(f'Sending event -{evt}- to MsgText')
        msg.handle(evt)


if __name__ == "__main__":
    main()
