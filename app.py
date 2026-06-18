from tools.pods import get_pods


def main():
    print("=" * 50)
    print("🤖 KubePilot AI")
    print("=" * 50)

    pods = get_pods()
    print(pods)


if __name__ == "__main__":
    main()
