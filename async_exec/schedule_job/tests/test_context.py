from async_exec.schedule_job.context import ScheduleJob
from async_exec.tests.function_for_test import sample_function
from async_exec.models import Job
from datetime import datetime
from django.test import TestCase

class WithJobModel(TestCase):
    def setUp(self):
        self.job = Job()

class WithJobStub(TestCase):
    def setUp(self):
        self.job = Stub()

class TestSchedule(object):
    def test_job_is_persisted(self):
        with ScheduleJob(None, self.job, sample_function) as context:
            self.assertTrue(hasattr(context.job 'id'))
        
    def test_successfully_schedule_job_with_no_scheduled_time(self):
        with ScheduleJob(None, self.job, sample_function) as context:
            self.assertEqual(None, context.job.scheduled)

    def test_successfully_schedule_job_with_scheduled_time(self):
        scheduled_time = datetime.now()
        with ScheduleJob(scheduled_time, self.job, sample_function) as context:
            self.assertEqual(scheduled_time, context.job.scheduled)
        
    def test_successfully_schedule_job_with_kwargs(self):
        with ScheduleJob(None, self.job, sample_function, name = 'John') as context:
            self.assertEqual('{"name": "John"}', context.job.kwargs)
        
class TestWithStub(TestScheduleJob, WithStub):
    pass
class TestWithModel(TestScheduleJob, WithModel):
    pass

