from agents.tempo_agent import TempoAgent

print("=" * 60)
print("Tempo Agent")
print("=" * 60)

agent = TempoAgent()

trace_id = input("Trace ID: ").strip()

state = {
    "trace_id": trace_id
}

state = agent.run(state)

print(state)
