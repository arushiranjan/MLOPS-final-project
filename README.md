# 🚀 End-to-End MLOps Pipeline for IMDb Sentiment Analysis

An end-to-end MLOps pipeline that automates the complete machine learning lifecycle—from data ingestion to model registration—using AWS, DVC, MLflow, and DagsHub. The project follows production-ready MLOps practices with experiment tracking, data/model versioning, reproducible pipelines, and cloud storage.

> **Status:** 🚧 In Progress  
> Upcoming features: Docker, GitHub Actions CI/CD, Amazon EKS deployment, Prometheus & Grafana monitoring, and an Agentic AI MLOps Assistant.

---

## 📌 Features

- Automated data ingestion from AWS S3
- Text preprocessing and feature engineering
- Model training and evaluation
- MLflow experiment tracking
- Model Registry using MLflow
- Data & model versioning using DVC
- Cloud storage with Amazon S3
- Experiment visualization with DagsHub
- Reproducible ML pipelines

---

# 🏗️ Architecture

```text
                    +----------------+
                    |   Amazon S3    |
                    +-------+--------+
                            |
                            ▼
                 Data Ingestion Pipeline
                            |
                            ▼
                  Data Preprocessing
                            |
                            ▼
                 Feature Engineering
                            |
                            ▼
                    Model Training
                            |
                            ▼
                   Model Evaluation
                            |
                            ▼
              MLflow Experiment Tracking
                            |
                            ▼
                 MLflow Model Registry
                            |
                            ▼
                DVC Data & Model Versioning
                            |
                            ▼
                      DagsHub Remote
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Cloud | AWS S3 |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Remote Experiment Server | DagsHub |
| ML | Scikit-learn |
| Version Control | Git, GitHub |
| Environment | Python Virtual Environment |

### Upcoming

- Docker
- GitHub Actions
- Amazon ECR
- Amazon EKS
- Prometheus
- Grafana
- LangGraph Agent

---

# 📂 Project Structure

```text
.
├── artifacts/
├── config/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── models/
├── notebooks/
├── src/
│   ├── components/
│   ├── data/
│   ├── features/
│   ├── model/
│   ├── utils/
│   └── logger.py
├── dvc.yaml
├── dvc.lock
├── requirements.txt
└── README.md
```

---

# ⚙️ Pipeline Workflow

```text
AWS S3
   │
   ▼
Data Ingestion
   │
   ▼
Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Evaluation
   │
   ▼
MLflow Tracking
   │
   ▼
Model Registry
   │
   ▼
DVC Versioning
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure AWS

```bash
aws configure
```

Enter

- AWS Access Key
- AWS Secret Key
- Region
- Output Format

---

## Configure Environment Variables

Create a `.env` file

```env
S3_BUCKET_NAME=your-bucket-name

DAGSHUB_USERNAME=your_username
DAGSHUB_REPO=your_repo
DAGSHUB_TOKEN=your_token
```

---

# ▶️ Run Pipeline

Run individual stages

```bash
python src/data/data_ingestion.py
```

```bash
python src/data/data_preprocessing.py
```

```bash
python src/features/feature_engineering.py
```

```bash
python src/model/train_model.py
```

```bash
python src/model/model_evaluation.py
```

```bash
python src/model/register_model.py
```

Or execute the complete pipeline

```bash
dvc repro
```

---

# 📈 Experiment Tracking

Experiments are logged using **MLflow** and synchronized with **DagsHub**.

Tracked information includes

- Parameters
- Metrics
- Models
- Artifacts

---

# 📦 Data Versioning

DVC is used for

- Dataset versioning
- Model versioning
- Pipeline reproducibility
- Remote storage on AWS S3

Useful commands

```bash
dvc repro
```

```bash
dvc status
```

```bash
dvc push
```

```bash
dvc pull
```

---

# 📊 Results

| Metric | Value |
|---------|------|
| Model | TBD |
| Accuracy | TBD |
| Precision | TBD |
| Recall | TBD |
| F1 Score | TBD |

---

# 🔜 Roadmap

- [x] AWS S3 Data Ingestion
- [x] Data Preprocessing
- [x] Feature Engineering
- [x] Model Training
- [x] Model Evaluation
- [x] MLflow Tracking
- [x] DVC Pipeline
- [x] DagsHub Integration
- [ ] Docker
- [ ] GitHub Actions CI/CD
- [ ] Amazon ECR
- [ ] Amazon EKS
- [ ] Prometheus Monitoring
- [ ] Grafana Dashboard
- [ ] Agentic AI MLOps Assistant

---

# 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.