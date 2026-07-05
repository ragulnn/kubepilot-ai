from agents.adaptive_pipeline import AdaptivePipeline

pipeline = AdaptivePipeline()

state = {

    "question":"Why is nginx restarting?"

}

pipeline.run(

    state

)
