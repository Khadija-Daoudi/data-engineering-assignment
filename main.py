from scripts import read_file,transform_data, load_data

def main():
    input_file = 'employee_details.csv'
    raw_data = read_file(input_file)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)

if __name__ == "__main__":
    main()
