#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name = 'Person', job = "job"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == type('string') and 0 < len(name) < 26:
            self._name = name.title()
            return self._name
        else:
            print("Name must be string between 1 and 25 characters.")
            
    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, job):
        cased_jobs = [job.lower() for job in APPROVED_JOBS]
        if job.lower() in cased_jobs:
            self._job = job
            return self._job
        else:
            print("Job must be in list of approved jobs.")
        
    job = property(get_job, set_job)
