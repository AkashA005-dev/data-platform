import os

RAW_DATA_DIR = "data/raw"

def list_raw_files():
    if not os.path.exists(RAW_DATA_DIR):
        print("Raw data directory does not exist")
        return []

    files = os.listdir(RAW_DATA_DIR)
    return files

if __name__ == "__main__":
    files = list_raw_files()
    print("Raw files found:", files)
