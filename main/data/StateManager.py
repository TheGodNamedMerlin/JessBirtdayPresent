

class StateManager(object):

    def __init__(self, currentState):

        self.currentstate = currentState
        self.oldState = None

    def get_state_events(self, event):
        self.currentstate.get_events(event)

    def get_state_update(self, clock):
        self.currentstate.get_update(clock)

    def display_state_objects(self, window):
        self.currentstate.display_objects(window)

    def change_state(self, state):
        self.oldState = self.currentstate
        self.currentstate = state

    def change_check(self):
        check = self.currentstate.change_check()
        if check == False:
            pass
        else:
            self.change_state(check)


