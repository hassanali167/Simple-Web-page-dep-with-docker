# 🚀 Sample Flask Web Project Deployment (Docker + Proxmox)

This project is a **simple and responsive two-page website** built using **HTML, CSS, and Python Flask**, designed to demonstrate **containerized deployment using Docker** on a **Proxmox Virtual Machine**.

> 🔥 While the website content is basic, the main objective of this project is to practice cloud-native deployment using virtualization and containerization technologies.

---

## 🌐 Website Overview

- **Welcome Page**: Beautiful landing page with project intro and animation.
- **About Page**: Information about the developers, project purpose, and CV download links.
- **Responsive Design**: Mobile and desktop-friendly layout with smooth animations.
- **CV Download**: Each team member’s CV is downloadable as a PDF.

---

## 🧑‍💻 Project Members

- **Hassan Ali**
- **Fahad Sajid**

CVs are available to download via the [About Page](http://localhost:5000/about).

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- HTML5 / CSS3
- Google Fonts
- Docker
- Proxmox (for VM creation)

---

## 📦 Folder Structure

```
project/
│
├── app.py                  # Flask application
├── Dockerfile              # Docker build file
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── welcome.html
│   └── about.html
├── static/                 # Static files (CSS, PDFs)
│   ├── style.css
│   ├── hassan_cv.pdf
│   └── fahad_cv.pdf
├── README.md               # This file
```

---

## 📸 Screenshots (Optional)

| Welcome Page | About Page |
|--------------|------------|
| ![Welcome Screenshot](screenshots/welcome.png) | ![About Screenshot](screenshots/about.png) |

> You can upload screenshots and link them here.

---

## 🧱 How It Works

We created a virtual machine inside a **Proxmox Cluster**, installed **Docker**, built the Flask app into a Docker container, and ran it as a service on the VM.

This mimics real-world cloud-native deployment and helps practice DevOps concepts.

---


### 📦 Docker Usage in This Project

In this project, Docker is used to **containerize** the Flask web application.

- A **Dockerfile** is created that defines the environment, dependencies, and instructions needed to run the app.
- This Docker image ensures that the application can run reliably in any environment, regardless of local machine differences.
- The built Docker container is deployed inside a **virtual machine hosted on a Proxmox Cluster**.

---

### 🐳 How Docker is Used

1. **Dockerfile** defines:
   - The base image (`python:3.10-slim` or similar).
   - Copying application files.
   - Installing dependencies from `requirements.txt`.
   - Running the Flask app.

2. **Build Docker Image**:

   ```bash
   docker build -t flask-web-project .
   ```

3. **Run Docker Container**:

   ```bash
   docker run -d -p 5000:5000 flask-web-project
   ```

4. The app becomes available on the VM's IP address at port `5000`.

---

### 🚀 Why Docker is Important in This Project

- **Consistency**: Docker ensures that the app runs the same way everywhere — no "it works on my machine" issues.
- **Portability**: The app can be moved across VMs, servers, or cloud providers easily by shipping the Docker image.
- **Isolation**: The Flask app runs isolated from the host system and other apps, avoiding conflicts.
- **Scalability**: Using Docker makes it easier to scale up (running multiple containers) if needed in the future.
- **Efficiency**: Containers are lightweight compared to full virtual machines, reducing resource usage and deployment time.
- **Professional Practice**: Using Docker is a real-world industry standard, making this deployment more aligned with DevOps and cloud-native practices.





---
## 🚀 Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/hassanali167/Simple-Web-page-dep-with-docker
```

### 2. 🐍 Set up a Python Virtual Environment (Optional for local testing)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. 🐳 Run with Docker (Preferred)

#### Step 1: Build the Docker image

```bash
docker build -t flask-web-project .
```

#### Step 2: Run the Docker container

```bash
docker run -d -p 5000:5000 flask-web-project
```

Access the web app at:  
📍 `http://<your_vm_ip>:5000`

---

## 📡 Deployment Notes

- The project is deployed inside a Docker container on a VM hosted in a **Proxmox cluster**.
- Make sure Docker is installed and running on your VM.
- CV files are placed in the `static/` folder to enable direct download via the web app.

---

## 🧠 Future Improvements (Optional Ideas)

- Add a contact form with Flask backend
- Use Flask Blueprints for larger projects
- Deploy using CI/CD pipeline (e.g., GitHub Actions + Docker Hub)
- Host on a cloud platform (like AWS EC2, GCP, etc.)

---

## 📧 Contact / Credits

Developed by:

- [Hassan Ali](mailto:hassanali1335@outlook.com)  
- [Fahad Sajid](mailto:fahadsajid492@gmail.com)

---

## 📜 License

This project is for educational purposes only.  
Feel free to fork and modify for your own learning!
