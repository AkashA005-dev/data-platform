# Batch Analytics Data Platform

## Overview
Build a simple batch analytics pipeline that ingests raw CSV, validates schema, attempts cleaning of invalid records, and separates cleaned vs rejected data for analytics readiness.

## Goals
- Practice real-world data engineering concepts
- Build a portfolio-grade project
- Demonstrate SQL, Python, and system design skills

## Architecture (Initial)
Raw CSV (data/invalid) → Validation Layer → Valid vs Invalid
Invalid → Cleaning → Cleaned + Rejected with error metadata

## How to run
# from project root
python -m src.pipeline

## What you will see
data/cleaned/cleaned_invalid_data.csv
data/rejected/rejected_data.csv

## Tech Stack
- Python
- SQL
- Git
