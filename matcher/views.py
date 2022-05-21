from ctypes import c_bool
from tkinter.messagebox import NO
from typing import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
from .models import Skill, Candidate, Job
from pprint import pprint
from boltons.setutils import IndexedSet


def search_job(request):
    query_dict = request.GET
    query = query_dict.get("query")
    candidates, job_skills, job_obj, job_obj_to_print = None, None, None, None
    if query:
        try:
            job_obj = Job.objects.all().filter(job_title=query)
            job_obj_to_print = [(job.job_title, [s.skill_name for s in job.job_skills.all()])
                                for job in job_obj]
        except:
            job_obj = None
    if job_obj:
        try:
            candidates = sorted_candidates_for_all_jobs(job_obj, query)
        except:
            candidates = None

    context = {"job_search": query,
               "job_objects": job_obj_to_print, "job_skills": job_skills, "candidates": candidates}
    return render(request, 'search_many_jobs.html', context=context)


def sorted_candidates_for_all_jobs(job_obj, query):
    candidates_obj = Candidate.objects.all().filter(candidate_title=query)
    all_sorted = []
    for job in job_obj:
        sorted_candidates = sorted(candidates_obj, key=lambda candidate: len(
            candidate.candidate_skills.all() & job.job_skills.all()), reverse=True)
        candidates = [(c.candidate_name, [s.skill_name for s in c.candidate_skills.all()])
                      for c in sorted_candidates]
        if candidates:
            all_sorted.append(candidates)

    return all_sorted if all_sorted else None


def search_partial(request):
    candidates, job_skills, job_objects, query_words, job_found = None, None, None, None, None
    query_dict = request.GET
    query = query_dict.get("query")
    if query:
        candidates, job_found = find_partial_job_match(query)
    context = {"job_search": query, "job_found": job_found,
               "candidates": candidates}
    return render(request, 'search_job.html', context=context)


def find_partial_job_match(query):
    all_jobs = Job.objects.all()
    all_candidates = Candidate.objects.all()
    candidates = IndexedSet()
    search_for = query
    query_words = query.split()
    job_found_flag = False
    for i in range(len(query_words)):
        try:
            matching_jobs = all_jobs.filter(job_title__icontains=search_for)
            if matching_jobs:
                job_found_flag = True
        except:
            continue

        cur_candidates = all_candidates.filter(
            candidate_title__startswith=search_for)
        for can in cur_candidates:
            candidates.add(can)

        search_for = search_for.rsplit(' ', 1)[0]

    ret_candidate = None
    if candidates:
        list_candidates = list(candidates)
        ret_candidate = [(c.candidate_title, c.candidate_name, [s.skill_name for s in c.candidate_skills.all()])
                         for c in list_candidates]
    return ret_candidate, job_found_flag
