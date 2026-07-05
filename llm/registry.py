PROVIDERS = {}


def register_provider(cls):

    provider = cls()

    PROVIDERS[provider.name] = provider

    return cls
