class BaseAgent:
    

    def can_act(self, bus):
       return False

    def act(self, bus):
       
        raise NotImplementedError("Agent must implement act()")
