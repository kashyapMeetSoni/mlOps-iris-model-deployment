## Hyperparameter Tuning Report

The hyperparameter tuning process was performed using `GridSearchCV` with 3-fold cross-validation. The following hyperparameters of the `RandomForestClassifier` were tuned:

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

**Results:**

- **Best Hyperparameters:**
    - `n_estimators`: 100
    - `max_depth`: 30
    - `min_samples_split`: 2
    - `min_samples_leaf`: 1
- **Best Cross-Validation Score (Accuracy):** 0.958
- **Observations:**
    - Increasing `n_estimators` generally improved performance, but the improvement plateaued after 100.
    - Deeper trees (`max_depth`) tended to perform better, with the best results at `max_depth` of 30 or None.
    - The default values for `min_samples_split` (2) and `min_samples_leaf` (1) worked well.
    
    
## Running the Model with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t iris-model-app .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 5001:5000 iris-model-app
    ```
3.  **Send a test request (using curl):**
    ```bash
    curl -X POST \
      http://localhost:5001/predict \
      -H 'Content-Type: application/json' \
      -d '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}'
    ```
 
