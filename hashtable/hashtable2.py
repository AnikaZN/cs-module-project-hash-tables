# A test to prove I can do it

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


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.load_factor = 0
        self.num_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Storage is a list, so we can check its len
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Default of 0
        return self.load_factor

    def update_load_factor(self):
        # How much available space is being consumed?
        self.load_factor = self.num_items/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
            hash = hash & 0xFFFFFFFF
            return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Take our arbitrary key and get a valid index
        index = self.hash_index(key)

        # If that index doesn't actually exist
        if self.storage[index] == None:
            # Insert our key and value at that index
            self.storage[index] = HashTableEntry(key, value)
            # Add 1 to our number of items to reflect the change
            self.num_items += 1
        # If the index does actually exist
        else:
            # Grab whatever is at the index
            node = self.storage[index]
            # Move through the list until we're at the right place
            while node.key != key and node.next is not None:
                node = node.next

            # When the key matches
            if node.key == key:
                # Set the value to be the given value
                node.value = value
            # If the key doesn't match, create a new one
            else:
                node.next = HashTableEntry(key, value)
                # Add 1 to our number of items to reflect the change
                self.num_items += 1

        # Check how much space we're using
        self.update_load_factor()
        # If it's more the 70%, resize it
        if self.load_factor > 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Take our arbitrary key and get a valid index
        index = self.hash_index(key)

        # If it doesn't exist
        if self.storage[index] == None:
            print('Warning! Key not found!')
            return None
        # If it does exist
        else:
            # Grab whatever it is at the index
            node = self.storage[index]
            # Establish a "previous" node
            prev = None

            # Move through the list until we're at the right place
            while node.key != key and node.next is not None:
                prev = node
                node = node.next

            # When we're at the right place
            if node.key == key:
                # If we're still where we started
                if prev == None:
                    # Move to the next node
                    self.storage[index] = node.next
                # If we're not where we started
                else:
                    # We skip the current node
                    prev.next = node.next

                # Remove 1 from our number of items to reflect the change
                self.num_items -= 1

                # Check how much space we're using
                self.update_load_factor()
                # If we're using less then 20% and the list capacity is 16+
                if self.load_factor < .20 and self.capacity >= 16:
                    # Resize it down to half of our current capacity
                    self.resize(self.capacity // 2)

                # Give back the value we just deleted
                return node.value

            # If the key doesn't exist
            else:
                print('Warning! Key not found!')

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Take our arbitrary key and get a valid index
        index = self.hash_index(key)

        # If there's nothing there, say so
        if self.storage[index] == None:
            return None
        # If there is something there
        else:
            # Grab whatever it is at the index
            node = self.storage[index]
            # Move through the list until we're at the right place
            while node.key != key and node.next is not None:
                node = node.next

            # When we're at the right place
            if node.key == key:
                # Return the value
                return node.value
            # Or return None
            else:
                return None

    def resize(self, new_capacity=None):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Get our storage as it currently exists
        old_storage = self.storage

        # If no specific capacity is given
        if new_capacity is None:
            # Set capacity to double the required size
            new_capacity = len(self.storage) * 2

        # Re-create our storage with the new length
        self.storage = [None] * new_capacity
        # Re-create our capacity as we calculated it
        self.capacity = new_capacity

        # For each item in our old storage
        for node in old_storage:
            # As long as the value is something
            while node is not None:
                # Stick the value into the new storage
                self.put(node.key, node.value)
                # Subtract 1 from our size
                self.num_items -= 1
                # Move on to the next node
                node = node.next

        # Check how much space we're consuming
        self.update_load_factor()



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
