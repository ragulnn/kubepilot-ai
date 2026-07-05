from learning_engine.learner import InvestigationLearner

history = [

    {

        "actions":[

            "logs",

            "metrics",

        ]

    },

    {

        "actions":[

            "logs",

        ]

    },

    {

        "actions":[

            "logs",

            "traces",

        ]

    },

]

learner = InvestigationLearner()

print(

    learner.learn(

        history

    )

)
