class Task:
    __id = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = False
        self.id = self.__update_id()

    def __update_id(self):
        Task.__id += 1
        return Task.__id

    def is_finished(self):
        return self.status

    def mark_finished(self):
        self.status = True

    def get_status(self):
        return "FINISHED" if self.is_finished() else "NOT FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.get_status()}"


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description=description, programmer=programmer, workload=workload)
        self.tasks.append(task)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set(task.programmer for task in self.all_orders()))

    def valid_programmer(self, programmer: str):
        if not programmer in self.programmers():
            raise ValueError

    def valid_id(self, id: int):
        if id not in [order.id for order in self.all_orders()]:
            raise ValueError

    def mark_finished(self, id: int):
        self.valid_id(id=id)

        for order in self.all_orders():
            order.mark_finished() if order.id == id else None

    def finished_orders(self):
        return [order for order in self.all_orders() if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.all_orders() if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        self.valid_programmer(programmer=programmer)

        result = [0, 0, 0, 0]

        for order in self.finished_orders():
            if order.programmer == programmer:
                result[0] += 1
                result[2] += int(order.workload)

        for order in self.unfinished_orders():
            if order.programmer == programmer:
                result[1] += 1
                result[3] += int(order.workload)

        return tuple(result)


class AppInterface:
    def __init__(self):
        self.order_book = OrderBook()

    def input_commands(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def input_add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split(" ")
        self.order_book.add_order(
            description=description, programmer=programmer, workload=workload
        )
        print("added!")

    def list_finished_orders(self):
        orders = self.order_book.finished_orders()
        [print(order) for order in orders] if orders else print("no finished tasks")

    def list_unfinished_orders(self):
        orders = self.order_book.unfinished_orders()
        [print(order) for order in orders] if orders else print("no tasks")

    def input_finished_order(self):
        id = int(input("id: "))
        self.order_book.mark_finished(id=id)
        print("marked as finished")

    def list_programmers(self):
        for programmer in self.order_book.programmers():
            print(programmer)

    def list_programmer_status(self):
        status = input("programmer: ")
        status = self.order_book.status_of_programmer(status)
        print(f"tasks: finished {status[0]}", end=" ")
        print(f"not finished {status[1]},", end=" ")
        print(f"hours: done {status[2]}", end=" ")
        print(f"scheduled {status[3]}")

    def run(self):
        self.input_commands()

        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            if command == "1":
                self.input_add_order()
            if command == "2":
                self.list_finished_orders()
            if command == "3":
                self.list_unfinished_orders()
            if command == "4":
                self.input_finished_order()
            if command == "5":
                self.list_programmers()
            if command == "6":
                self.list_programmer_status()


app = AppInterface()
app.run()
