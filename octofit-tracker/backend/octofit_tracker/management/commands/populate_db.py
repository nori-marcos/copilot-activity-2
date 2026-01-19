from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
        ]

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30)
        Activity.objects.create(user='Captain America', activity_type='Cycling', duration=45)
        Activity.objects.create(user='Batman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='Superman', activity_type='Flying', duration=120)

        # Leaderboard
        Leaderboard.objects.create(user='Iron Man', points=100)
        Leaderboard.objects.create(user='Captain America', points=90)
        Leaderboard.objects.create(user='Batman', points=110)
        Leaderboard.objects.create(user='Superman', points=120)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        Workout.objects.create(name='Power Lift', description='Strength training for super strength')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
