from providers.kubernetes_provider import PodsTool

pods = PodsTool().run()

print(type(pods))

print()

print(pods[0])
