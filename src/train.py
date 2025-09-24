# /src/train.py

class _Car:
    __slots__ = ("id", "prev", "next")

    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None


class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        node = _Car(car_id)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def attach_back(self, car_id):
        node = _Car(car_id)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def detach_front(self):
        if not self.head:
            return None
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # list became empty
        return node.id

    def detach_back(self):
        if not self.tail:
            return None
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None  # list became empty
        return node.id

    def detach(self, car_id):
        node = self.head
        while node:
            if node.id == car_id:
                prev_node = node.prev
                next_node = node.next
                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                return True
            node = node.next
        return False

    def to_list(self):
        result = []
        node = self.head
        while node:
            result.append(node.id)
            node = node.next
        return result
