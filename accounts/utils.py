from faker import Faker
from .models import Customer

fake = Faker()

def generate_customer(num):
    for i in range(num):
        customer = Customer.objects.create(
            name = fake.user_name(),
            phone = fake.phone_number(),
            email = fake.email()
        )
        customer.save()
