from node import Node

class MedianStore:
    count = 0
    index_values = {}
    value_index = {}
    root = None

    def add_number(self, number: int):
        node = Node('{}-{}'.format(self.count, number), number)
        if self.root == None:
            self.root = node
            self.index_values[self.count] = node
            self.value_index[node.label] = self.count
        else:
            appended_node = self.root.add_node(node)
            index_of_append_node = self.value_index[appended_node.label]
            if appended_node.value < number:
                if index_of_append_node < self.count - 1:
                    self.shift_index(index_of_append_node + 1)
                self.index_values[index_of_append_node + 1] = node
                self.value_index[node.label] = index_of_append_node + 1
            else:
                self.shift_index(index_of_append_node)
                self.index_values[index_of_append_node] = node
                self.value_index[node.label] = index_of_append_node

        self.count += 1

    def shift_index(self, from_index):
        t1 = self.index_values[from_index]
        t2 = None
        for i in range(from_index, self.count):
            if i < self.count - 1:
                t2 = self.index_values[i + 1]
            self.index_values[i + 1] = t1
            t1 = t2
            self.value_index[self.index_values[i].label] += 1

    def get_median(self):
        if self.count == 1:
            return self.index_values[self.count - 1].value
        center = int(self.count/2)
        if int(self.count % 2) == 0:
            return (self.index_values[center].value + self.index_values[center-1].value)/2
        else:
            return self.index_values[center].value

def main():
    median_store = MedianStore()
    median_store.add_number(7)
    median_store.add_number(3)
    median_store.add_number(6)
    median_store.add_number(4)
    median_store.add_number(2)
    median_store.add_number(2)
    median_store.add_number(5)

    print('median:', median_store.get_median())

    #for i in range(0, median_store.count):
    #    print(median_store.index_values[i].value)


if __name__ == "__main__":
    main()
