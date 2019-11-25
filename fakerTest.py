from faker import Faker

faker = Faker('hi_IN')

print(f'name: {faker.name()}')
print(f'address: {faker.address()}')
print(f'phone no{faker.phone_number()}')
print(f'text: {faker.text()}')