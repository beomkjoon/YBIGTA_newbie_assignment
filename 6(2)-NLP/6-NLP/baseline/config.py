"""
KorNLI Configuration - 설정값 관리
"""

import torch

# Label Mapping
LABEL2ID = {"entailment": 0, "neutral": 1, "contradiction": 2}
ID2LABEL = {v: k for k, v in LABEL2ID.items()}
NUM_LABELS = len(LABEL2ID)

# Device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Paths
DEFAULT_DATA_DIR = "../data"
DEFAULT_OUTPUT_DIR = "../submission"
DEFAULT_CHECKPOINT_DIR = "./checkpoints"

# Configuration Presets
CONFIGS = {
    # 실제 제출용 - klue/bert-base 풀 파인튜닝. Colab T4 기준 epoch당 ~10분대.
    "default": {
        "model_name": "klue/bert-base",
        "max_length": 64,
        "batch_size": 32,
        "learning_rate": 2e-5,
        "epochs": 4,
        "warmup_ratio": 0.1,
        "weight_decay": 0.01,
        "classifier_dropout": 0.1,
        "early_stopping_patience": 2,
        "preprocess": True,
        "train_file": "train.tsv",
        "dev_file": "val.tsv",
        "test_file": "test_unlabeled.tsv",
    },
    # 파이프라인/코드 변경 확인용 빠른 preset (작은 모델 + 1 epoch)
    "fast": {
        "model_name": "monologg/distilkobert",
        "max_length": 64,
        "batch_size": 64,
        "learning_rate": 5e-5,
        "epochs": 1,
        "warmup_ratio": 0.1,
        "weight_decay": 0.01,
        "classifier_dropout": 0.1,
        "early_stopping_patience": None,
        "preprocess": True,
        "train_file": "train.tsv",
        "dev_file": "val.tsv",
        "test_file": "test_unlabeled.tsv",
    },
}


def get_config(preset: str = "default", **overrides) -> dict:
    """설정 프리셋 로드 + override 적용"""
    if preset not in CONFIGS:
        raise ValueError(f"Unknown preset: {preset}. Available: {list(CONFIGS.keys())}")
    config = CONFIGS[preset].copy()
    config.update(overrides)
    return config