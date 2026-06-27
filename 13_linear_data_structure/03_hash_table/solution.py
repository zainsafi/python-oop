class HashTable:
    def __init__(self):
        # Stores hashed values as keys and nested dictionaries as values
        self.collection = {}

    def hash(self, key: str):
        # Sum Unicode values of each character
        return sum(ord(char) for char in key)

    def add(self, key, value):
        # Get hash index
        index = self.hash(key)

        # If hash index does not exist, create a nested dictionary
        if index not in self.collection:
            self.collection[index] = {}

        # Store key-value pair inside the nested dictionary
        self.collection[index][key] = value

    def remove(self, key):
        # Get hash index
        index = self.hash(key)

        # Check if hash index exists
        if index in self.collection:
            # Check if the actual key exists inside the nested dictionary
            if key in self.collection[index]:
                del self.collection[index][key]

                # Remove empty hash bucket
                if not self.collection[index]:
                    del self.collection[index]

    def lookup(self, key):
        # Get hash index
        index = self.hash(key)

        # Check if hash index and key exist
        if index in self.collection:
            if key in self.collection[index]:
                return self.collection[index][key]

        # Key not found
        return None
    

table = HashTable()

table.add("golf", "sport")

print(table.collection)
# {424: {'golf': 'sport'}}

print(table.lookup("golf"))
# sport

print(table.lookup("tennis"))
# None


