import random
from faker import Faker

from django.test import TestCase
from django.db.models import Count, Q
from django.db.models.functions import TruncMonth, TruncYear

from django.contrib.auth import get_user_model

from .models import Event

User = get_user_model()

fake = Faker()


def make_queryset_legible(query):
    print(str(query).replace("}, ", "},\n").replace("<QuerySet [", "<QuerySet [\n"))


class HistoryAPITestCase(TestCase):
    def setUp(self):
        user_quantity = 5
        users_details = []
        users = []

        event_quantity = 25
        events = []
        # Create Test Users
        for x in range(user_quantity):
            users_details.append(fake.simple_profile())
            users.append(User.objects.create(username=users_details[x]["username"], password=fake.password(length=12)))
        # Create Test Events
        for x in range(event_quantity):
            events.append(
                Event.objects.create(
                    user=users[random.randint(0, user_quantity - 1)],
                    success=fake.boolean(chance_of_getting_true=69),
                    created=fake.past_date(start_date="-120d", tzinfo=None),
                )
            )

    def test_query(self):
        print(User.objects.count())
        print(Event.objects.count())
        q = (
            Event.objects.annotate(month=TruncMonth("created"))
            .values("month", "user")
            .annotate(completed=Count("uuid", filter=Q(success=True)))
            .annotate(failed=Count("uuid", filter=Q(success=False)))
        )
        make_queryset_legible(q)
