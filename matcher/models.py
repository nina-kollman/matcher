from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name

    class Meta:
        db_table = "skill"


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=100)
    candidate_title = models.CharField(max_length=100)
    candidate_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.candidate_name

    class Meta:
        db_table = "candidate"


class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.job_title

    class Meta:
        db_table = "job"
