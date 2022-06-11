import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "min_salary": "1000",
            "max_salary": "2000",
            "date_posted": "2020-05-07",
        },
        {
            "min_salary": "500",
            "max_salary": "1000",
            "date_posted": "2020-05-06",
        },
        {
            "min_salary": "2000",
            "max_salary": "3000",
            "date_posted": "2020-05-08",
        },
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "500"

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "3000"

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-05-08"

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
