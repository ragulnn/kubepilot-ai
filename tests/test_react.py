import tools.pods
import tools.services
import tools.events
import tools.nodes
import tools.namespaces

from agent.react import KubernetesAgent

agent = KubernetesAgent()

question = input("Question: ")

answer = agent.investigate(question)

print("\nAI Analysis\n")

print(answer)
