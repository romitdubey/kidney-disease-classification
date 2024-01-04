from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"**************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = PrepareBaseModelTrainingPipline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"**************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model_Evaluation"
try:
    logger.info(f"**************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e