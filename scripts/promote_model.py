import os
import mlflow
from dotenv import load_dotenv


def promote_model():
    # Load environment variables (for local use)
    # In GitHub Actions, these are already set via workflow secrets.
    load_dotenv()

    repo_owner = os.getenv("DAGSHUB_USERNAME")
    repo_name = os.getenv("DAGSHUB_REPO")
    token = os.getenv("MLOPS_DAGSHUB_TOKEN")

    if not all([repo_owner, repo_name, token]):
        raise EnvironmentError("Missing DagsHub environment variables.")

    os.environ["MLFLOW_TRACKING_USERNAME"] = token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = token

    mlflow.set_tracking_uri(
        f"https://dagshub.com/{repo_owner}/{repo_name}.mlflow"
    )

    client = mlflow.MlflowClient()

    model_name = "my_model"

    # Fetch all registered model versions
    versions = client.search_model_versions(f"name='{model_name}'")

    if not versions:
        raise Exception(f"No registered versions found for model '{model_name}'")

    best_version = None
    best_auc = -1

    # Find the model version with the highest AUC
    for mv in versions:
        run = client.get_run(mv.run_id)

        auc = run.data.metrics.get("auc")

        if auc is None:
            print(f"Skipping version {mv.version}: AUC not found")
            continue

        print(f"Version {mv.version}: AUC = {auc}")

        if auc > best_auc:
            best_auc = auc
            best_version = mv.version

    if best_version is None:
        raise Exception("No model version contains an AUC metric.")

    # Assign the alias 'champion' to the best model
    client.set_registered_model_alias(
        name=model_name,
        alias="champion",
        version=best_version,
    )

    print(
        f"Model version {best_version} is now the CHAMPION "
        f"(AUC = {best_auc:.4f})"
    )


if __name__ == "__main__":
    promote_model()