from async_exec.schedule_job.role import Task 

class Context(object):
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):
        self.__enter__()
        self.__exit__()

    def __enter__(self):
        self.setup(*self.__args, **self.__kwargs)
        self.pre_conditions()
        self.use_case()
        self.post_conditions()
        return self

    def __exit__(self, *_):
        for o in self.__dict__:
            if type(type(o)) == ModelRoleType:
                revoke_roles(o)


def django_view(request):
    with ScheduleJob(time, job, 'foo', ['bar', 3]) as context:
        # By here the use case is executed, so we can now pull data off the objects to present to user
        id = context.job.id 


class ScheduleJob(Context):
    def setup(self, time_to_execute, job, function, args, kwargs):
        self.job = Task(job)
        self.time_to_execute = time_to_execute
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def pre_conditions(self):
        assert not self.job.executed()

    def use_case(self):
        self.job.set_call(self.function, *self.args, **self.kwargs)
        if self.time_to_execute:
            self.job.schedule(self.time_to_execute)
        self.job.save() 

class ScheduleJob(object):
    def __init__(self, time_to_execute, job, function, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.time_to_execute = time_to_execute
        # assign roles
        self.job = Task(job)

    def __enter__(self):
        # pre conditions here
        self.job.set_call(self.function, *self.args, **self.kwargs)
        if self.time_to_execute:
            self.job.schedule(self.time_to_execute)
        self.job.save() 
        return self

    def __exit__(self, type, value, traceback):
        Task.revoke(self.job)

