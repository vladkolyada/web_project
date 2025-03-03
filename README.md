# **Worky – Architectural Company Website**

Worky is a website for an architectural company that allows clients to explore services, view the portfolio, read the company blog, and contact the administration.

### **Website Features**

#### _1. Home Page (/home)_

The home page includes:
* A presentation of the company and its activities.
* Information blocks about projects, the team, and partners.
* Contact details for communication.

#### _2. About Page (/about)_

This page provides more details about the company, its mission, the team, and its experience in architecture.

#### _3. Services Page (/services)_

Contains a list of architectural services offered by the company.Each service has a brief description and is presented in a separate block.

#### _4. Blog Page (/blog.)_

The blog is a key element of the website, allowing the company to publish useful materials and news about architecture.

**_Main blog functionality:_**

* Displaying a list of articles:
* Article title.
* Short description.
* Image.
* Publication date.
* Author name.
* "Read More" button to view the full text.

**_Single article (/post)_**

* Full text of the selected post with comments.

**_Blog search (/search)_**

* Filtering articles by keywords.
* Trimming long descriptions to 48 words in search results.

**_Creating new posts (create_post.html)_**

* Form for adding posts with fields for title, text and image.

**_Blog administration (/admin_profile)_**
* The administrator can view, edit and delete posts.


### **Technologies Used:**

Framework: Django(Python)

HTML, CSS, JavaScript(Node.js, React)


## For developers

This project is a web application built with **Django**. It includes a basic structure for web applications, covering settings, routing, models, and templates.

### Project Features

- **Framework**: Django(v.5.1.3)  
- **Structure**:
  - `manage.py` – main script for managing the project
  - `web_project/` – main directory containing project settings (settings.py, urls.py, etc.)
  - `app/` – individual app containing:
    - `models.py` – database models
    - `views.py` – request handling logic
    - `templates/` – HTML templates
    - `static/` – static files (CSS, JS, images)

### Installation & Setup

1. **Clone the repository**  
   ```sh
   git clone https://github.com/vladkolyada/web_project.git
   cd web_project/worky_project
   ```

2. **Apply database migrations**  
   ```sh
   python manage.py migrate
   ```

3. **Run the server**  
   ```sh
   python manage.py runserver
   ```

4. **Open in a browser**  
   ```
   http://127.0.0.1:8000/
   ```
