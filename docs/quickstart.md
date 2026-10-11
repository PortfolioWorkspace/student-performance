# Quickstart Guide

Follow the steps below to get up and running in minutes.

## System Requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/)

## 1. Clone the Repository

```bash
git clone https://github.com/maybe-Inhuman/student-performance.git
cd student-performance
```

## 2. Install the Dependencies

```bash
uv sync
.venv\Scripts\Activate.ps1 # Windows
source .venv/bin/activate  # Linux / macOS
```

## 3. Prepare the Dataset

1. Download the [Student Performance Dataset](https://www.kaggle.com/datasets/nabeelqureshitiii/student-performance-dataset) from Kaggle.
2. Exract the `student_performance.csv` file.
3. Move the downloaded file to `data/raw` directory.

> [!NOTE]
> See the [Dataset](../data/README.md) for licensing and author information.

## 4. Start the Application

```bash
python -m main
```

That's it! The project now should be running.
