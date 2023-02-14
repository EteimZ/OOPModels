class EventEmitter:

    def __init__(self):
        self.events: dict = {}

    def on(self, event_name: str, callback):
        """
        Listen to event
        """
        if callable(callback):
            self.events[event_name] = callback
        else:
            raise Exception("Callback should be a callable")

    def emit(self, event_name, *arg):
        """
        Trigger event
        """

        try:
            if len(arg) == 0:
                self.events[event_name]()
            self.events[event_name](*arg)
        except KeyError:
            print(f"{event_name} event doesn't exist")

if __name__ == "__main__":
    e = EventEmitter()
    e.on("add", lambda x, y : print(x + y))
    e.on("sub", lambda x, y : print(x - y))
    e.emit("add", 2, 3)
    e.emit("sub", 5, 2)
    e.emit("prin")
