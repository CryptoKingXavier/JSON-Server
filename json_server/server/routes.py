from json import load, dump
from flask import Blueprint, redirect, url_for, request


server: Blueprint = Blueprint("server", __name__)
json_path = "./json_server/json/jobs.json"
setup_path = "./json_server/json/setup.json"


# Utilities
def get_jobs(): return load(open(json_path))["jobs"]


def get_ids() -> list[str]: return [job["id"] for job in get_jobs()]


def new_id() -> str: return str(int(get_ids()[-1]) + 1)


# URL Configurations

# GET /jobs/proxy/job-type/: Retrieve New Job Type data.
@server.get("/jobs/proxy/job-type/")
def job_type():
    return load(open(setup_path))["setup"]["Job-Type"]


# GET /jobs/proxy/salary/: Retrieve New Job Salary data.
@server.get("/jobs/proxy/salary/")
def salary():
    return load(open(setup_path))["setup"]["Salary"]

# GET /jobs/: Retrieve all JSON data.
@server.get("/")
@server.get("/jobs/")
def read_jobs(): return get_jobs()


# GET /jobs/{id}/: Retrieve JSON data by ID.
@server.get("/jobs/<id>/")
def read_job(id):
    if id not in get_ids(): return "⚠️ Not Found! ⚠️"
    else:
        for job in get_jobs():
            if job["id"] == id: return job


# POST /jobs/: Add new JSON data.
@server.post("/jobs/")
def create_job():
    jobs = get_jobs()
    jobs.append(
        {
            "id": new_id(),
            "type": request.form.get("type"),
            "title": request.form.get("title"),
            "description": request.form.get("description"),
            "salary": request.form.get("salary"),
            "location": request.form.get("location"),
            "company": {
                "name": request.form.get("company_name"),
                "description": request.form.get("company_description"),
                "contactEmail": request.form.get("contact_email"),
                "contactPhone": request.form.get("contact_phone")
            }
        }
    )
    
    json_data = dict(jobs=jobs)
    
    with open(json_path, "w") as server_file:
        dump(json_data, server_file, indent=4, sort_keys=True)
    
    return get_jobs()


# PATCH /jobs/{id}/: Partially update existing JSON data.
# PUT /jobs/{id}/: Fully update existing JSON data.
@server.patch("/jobs/<id>/")
@server.put("/jobs/<id>/")
def update_job(id):
    if id not in get_ids(): return "⚠️ Not Found! ⚠️"
    else:
	jobs = get_jobs()
        for job in jobs:
            if job["id"] == id: job.update(request.form)
    
    json_data = dict(jobs=jobs)
    
    with open(json_path, "w") as server_file:
        dump(json_data, server_file, indent=4, sort_keys=True)
    
    return get_jobs()



# DELETE /jobs/{id}/: Delete JSON data by ID.
@server.delete("/jobs/<id>/")
def delete_job(id):
    if id not in get_ids(): return "⚠️ Not Found! ⚠️"
    else:
	jobs = get_jobs()
        for job in get_jobs():
            if job["id"] == id: jobs.remove(job)
    
    json_data = dict(jobs=jobs)
    
    with open(json_path, "w") as server_file:
        dump(json_data, server_file, indent=4, sort_keys=True)
    
    return get_jobs()
