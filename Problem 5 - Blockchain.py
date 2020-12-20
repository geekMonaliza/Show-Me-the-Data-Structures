import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None


    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(self.data.encode('utf-8'))

        return sha.hexdigest()

    def __repr__(self):
        return str(self.timestamp) + '|' + str(self.data) + '|' + str(self.hash) + '|' + str(self.previous_hash)

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if not data:
            return
        if self.head == None:
            new_node = Block(datetime.datetime.utcnow(), data, 0)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Block(datetime.datetime.utcnow(), data, self.tail.hash)
            self.tail.next = new_node
            self.tail = new_node

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node)
            node = node.next
        return out


# Testcase1
bc1 = Blockchain()

bc1.append("First Node")
bc1.append("")
bc1.append("Second Node")

print(bc1.to_list())  # prints 2 nodes that have data

# Testcase2
bc2 = Blockchain()

bc2.append(None)
bc2.append("")
bc2.append(False)

print(bc2.to_list())    # prints empty list

# Testcase3
bc3 = Blockchain()

bc3.append("Node 1")
bc3.append("Node 2")
bc3.append("Node 3")

print(bc3.to_list())    # prints list of three Nodes
