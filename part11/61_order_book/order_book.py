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


if __name__ == "__main__":
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)
