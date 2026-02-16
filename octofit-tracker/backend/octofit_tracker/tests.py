from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@user.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@user.com')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', members=['A', 'B'])
        self.assertEqual(team.name, 'Test Team')
        self.assertEqual(team.members, ['A', 'B'])

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', type='Running', duration=30, date='2026-02-16')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(lb.team, 'Test Team')
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc', difficulty='Easy')
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.difficulty, 'Easy')
