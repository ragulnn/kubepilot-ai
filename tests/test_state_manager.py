from state_engine.manager import StateManager

manager = StateManager()

state = manager.refresh()

print(state)

print(manager.current())
