import csv
from src.validation.schema import USER_SCHEMA

RAW_FILE = "data/raw/users.csv"

def validate_row(row,line_number):
    errors = []

    for column , expected_type in USER_SCHEMA.items():
        value = row.get(column)

        if value is None or value == "":
            errors.append(f"{column} is missing")
            continue

        try:
            expected_type(value)
        except ValueError:
            errors.append(f"{column} has invalid type : {value}")
    
    return errors 

def validate_file():
    with open(RAW_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for i , row in enumerate(reader , start=2):
            errors = validate_row(row,i)

            if errors:
                print(f"Line {i} errors: ",errors)
            else:
                print(f"Line {i} valid")

if __name__ == "__main__":
    validate_file()



# python -m src.validation.validate_users