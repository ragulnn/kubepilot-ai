import traceback
from cli.menu import Menu
from cli.display import Display

from agents.adaptive_pipeline import AdaptivePipeline


class CLIController:

    def __init__(self):

        self.menu = Menu()

        self.display = Display()

        self.pipeline = AdaptivePipeline()

    def run(self):

        while True:

            choice = self.menu.show()

            if choice == "1":

                self.display.title(
                    "Investigation"
                )

                question = input(
                    "Question: "
                ).strip()

                if not question:

                    print()
                    print("Question cannot be empty.")
                    continue

                state = {

                    "question": question

                }

                try:

                    state = self.pipeline.run(
                        state
                    )

                    self.display.title(
                        "FINAL STATE"
                    )

                    if not state:

                        print("Pipeline returned no data.")
                        continue

                    for key, value in state.items():

                        print()

                        print(key)

                        print("-" * 40)

                        print(value)
                except Exception:

                       print()

                       self.display.title(
                           "Pipeline Error"
                       )

                       traceback.print_exc()
            elif choice == "2":

                self.display.title(
                    "Fleet Dashboard"
                )

                print()

                print("Fleet Dashboard integration coming in the next integration phase.")

            elif choice == "3":

                self.display.title(
                    "Cluster Inventory"
                )

                print()

                print("Cluster Inventory integration coming in the next integration phase.")

            elif choice == "4":

                self.display.title(
                    "Goodbye"
                )

                print()

                print("Stopping Kubepilot...")

                break

            else:

                print()

                print("Invalid option. Please choose 1-4.")
