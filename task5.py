"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
##############################################################################################
"""Сложность: O(1)"""
from LinkedList import LinkedList


class LinkedStack(object):

    def __init__(self, iterable=None):
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        self.list.prepend(item)

    def peek(self):
        head = self.list.head
        return None if head is None else head.data

    def pop(self):

        head = self.peek()
        self.list.delete(head)
        return head


##############################################################################################
""""Сложность: O(n)"""


class ArrayStack(object):

    def __init__(self, iterable=None):
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, item):
        self.list.append(item)

    def peek(self):
        last_item_idx = len(self.list) - 1
        return None if last_item_idx < 0 else self.list[last_item_idx]

    def pop(self):
        if self.peek() == None:
            raise ValueError("list is empty")
        else:
            return self.list.pop()


###########################################################################################
"""Сложность )(1)"""


class Stacks:
    def __init__(self):
        self.stacks = []
        self.noOfStacks = 0
        self.itemsOnStack = 0

    def dev(self):
        self.stacks.append(Stack())
        # if len(self.stacks) != 0:
        # self.noOfStacks += 1

    def push(self, item):

        if self.itemsOnStack > 3:
            self.dev()
        else:
            self.itemsOnStack += 1
            self.stacks[self.noOfStacks].push(item)

    def pop(self, stackNo):
        return self.stacks(noOfStacks).pop()

    def size(self):
        return len(self.stacks)

    def printtack(self, index):
        print(self.stacks[index].size())
        self.stacks[index].printStack()


stacky = Stacks()
stacky.dev()
stacky.push(3)
stacky.printtack(0)
