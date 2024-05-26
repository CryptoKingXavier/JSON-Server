# RESTful API Testing with cURL

### *Use cURL to Test Retrieval RESTful APIs*
**`curl -X GET <url_path>`**

### *See Details of Request and Response*
**`curl -i <url_path> - includes status code and headers`**  
**`curl -v <url_path> - includes details of request and response`**

### *Use cURL to Test Create RESTful APIs*
**`curl -H "Content-Type: application/json" -d "{\"key\": \"value\"}" <url_path>`**

### *Use cURL to Test Full Update REST APIs*
**`curl -X PUT -H "Content-Type: application/json" -d "{\"key\": \"value\"}" <url_path>`**

### *Use cURL to Test Partial Update REST APIs*
**`curl -X PATCH -H "Content-Type: application/json" -d "{\"key\": \"value\"}" <url_path>`**

### *Use cURL to Test Delete REST APIs*
**`curl -v -X DELETE <url_path>`**

---
# CRUD Configurations

### CREATE FUNCTIONALITY
- **`POST /jobs/` *Add new JSON data***

### READ FUNCTIONALITY

- **`GET /jobs/proxy/job-type/` *Retrieve New Job Type data***

- **`GET /jobs/proxy/salary/` *Retrieve New Job Salary data***

- **`GET /jobs/` *Retrieve all JSON data***

- **`GET /jobs/{id}/` *Retrieve JSON data by ID***

### UPDATE FUNCTIONALITY

- **`PATCH /jobs/{id}/` *Partially update existing JSON data***

- **`PUT /jobs/{id}/` *Fully update existing JSON data***

### DELETE FUNCTIONALITY

- **`DELETE /jobs/{id}/` *Delete JSON data by ID***

---
# Live Server on Render...
### Use this URL for testing purposes only...

- ***`https://json-server-wnyh.onrender.com`***
