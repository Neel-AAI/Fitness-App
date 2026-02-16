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

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Thor', email='thor@marvel.com', team='Marvel'),
            User(name='Hulk', email='hulk@marvel.com', team='Marvel'),
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Flash', email='flash@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user='Iron Man', type='Running', duration=30, date='2026-02-15'),
            Activity(user='Superman', type='Cycling', duration=45, date='2026-02-15'),
            Activity(user='Batman', type='Swimming', duration=25, date='2026-02-15'),
            Activity(user='Wonder Woman', type='Yoga', duration=60, date='2026-02-15'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        workouts = [
            Workout(name='Morning Cardio', description='A quick cardio session.', difficulty='Easy'),
            Workout(name='Strength Training', description='Build muscle strength.', difficulty='Hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
