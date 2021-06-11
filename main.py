from application import db, salary


def main():
    salary.calculate_salary()
    db.people.get_employees()


if __name__ == '__main__':
    main()
