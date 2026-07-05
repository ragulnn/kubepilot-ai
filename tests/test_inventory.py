from kubernetes import config

from state_engine.manager import StateManager

from inventory_engine.manager import InventoryManager
from inventory_engine.summary import InventorySummary

config.load_kube_config()

state = StateManager().refresh()

inventory = InventoryManager().build(

    state

)

summary = InventorySummary().summarize(

    inventory

)

print(summary)
