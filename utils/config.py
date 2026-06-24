import os
from dotenv import load_dotenv

load_dotenv()

PLANNER_MODEL = os.getenv("PLANNER_MODEL", "qwen2.5:3b")
ANALYZER_MODEL = os.getenv("ANALYZER_MODEL", "qwen3:8b")
