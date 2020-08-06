class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashLinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def add_to_head(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        # Create previous instance of the current head
        current = self.head

        # Check if head is empty and if so return None
        if current is None:
            return None

        # Check for the key of the head
        elif current.key == key:
            self.head = current.next
            return current

        # Cycle through any other part getting deleted
        else:
            previous = current
            current = current.next

            while current is not None:
                if current.key == key:
                    previous.next = current.next
                    return current

                else:
                    previous = current
                    current = current.next
            return None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.count = 0

        # Cycle through the capacity and pushing them through the HashLinkedList class
        for i in range(self.capacity):
            self.hash_table[i] = HashLinkedList()

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # hash_value = self.hash_index(key)
        # self.hash_table[hash_value] = value

        # Create index of the hash key
        index = self.hash_index(key)
        # Create a current_node of the hash table to find the associated key
        current_node = self.hash_table[index].find(key)

        # Check if load factor is above 0.7 and if it is then double capacity size
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

        # Check if our current node exists and assign it to value
        if current_node:
            current_node.value = value
        # If not then add it to the head and add our count by 1
        else:
            self.hash_table[index].add_to_head(key, value)
            self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # hash_value = self.hash_index(key)
        # if self.hash_table[hash_value] == None:
        #     print("Warning: Key Does Not Exist!")
        # else:
        #     self.hash_table[hash_value] = None

        # Create index of hash
        index = self.hash_index(key)
        # Pass our current index through our delete method and pass the key to that method to remove from the table
        current_node = self.hash_table[index].delete(key)

        # Check if the current_node to delete exists and if not print warning message
        if current_node is None:
            print("Warning Key Does Not Exist")
        # If it exists subtract our total count
        else:
            self.count -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # hash_value = self.hash_index(key)
        # if self.hash_table[hash_value] == None:
        #     return None
        # else:
        #     return self.hash_table[hash_value]

        # Create index of our hash table
        index = self.hash_index(key)
        # Try to retrieve the current node using the find method in our LL class
        current_node = self.hash_table[index].find(key)

        # Check if current node exists and if not return None
        if current_node is None:
            return None
        # If current node exists return the value
        else:
            return current_node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # Create variable for our current table which will become our previous table
        prev_table = self.hash_table
        # Rehash the table using the new_capacity
        rehash_table = [None] * new_capacity

        # Cycle through the new capacity and pass each index to our LL class
        for i in range(new_capacity):
            rehash_table[i] = HashLinkedList()

        # Reassign our initial values of our previous __init__ function
        self.hash_table = rehash_table
        self.capacity = new_capacity
        self.count = 0

        # Cycle through our previous table and assign head to it
        for i in prev_table:
            head_value = i.head

            # Check if the head exists and put the values there with the put class along with reassigning the value of the head to the next index
            while head_value:
                self.put(head_value.key, head_value.value)
                head_value = head_value.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
