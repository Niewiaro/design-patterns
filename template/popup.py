def popup(msg: str) -> None:
    import win32api
    win32api.MessageBox(0, msg, "Popup", 0x00001000)

def popup_thread(items: list[str] | str) -> None:
    import threading

    threads = []
    for item in items:
        def thread_func(it=item):
            popup(it)
            # Recurse only if it is not a single character
            if isinstance(it, str) and len(it) > 1:
                popup_thread(it)
        t = threading.Thread(target=thread_func)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def main() -> None:
    user_input = input("Enter a message: ")
    words = user_input.split()
    if words:
        popup_thread(words)

if __name__ == "__main__":
    main()
