class Turn:
    def __init__(self, agents):
        self._agents = agents

    @property
    def agent(self):
        return self._agents[0]

    def switch_turn(self):
        self._agents.reverse()
