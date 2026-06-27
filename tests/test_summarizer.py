from agent.summarizer import Summarizer

observations = [
    {
        "tool":"pods",
        "result":"""
default nginx Running
default redis Running
default mysql Running
default api Running
default worker Running
"""
    }
]

s = Summarizer()

print(s.summarize(observations))
