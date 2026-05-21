# custom shopping cart example

class cart:

    def __init__(self):

        self.items = []

    # normal method
    def add(self, item):

        self.items.append(item)

    # normal method
    def remove(self, item):

        if item in self.items:

            self.items.remove(item)

        else:

            print(f'{item} is not in cart.')

    # special method for len()
    def __len__(self):

        return len(self.items)

    # special method for indexing
    def __getitem__(self, index):

        return self.items[index]

    # special method for "in" keyword
    def __contains__(self, item):

        return item in self.items

    # special method for loops
    def __iter__(self):

        return iter(self.items)

    # special method for print()
    def __str__(self):

        return f'cart items -> {self.items}'


# creating object
cart = cart()

# adding items
cart.add('laptop')
cart.add('wireless mouse')
cart.add('keyboard')
cart.add('monitor')


# using __iter__

print('\n----- __iter__ method -----\n')

for item in cart:

    print(item)


# using __len__

print('\n----- cart length -----\n')

print(len(cart))


# using __getitem__

print('\n----- indexing -----\n')

print(cart[0])
print(cart[2])


# using __contains__

print('\n----- contains method -----\n')

print('monitor' in cart)
print('phone' in cart)


# using __str__

print('\n----- string representation -----\n')

print(cart)


# removing items

print('\n----- remove items -----\n')

cart.remove('keyboard')

print(cart)

cart.remove('phone')

