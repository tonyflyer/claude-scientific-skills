"""
Templates module for arxiv-database skill.

Provides pre-built workflow templates for common research tasks.
"""

from .literature_review import main as literature_review
from .deep_analysis import main as deep_analysis
from .reproduction import main as reproduction
from .survey import main as survey

__all__ = ["literature_review", "deep_analysis", "reproduction", "survey"]
