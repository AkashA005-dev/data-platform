from src.cleaning.cleaner import clean_invalid_data

if __name__ == "__main__":
    clean_invalid_data(
        input_path="data/invalid/invalid_data.csv",
        cleaned_path="data/cleaned/cleaned_invalid_data.csv",
        rejected_path="data/rejected/rejected_data.csv"
    )