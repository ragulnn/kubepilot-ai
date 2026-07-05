from resolver.resource_resolver import ResourceResolver

resolver = ResourceResolver()

resolver.load({

    "pods":[

        {

            "kind":"Pod",

            "name":"nginx-abc",

            "namespace":"default",

        }

    ],

    "deployments":[

        {

            "kind":"Deployment",

            "name":"frontend",

        }

    ]

})

print()

print(resolver.resolve("nginx"))

print()

print(resolver.resolve("front"))
