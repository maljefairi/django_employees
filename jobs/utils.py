# jobs/utils.py 
from fuzzywuzzy import fuzz
from django.db.models import Q


def search_with_aprox(keyword, queryset):
    results = []
    # Exact match
    exact_match_results = search_without_aprox(keyword, queryset)
    for ind in exact_match_results:
        results.append(ind)

    # Fuzzy match
    fuzzy_results = []
    for ind in queryset:
        match_ratio = fuzz.token_sort_ratio(keyword, ind.name)
        if match_ratio > 70:
            fuzzy_results.append(ind)

    # Combine and return results as a QuerySet
    results.extend(fuzzy_results)
    return queryset.filter(pk__in=[ind.pk for ind in results])

def search_without_aprox(keyword, queryset):
    filter_data = queryset.filter(
        Q(job_title__contains=keyword)
        | Q(department__contains=keyword)
        | Q(administration__contains=keyword)
        | Q(qualification__contains=keyword)
        | Q(major__contains=keyword)
        | Q(degree__contains=keyword)
        | Q(job_description__contains=keyword)
        | Q(job_duties__contains=keyword)
        | Q(job_objectives__contains=keyword)
        | Q(suggested_training__contains=keyword)
    )
    return filter_data
