'''
Module for the TopNList data type
'''
from typing import Union
from cli.csv_parse import Record

class _DoublyLinkedList:
    def __init__(self, capacity: int):
        self.head :Union[_Node, None] = None
        self.tail : Union[_Node, None] = None
        self.capacity : int = capacity
        self.len : int = 0
    
class _Node:
    def __init__(self, data: Record):
        self.data : Record = data
        self.next : Union[_Node, None] = None
        self.prev : Union[_Node, None] = None

    def __next__(self):
        if self.next is None:
            raise StopIteration
        return self.next

class TopNList:
    '''
    Keeps a list of the top n elements. Adding to it either accomodates for the
    new element if it's greater than existing entries, otherwise it ignores it.
    '''
    def __init__(self, number):
        self._ordered_list = _DoublyLinkedList(number)

    def add(self, new_record: Record):
        '''
        Add a new record if it breaks into the top records
        '''

        # empty linked list
        if self._ordered_list.len == 0:
            self._ordered_list.tail = self._ordered_list.head = _Node(new_record)
            self._ordered_list.len = 1
            return

        runner = self._ordered_list.tail
        # find the insertion site
        # invariant after this loop: runner will be the node s.t. runner.data > new_record but runner.next.data is not
        # and if there is no such node (new_record is greater than all existing records) then runner is None
        while runner is not None and new_record > runner.data:
            runner = runner.prev
        
        new_node = _Node(new_record)
        if runner is None:
            # make new head and connect it to the previous linked list
            new_head = new_node
            new_head.next = self._ordered_list.head
            self._ordered_list.head.prev = new_head
            self._ordered_list.head = new_head
            if self._ordered_list.len < self._ordered_list.capacity:
                # leave the tail alone
                self._ordered_list.len += 1
            else:
                # move the tail up to its previous
                self._ordered_list.tail = self._ordered_list.tail.prev
                self._ordered_list.tail.next = None
        else:
            rest_of_list = runner.next
            if rest_of_list is None:
                if self._ordered_list.len < self._ordered_list.capacity:
                    runner.next = new_node
                    new_node.prev = runner
                    self._ordered_list.tail = new_node
                    self._ordered_list.len += 1
            else:
                new_node.next = rest_of_list
                new_node.prev = runner

                runner.next = new_node
                rest_of_list.prev = new_node

                if self._ordered_list.len == self._ordered_list.capacity:
                    # move the tail up
                    self._ordered_list.tail = self._ordered_list.tail.prev
                    self._ordered_list.tail.next = None
                else:
                    self._ordered_list.len += 1

    def __str__(self) -> str:
        runner = self._ordered_list.head
        result = f"(head: {runner.data._firstname}, tail: {self._ordered_list.tail.data._firstname}) " + runner.data.__str__() + " -> "
        runner = runner.next
        while runner is not None:
            result += f"{runner.data._firstname}, {runner.data._lastname} -> "
            runner = runner.next
        return result

    def __iter__(self):
        return self._ordered_list.head