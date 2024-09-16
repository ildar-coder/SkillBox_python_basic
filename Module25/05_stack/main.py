# TODO здесь писать код
class TaskManager:
    def __init__(self):
        self.__stack = []

    def display_result(self):
        print("Результат:")
        sorted_stack = sorted(self.__stack, key=lambda item: item[1])
        result = {}
        for el in sorted_stack:
            if el[1] not in result:
                result[el[1]] = [el[0]]
            else:
                result[el[1]].append(el[0])

        for key, value in result.items():
            print(f"{key} {'; '.join(value)}")

    def new_task(self, task: str, priority: int):
        self.__stack.append((task, priority))

    def remove_task(self):
        if len(self.__stack) == 0:
            return None
        else:
            removed_task = self.__stack.pop()
            return removed_task

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return f"{self.stack}"

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            removed_item = self.stack.pop()
            return removed_item


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager.remove_task())
manager.display_result()

st = Stack()
print(st.stack)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st)
st.pop()
print(st)
st.pop()
print(st)
print(st.pop())
print(st)
print(st.pop())
print(st)
print(st.pop())


