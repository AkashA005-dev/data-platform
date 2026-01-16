import csv
from src.validation.schema import USER_SCHEMA

RAW_FILE = "data/raw/users.csv"
VALID_OUTPUT = "data/processed/valid_users.csv"
INVALID_OUTPUT = "data/processed/invalid_users.csv"


def validate_row(row):
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

def process_file():
    valid_rows = []
    invalid_rows = []

    with open(RAW_FILE,newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            errors = validate_row(row)

            if errors:
                row["errors"] = "; ".join(errors)
                invalid_rows.append(row)
            else:
                valid_rows.append(row)
    return valid_rows , invalid_rows


def write_csv(path,rows,Fieldnames):
    with open(path,"w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=Fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    valid_rows , invalid_rows = process_file()

    if valid_rows:
        write_csv(VALID_OUTPUT,valid_rows,Fieldnames=valid_rows[0].keys())
    
    if invalid_rows:
        write_csv(INVALID_OUTPUT,invalid_rows,Fieldnames=invalid_rows[0].keys())
    
    print(f"Valid rows written: {len(valid_rows)}")
    print(f"Invalid rows written: {len(invalid_rows)}")



# python -m src.validation.validate_users