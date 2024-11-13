from Load_Dag import load_to_dynamodb

def main():
    # Run the ETL process: Extract -> Transform -> Load
    load_to_dynamodb()

if __name__ == "__main__":
    main()
