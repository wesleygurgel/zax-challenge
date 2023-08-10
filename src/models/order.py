class Order:
    def __init__(self, store, value):
        self.store = store
        self.value = value

    def commission(self):
        return self.store.commission_fee * self.value
