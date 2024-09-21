import csv
import re
import os


def is_valid_email(email):
    try:
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if email is not None:
            return re.match(email_regex, email)
    except Exception as e:
        print(f"Error in email validation: {str(e)}")


def clean_csv(input_file, output_file):
    cleaned_data = []
    seen_user_ids = set()

    if not os.path.exists(input_file):
        print("file doesnot exits.")
        return

    try:
        # reading csv file
        with open(input_file, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                user_id = row["user_id"]
                email = row["email"]

                if user_id not in seen_user_ids and is_valid_email(email):
                    cleaned_data.append(row)
                    seen_user_ids.add(user_id)
    except Exception as e:
        print(f"Error while reading file: {str(e)}")

    try:
        # writing cleaned data to file
        with open(output_file, mode="w", newline="") as csvfile:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(cleaned_data)
    except Exception as e:
        print(f"Error while writing file: {str(e)}")


input_file = "data/user.csv"
output_file = "data/cleaned_user.csv"
clean_csv(input_file, output_file)
