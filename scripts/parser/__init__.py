"""
Code Security Research — 学术文献版面解析模块 (Parser Package)
"""
from .lightweight_parser import convert_pdf_to_clean_markdown
from .evaluator import analyze_markdown_quality

__all__ = ["convert_pdf_to_clean_markdown", "analyze_markdown_quality"]
