class MessageBus:
    """
    Shared communication medium for agents.
    Agents publish data here and react to data produced by others.
    """

    def __init__(self):
        self.state = {}

    def publish(self, key, value):
        """
        Store data on the bus.
        """
        self.state[key] = value

    def read(self, key):
        """
        Read data from the bus.
        """
        return self.state.get(key)

    def has(self, key):
        """
        Check if a specific data item exists on the bus.
        """
        return key in self.state
