from utils import load_data, filter_sort_spisok, formatted_data


def main():
    data = load_data()
    data = filter_sort_spisok(data)

    for i in range(5):
        print(formatted_data(data[i]))


if __name__ == '__main__':
    main()
