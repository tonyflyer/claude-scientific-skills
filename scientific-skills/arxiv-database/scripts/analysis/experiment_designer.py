"""
Experiment design assistant for generating experimental plans based on paper methodology.

Analyzes paper methods and generates detailed experimental protocols.
"""

import json
import re
from typing import Any


class ExperimentDesigner:
    """Generate experimental design from paper methodology."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def design_experiment(
        self,
        paper_data: dict,
        methodology_text: str = "",
        target_metric: str = "",
    ) -> dict:
        """
        Generate a comprehensive experimental design.

        Args:
            paper_data: Paper metadata
            methodology_text: Extracted methodology section text
            target_metric: Specific metric to optimize for

        Returns:
            Complete experimental design
        """
        design = {
            "paper_id": paper_data.get("id", ""),
            "title": paper_data.get("title", ""),
            "generated_at": self._get_timestamp(),
            "research_objective": self._define_objective(paper_data, methodology_text),
            "experimental_variables": self._identify_variables(methodology_text),
            "datasets": self._identify_datasets(methodology_text),
            "baselines": self._identify_baselines(methodology_text),
            "metrics": self._identify_metrics(methodology_text, target_metric),
            "experimental_protocol": self._create_protocol(methodology_text),
            "hyperparameters": self._extract_hyperparameters(methodology_text),
            "implementation_guide": self._create_implementation_guide(methodology_text),
            "evaluation_plan": self._create_evaluation_plan(methodology_text),
            "expected_outputs": self._define_expected_outputs(),
        }

        return design

    def _define_objective(self, paper_data: dict, methodology: str) -> dict:
        """Define the research objective based on paper."""
        title = paper_data.get("title", "").lower()
        abstract = paper_data.get("abstract", "").lower()

        # Detect task type
        task_types = {
            "classification": ["classification", "classifier", "classify"],
            "generation": ["generation", "generate", "gpt", "llm"],
            "detection": ["detection", "detect", "yolo", "faster r-cnn"],
            "segmentation": ["segmentation", "segment", "mask"],
            "prediction": ["prediction", "predict", "forecast"],
            "optimization": ["optimization", "optimize", "optimal"],
            "reinforcement": ["reinforcement", "rl", "policy", "agent"],
        }

        detected_task = "general"
        for task, keywords in task_types.items():
            if any(kw in abstract for kw in keywords):
                detected_task = task
                break

        return {
            "task_type": detected_task,
            "primary_goal": "Reproduce and validate the methodology from the paper",
            "success_criteria": [
                "Achieve comparable performance on reported metrics",
                "Validate key findings through ablation studies",
                "Confirm reproducibility of main results",
            ],
        }

    def _identify_variables(self, methodology: str) -> dict:
        """Identify independent and dependent variables."""
        methodology_lower = methodology.lower()

        variables = {
            "independent": [],
            "dependent": [],
            "controlled": [],
        }

        # Common independent variables in ML papers
        if any(kw in methodology_lower for kw in ["learning rate", "lr"]):
            variables["independent"].append({
                "name": "learning_rate",
                "description": "Step size for gradient descent",
                "typical_range": "[0.0001, 0.1]",
            })

        if any(kw in methodology_lower for kw in ["batch size", "batch_size"]):
            variables["independent"].append({
                "name": "batch_size",
                "description": "Number of samples per gradient update",
                "typical_range": "[16, 512]",
            })

        if any(kw in methodology_lower for kw in ["epoch", "training step"]):
            variables["independent"].append({
                "name": "epochs",
                "description": "Number of complete passes through the dataset",
                "typical_range": "[10, 1000]",
            })

        # Dependent variables (metrics)
        if any(kw in methodology_lower for kw in ["accuracy", "acc"]):
            variables["dependent"].append({"name": "accuracy", "description": "Classification accuracy"})

        if any(kw in methodology_lower for kw in ["loss"]):
            variables["dependent"].append({"name": "loss", "description": "Training/validation loss"})

        if any(kw in methodology_lower for kw in ["f1", "f1-score"]):
            variables["dependent"].append({"name": "f1_score", "description": "F1 Score"})

        # Controlled variables
        variables["controlled"] = [
            {"name": "random_seed", "value": "42 (for reproducibility)"},
            {"name": "hardware", "value": "GPU type and count"},
            {"name": "preprocessing", "value": "Consistent data preprocessing pipeline"},
        ]

        return variables

    def _identify_datasets(self, methodology: str) -> list[dict]:
        """Identify datasets used in the paper."""
        datasets = []

        # Common dataset names
        dataset_patterns = {
            "ImageNet": ["imagenet"],
            "COCO": ["coco", "ms-coco"],
            "MNIST": ["mnist"],
            "CIFAR-10": ["cifar-10", "cifar10"],
            "CIFAR-100": ["cifar-100", "cifar100"],
            "GLUE": ["glue benchmark"],
            "SQuAD": ["squad"],
            "PubMed": ["pubmed"],
            "BookCorpus": ["bookcorpus", "books corpus"],
        }

        methodology_lower = methodology.lower()
        for dataset_name, patterns in dataset_patterns.items():
            for pattern in patterns:
                if pattern in methodology_lower:
                    datasets.append({
                        "name": dataset_name,
                        "source": f"Standard benchmark ({dataset_name})",
                        "size": "See original dataset documentation",
                        "split": "train/val/test as specified in paper",
                    })
                    break

        # If no specific datasets found
        if not datasets:
            datasets.append({
                "name": "To be identified",
                "source": "Extract from paper methodology section",
                "note": "Review paper for specific dataset names and sources",
            })

        return datasets

    def _identify_baselines(self, methodology: str) -> list[dict]:
        """Identify baseline methods for comparison."""
        baselines = []

        # Common baseline patterns
        baseline_keywords = [
            "resnet", "bert", "gpt", "vit", "yolo", "gan",
            "random forest", "svm", "logistic regression",
            "vanilla", "standard", "baseline",
        ]

        methodology_lower = methodology.lower()
        for keyword in baseline_keywords:
            if keyword in methodology_lower:
                baselines.append({
                    "name": keyword.title(),
                    "description": f"Method mentioned in paper: {keyword}",
                    "source": "Standard implementation or paper citation",
                })

        # Add generic baseline if none found
        if not baselines:
            baselines = [
                {"name": "Random Baseline", "description": "Random prediction or initialization"},
                {"name": "Naive Method", "description": "Simplest possible approach for the task"},
            ]

        return baselines

    def _identify_metrics(self, methodology: str, target_metric: str = "") -> list[dict]:
        """Identify evaluation metrics."""
        metrics = []

        metric_patterns = {
            "Accuracy": [r"\bacc(?:uracy)?\b", r"\bcorrect\b"],
            "F1 Score": [r"\bf1(?:\s*score)?\b", r"\bf1\b"],
            "mAP": [r"\bmAP\b", r"\bmean\s*average\s*precision\b"],
            "IoU": [r"\biou\b", r"\bintersection\s*over\s*union\b"],
            "BLEU": [r"\bbleu\b"],
            "ROUGE": [r"\brouge\b"],
            "Perplexity": [r"\bperplexity\b"],
            "Loss": [r"\bloss\b"],
            "AUC-ROC": [r"\bauc\b", r"\broc\b"],
        }

        methodology_lower = methodology.lower()
        for metric_name, patterns in metric_patterns.items():
            for pattern in patterns:
                if re.search(pattern, methodology_lower):
                    metrics.append({
                        "name": metric_name,
                        "description": f"Primary metric: {metric_name}",
                        "higher_is_better": metric_name not in ["Loss"],
                    })
                    break

        # Add target metric if specified
        if target_metric and target_metric not in [m["name"] for m in metrics]:
            metrics.append({
                "name": target_metric,
                "description": "User-specified target metric",
                "higher_is_better": True,
            })

        return metrics

    def _create_protocol(self, methodology: str) -> dict:
        """Create detailed experimental protocol."""
        return {
            "phase1_data_preparation": {
                "steps": [
                    "Download and verify dataset integrity",
                    "Implement data preprocessing pipeline",
                    "Create data loaders with appropriate batch size",
                    "Apply data augmentation as specified in paper",
                    "Split data into train/val/test sets",
                ],
                "estimated_time": "30-60 minutes",
            },
            "phase2_model_implementation": {
                "steps": [
                    "Implement model architecture from paper",
                    "Initialize weights according to paper specifications",
                    "Set up optimizer with specified settings",
                    "Configure learning rate scheduler if applicable",
                ],
                "estimated_time": "1-4 hours",
            },
            "phase3_training": {
                "steps": [
                    "Train model for specified number of epochs",
                    "Monitor training and validation metrics",
                    "Implement early stopping if applicable",
                    "Save checkpoints at appropriate intervals",
                ],
                "estimated_time": "Depends on model size and dataset",
            },
            "phase4_evaluation": {
                "steps": [
                    "Evaluate on test set",
                    "Run comparison with baseline methods",
                    "Perform statistical significance tests",
                    "Generate visualizations of results",
                ],
                "estimated_time": "1-2 hours",
            },
        }

    def _extract_hyperparameters(self, methodology: str) -> dict:
        """Extract hyperparameters mentioned in methodology."""
        hyperparameters = {}

        # Learning rate
        lr_match = re.search(r"learning rate[:\s]+([\d.e\-]+)", methodology, re.IGNORECASE)
        if lr_match:
            hyperparameters["learning_rate"] = lr_match.group(1)

        # Batch size
        batch_match = re.search(r"batch(?:size)?[:\s]+(\d+)", methodology, re.IGNORECASE)
        if batch_match:
            hyperparameters["batch_size"] = batch_match.group(1)

        # Epochs
        epoch_match = re.search(r"epoch[s]?[:\s]+(\d+)", methodology, re.IGNORECASE)
        if epoch_match:
            hyperparameters["epochs"] = epoch_match.group(1)

        # Weight decay
        decay_match = re.search(r"weight decay[:\s]+([\d.e\-]+)", methodology, re.IGNORECASE)
        if decay_match:
            hyperparameters["weight_decay"] = decay_match.group(1)

        # Dropout
        dropout_match = re.search(r"dropout[:\s]+([\d.]+)", methodology, re.IGNORECASE)
        if dropout_match:
            hyperparameters["dropout"] = dropout_match.group(1)

        if not hyperparameters:
            hyperparameters = {
                "note": "Extract specific values from methodology section",
                "common_params": ["learning_rate", "batch_size", "epochs", "weight_decay", "dropout"],
            }

        return hyperparameters

    def _create_implementation_guide(self, methodology: str) -> dict:
        """Create implementation guidance."""
        return {
            "recommended_structure": {
                "data/": "Dataset and preprocessing scripts",
                "models/": "Model architecture definitions",
                "training/": "Training loop and utilities",
                "evaluation/": "Metrics and evaluation scripts",
                "configs/": "Configuration files",
            },
            "dependencies": [
                "torch >= 2.0 / tensorflow >= 2.0",
                "numpy >= 1.20",
                "pandas >= 1.5",
                "scikit-learn >= 1.0",
                "Additional task-specific packages",
            ],
            "coding_tips": [
                "Start with data pipeline before model",
                "Verify each component independently",
                "Log all hyperparameters for reproducibility",
                "Use tensorboard or wandb for experiment tracking",
            ],
        }

    def _create_evaluation_plan(self, methodology: str) -> list[dict]:
        """Create evaluation plan."""
        plan = [
            {
                "item": "Primary Metric Comparison",
                "description": "Compare reproduction results with paper's reported metrics",
                "success_threshold": "Within 2-5% of paper's reported performance",
            },
            {
                "item": "Ablation Study",
                "description": "Systematically remove/modify components to understand their contributions",
                "scope": "Key architectural choices and hyperparameters",
            },
            {
                "item": "Qualitative Analysis",
                "description": "Visual inspection of outputs (for generative tasks)",
                "scope": "Sample outputs and failure cases",
            },
            {
                "item": "Runtime Analysis",
                "description": "Measure training time and inference speed",
                "metrics": ["Training time per epoch", "Inference latency", "Memory usage"],
            },
        ]
        return plan

    def _define_expected_outputs(self) -> list:
        """Define expected outputs of the experiment."""
        return [
            "Trained model checkpoint(s)",
            "Training/validation curves",
            "Test set evaluation results",
            "Comparison with baseline methods",
            "Ablation study results (if applicable)",
            "Reproducibility report documenting all settings",
        ]

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()

    def generate_experiment_code(self, design: dict) -> str:
        """Generate starter code for the experiment."""
        code = []
        code.append("#!/usr/bin/env python3")
        code.append("# Experiment: " + design.get("title", "Untitled")[:50])
        code.append("# Generated by arxiv-database ExperimentDesigner")
        code.append("")
        code.append("import torch")
        code.append("import torch.nn as nn")
        code.append("from torch.utils.data import DataLoader")
        code.append("import numpy as np")
        code.append("import random")
        code.append("")
        code.append("# Set random seed for reproducibility")
        code.append("SEED = 42")
        code.append("random.seed(SEED)")
        code.append("np.random.seed(SEED)")
        code.append("torch.manual_seed(SEED)")
        code.append("if torch.cuda.is_available():")
        code.append("    torch.cuda.manual_seed_all(SEED)")
        code.append("")
        code.append("# Configuration")
        config = design.get("hyperparameters", {})
        code.append("config = {")
        for key, value in config.items():
            if isinstance(value, str) and value[0].isdigit():
                code.append(f"    '{key}': {value},")
            else:
                code.append(f"    '{key}': '{value}',")
        code.append("}")
        code.append("")
        code.append("# TODO: Implement dataset loading")
        code.append("# TODO: Implement model architecture")
        code.append("# TODO: Implement training loop")
        code.append("# TODO: Implement evaluation")
        code.append("")
        code.append("if __name__ == '__main__':")
        code.append("    print('Experiment configuration:', config)")
        code.append("")

        return "\n".join(code)
