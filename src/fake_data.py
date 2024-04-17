from faker import Faker


class FakeData:
    @property
    def first_name(self):
        return Faker().first_name()

    @property
    def last_name(self):
        return Faker().last_name()

    @property
    def postcode(self):
        return Faker().postcode()

