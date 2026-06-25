import time


class Timer:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()

        print()
        print("=" * 60)
        print(f"🚀 {self.name}")
        print("=" * 60)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start

        print("-" * 60)
        print(f"⏱ {self.name} Time : {elapsed:.2f} sec")
        print("=" * 60)
        print()
