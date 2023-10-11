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
                result[2] += order.workload

        for order in self.unfinished_orders():
            if order.programmer == programmer:
                result[1] += 1
                result[3] += order.workload

        return tuple(result)
