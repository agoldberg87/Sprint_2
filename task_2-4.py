class EmployeeSalary:
    hours = None
    hourly_payment = 400
    email = None
    rest_days = None
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        EmployeeSalary.hours = hours
        EmployeeSalary.rest_days = rest_days
        EmployeeSalary.email = email
    
    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    @classmethod
    def salary(cls):
        return cls.hours * cls.hourly_payment
