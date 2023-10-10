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
        return set(task.programmer for task in self.all_orders())


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)
