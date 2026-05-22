# custom shopping Cart example

class Cart:

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

            print(f'{item} is not in Cart.')

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

        return f'Cart items -> {self.items}'


# creating object
Cart = Cart()

# adding items
Cart.add('laptop')
Cart.add('wireless mouse')
Cart.add('keyboard')
Cart.add('monitor')


# using __iter__

print('\n----- __iter__ method -----\n')

for item in Cart:

    print(item)


# using __len__

print('\n----- Cart length -----\n')

print(len(Cart))


# using __getitem__

print('\n----- indexing -----\n')

print(Cart[0])
print(Cart[2])


# using __contains__

print('\n----- contains method -----\n')

print('monitor' in Cart)
print('phone' in Cart)


# using __str__

print('\n----- string representation -----\n')

print(Cart)


# removing items

print('\n----- remove items -----\n')

Cart.remove('keyboard')

print(Cart)

Cart.remove('phone')



print(dir(Cart))