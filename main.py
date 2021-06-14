from datetime import datetime
from application import db, salary


def main():
    print(datetime.utcnow())
    salary.calculate_salary()
    db.people.get_employees()


if __name__ == '__main__':
    main()
