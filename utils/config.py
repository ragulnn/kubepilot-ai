import os
from dotenv import load_dotenv

load_dotenv()

# Planner Model (fast)
PLANNER_MODEL = "qwen2.5:3b"

# Analyzer Model (accurate)
ANALYZER_MODEL = "qwen2.5:7b"

# Embedding / Memory (future)
EMBEDDING_MODEL = "nomic-embed-text"
