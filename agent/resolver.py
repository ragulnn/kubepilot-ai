class ResourceResolver:

    def resolve_pod(self, context, name):

        name = name.lower()

        for pod in context["pods"].splitlines():

            if name in pod.lower():
                return pod.split()[0]

        return None

    def resolve_namespace(self, context, pod):

        for line in context["pods"].splitlines():

            if pod in line:

                parts = line.split()

                return parts[0]

        return "default"
