from django.core.management.base import BaseCommand
from shopapp.models import Customer



class Command(BaseCommand):
    help = "Get customer"

    def handle(self, *args, **kwargs):

        customer = Customer(name='Marina', email='marina@mail.ru', phone='81234567899',
                            address='S-Petersburg st.Zavodskaya 1 99')
        customer.save()
        self.stdout.write(f'{customer}')