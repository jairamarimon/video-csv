# Video CSV API
This is a simple REST API built project using Django and Django REST Framework where all video records are stored in a CSV file instead of a database. You can add, update, delete, and sort videos by name, views_count, or post_date.

---

## Setup

### 1. Download and extract the project zip file 


### 2. Set Up Virtual Environment

Navigate to the directory and create a virtual environment

```bash
cd /path/to/extracted/project
python -m venv venv
.\venv\Scripts\activate # for Windows
source venv/bin/activate # for Mac/Linux
```

### 3. Install Dependencies

With the virtual environment activated, install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run Django Server

```bash
python manage.py runserver
```

---

## Endpoints

### 1. GET /videos/

Retrieves a list of all video records. You can optionally sort the results by `name`, `post_date`, or `views_count`, and specify the sorting order (asc or desc).

Query parameters (optional):
- `sort_by`: field to sort by  `name`, `post_date`, or `views_count`
- `order`: field to order by ascending or descending

```
GET http://127.0.0.1:8000/videos/?sort_by=name&order=desc
```

### 2. POST /videos/

Adds a new video record.

```
POST http://127.0.0.1:8000/videos/
```

Sample request body:
```
{
    "id": "3",
    "name": "New Video Sample",
    "href": "https://video.url/3",
    "post_date": "2025-03-01",
    "views_count": 1000
}
```

### 3. GET /videos/{id}/

Retrieves the details of a single video by its `id`.

```
GET http://127.0.0.1:8000/videos/1/
```

### 4. PUT /videos/{id}/

Updates the details of an existing video by its `id`.

```
PUT http://127.0.0.1:8000/videos/1/
```

### 5. DELETE /videos/{id}/

Deletes a video by its `id`.

```
DELETE http://127.0.0.1:8000/videos/1/
```


