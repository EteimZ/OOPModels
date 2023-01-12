from dataclasses import dataclass

@dataclass
class Todo:
    id: int | None
    descr: str
    status: bool

class Model:

    def __init__(self):
        self.todos: list[Todo] = []
        self.id = 0

    def add(self, todo: Todo):
        if todo.id == None:
            todo.id = self.id
            self.increment()
        self.todos.append(todo)

    def remove(self, id: int ):
        id -= 1
        part_1 = self.todos[0:id]
        part_2 = self.todos[id+1:]
        self.todos = part_1 + part_2

    def get_data(self):
        return self.todos

    def increment(self):
        self.id += 1
'''
    def get(self, id: int):
        print(id)
        id -= 1
        print(id)
        return self.todos[id]
'''

class View:

    def display(self, data: list[Todo]):
        print("id    | description | status")
        for i in data:
            print(f"{i.id} | {i.descr} | {i.status} ")


class Controller:

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
    
    def update_view(self):
        data = self.model.get_data()
        self.view.display(data)
    
    def add_data(self, todo: Todo):
        self.model.add(todo)
        self.update_view()

    def remove_data(self, id: int):
        self.model.remove(id)
        self.update_view()
    
    def update_data(self):
        "Add update logic"
        pass

    def list_data(self):
        data = self.model.get_data()
        self.view.display(data)

class Application:
    
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
                descr = input("Add Description: ")
                status = input("Add Status: ")
                status = False if status == "False" else True 
                todo = Todo(id=None, descr=descr, status=status)
                self.c.add_data(todo)

            elif n == 3:
                id = input("Select Id: ")
                self.c.remove_data(int(id))
            
            elif n == 4:
                self.info()
            
            n = int(input("Select another option: "))

    def info(self):
        print("Welcome to TodoMVC")
        print("1. To display todos")
        print("2. To add todo")
        print("3. To delete todo")
        print("4. To display this info")
        print("0. To exit")

# Todo: properly abstract status option

if __name__ == '__main__':
    m = Model()
    v = View()
    c = Controller(m, v)

    app = Application(m, v, c)

    try:
        app.main_loop()
    except KeyboardInterrupt:
        print("Exiting")