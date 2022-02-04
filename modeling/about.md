# Work in Progress: Models directory

All files for data preprocessing, embedding, model generation, training and prediction‚ are located in this folder.

## Architecture

* /configs
    * Here we can store all configurations in a yml-file
    * For example:
        * Training settings, like batch_size, seed, epochs, loss, metric, regularizer
        * Model
        * Embedding settings
        * Dataset settings, like training directions, test directions, train_val_split
        * Logging settings, like verbose, with or without plots, etc.
* /models
   * directory with logical files for models. which we can import in trian.py to train the models on differently preprocessed data and in predict.py to make predictions.
   * For example:
      * Transformers
      * RNN
      * etc.
* train.py
    * import mlflow
    * import config
    * import data
    * import vectorizer/embedder
    * import models
    * save models and results with mlflow
* predict.py
    * load trained models
    * load testdata
    * preprocess testdata
    * predict X_test with saved model
    * evaluate
    * save X_test predictions to submission file
    * Save results with mlflow tracking
* text_processing.py
