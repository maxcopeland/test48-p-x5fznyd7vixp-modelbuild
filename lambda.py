{
    "GET_PIPELINE_KWARGS": {
        "pipeline_name": "use-case-example-pipe",
        "model_package_group_name": "use-case-example-mpg",
        "processing_instance_type": "ml.m5.large",
        "training_instance_type": "ml.m5.large",
        "inference_instance_type": "ml.m5.large"
    },
    "RUN_PIPELINE_PARAMS": {
        "SkipDataQualityCheck": true, 
        "RegisterNewDataQualityBaseline": true, 
        "SkipDataBiasCheck": true, 
        "RegisterNewDataBiasBaseline": true, 
        "SkipModelQualityCheck": true,
        "RegisterNewModelQualityBaseline": true, 
        "SkipModelBiasCheck": true, 
        "RegisterNewModelBiasBaseline": true,
        "SkipModelExplainabilityCheck": true,
        "RegisterNewModelExplainabilityBaseline": true 
    }
}