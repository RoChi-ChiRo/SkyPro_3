from utils import get_last_operations, format_operation


def main():
    last_operations = get_last_operations(5)

    for operation in last_operations:
        print(format_operation(operation), end='\n\n')


if __name__ == '__main__':
    main()
