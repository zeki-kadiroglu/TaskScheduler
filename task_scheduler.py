from src.node_tree import TreeNode
from src.search.deep_first_search import DeepFirstSearch


class TaskScheduler:
    def __init__(self):
        self.root = DeepFirstSearch("Root")
        self.tasks = {}
    def add_task(self, name, dependencies=None, duration=1, ):
        if dependencies is None:
            dependencies = []
        if name in self.tasks:
            raise ValueError(f'Task "{name}" already exists.')
        self.tasks[name] = {'dependencies': dependencies,
                            'duration': duration}
        self.root.root.add_child(TreeNode(self.tasks[name]))


    def schedule_tasks(self):
        current_time = 0
        schedule = []

        for task in self.root.iterate_tasks():
            if task != "Root":
                schedule.append(f'{task} starts at {current_time} and lasts {task["duration"]} unit(s)')
                current_time += task["duration"]



        return schedule


if __name__ == "__main__":

    # Example Usage:
    scheduler = TaskScheduler()
    # Adding tasks with dependencies and durations
    scheduler.add_task("A")
    scheduler.add_task("B", ["A"])
    scheduler.add_task("C", ["A"])
    scheduler.add_task("D", ["B", "C"])
    scheduler.add_task("E", ["D"])

    # Adding a task with a circular dependency (uncomment to test)
    # scheduler.add_task("F", ["F"])

    try:
        scheduled_tasks = scheduler.schedule_tasks()
        print("Scheduled Tasks:", scheduled_tasks)
    except ValueError as error:
        print(error)
