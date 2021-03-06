from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_list = read(path)

    job_types = []

    for job in job_list:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_list = [job for job in jobs if job["job_type"] == job_type]

    return filtered_list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    job_list = read(path)

    job_industries = []

    for job in job_list:
        if job["industry"] and job["industry"] not in job_industries:
            job_industries.append(job["industry"])

    return job_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_list = [job for job in jobs if job["industry"] == industry]

    return filtered_list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    job_list = read(path)

    salaries = []

    for job in job_list:
        try:
            salary = int(job["max_salary"])
            salaries.append(salary)
        except (ValueError):
            pass

    return max(salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    job_list = read(path)

    salaries = []

    for job in job_list:
        try:
            salary = int(job["min_salary"])
            salaries.append(salary)
        except (ValueError):
            pass

    return min(salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        if not type(min_salary) == type(max_salary) == int:
            raise ValueError("O valores precisam ser inteiros v??lidos!")
        elif min_salary > max_salary:
            raise ValueError("O valor m??nimo n??o pode ser maior que o m??ximo.")

    except KeyError:
        raise ValueError("As chaves min_salary e max_salary s??o obrigat??rias.")
    else:
        output = min_salary <= salary <= max_salary
        return output


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    filtered_jobs = []

    for job in jobs:
        try:
            if type(salary) == int and matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass

    return filtered_jobs
