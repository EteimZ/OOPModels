from dataclasses import dataclass

@dataclass
class Todo:

    """
    dataclass to represent individual todos
    """

    id: int | None
    descr: str
    status: bool

class Model:

    """
    Model class that stores all todos.
    """

    def __init__(self):
        self.todos: dict[int, Todo] = {}
        self.id = 0

    def add(self, todo: Todo):
        if todo.id == None:
            todo.id = self.id
            self.increment()
        self.todos[todo.id] = todo

    def remove(self, id: int ):
        del self.todos[id]

    def update(self, id: int , descr: str, status: bool):
        self.todos[id].descr = descr
        self.todos[id].status = status

    def get(self):
        return self.todos

    def increment(self):
        self.id += 1


class View:

    """
    View class that handles user display
    """

    def display(self, todos: dict[int, Todo]):
        print(f"{'id'}|{'description':^40}|status")
        for todo in todos.items():
            print(f"{todo[0]} | {todo[1].descr:40} | {todo[1].status} ")


class Controller:

    """
    Controller class that connects model to view
    """

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
    
    def update_view(self):
        todos = self.model.get()
        self.view.display(todos)
    
    def add_data(self, todo: Todo):
        self.model.add(todo)
        self.update_view()

    def remove_data(self, id: int):
        self.model.remove(id)
        self.update_view()
    
    def update_data(self, id:int, descr: str, status: bool):
        self.model.update(id, descr, status)
        self.update_view()

    def list_data(self):
        todos = self.model.get()
        self.view.display(todos)

class Application:

    """
    Application that uses the MVC architecture
    """
    
    def __init__(self, model: Model, view: View, ctrl: Controller) -> None:
        self.m = model
        self.v = view
        self.c = ctrl

 
    def main_loop(self):
        self.info()

        n = int(input("Select an option: "))


        while n != 0:
            if n == 1:
                self.c.list_data()

            elif n == 2:
                descr = input("Type Description: ")
                todo = Todo(id=None, descr=descr, status=False)
                self.c.add_data(todo)

            elif n == 3:
                id = input("Select Id: ")
                self.c.remove_data(int(id))

            elif n == 4:
                id = int(input("Select Id: "))
                descr = str(input("Update description: "))
                status = int(input("Update status(0 for False & 1 for True): "))
                if status == 1: 
                    status = True
                else: 
                    status = False
                self.c.update_data(id, descr, status)

            elif n == 5:
                self.info()
            
            n = int(input("Select another option: "))

    def info(self):
        print("Welcome to TodoMVC")
        print("1. To display todos")
        print("2. To add todo")
        print("3. To delete todo")
        print("4. To update todo")
        print("5. To display this info")
        print("0. To exit")


# Todos: Refactor the code and handle edge cases(when a user tries to update or delete non existing todos)

if __name__ == '__main__':
    m = Model()
    v = View()
    c = Controller(m, v)

    app = Application(m, v, c)

    try:
        app.main_loop()
    except KeyboardInterrupt:
        print("Exiting")