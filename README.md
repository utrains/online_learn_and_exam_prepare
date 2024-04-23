# Online Entrance Preparation System

<br>

Our project strives to provide a comprehensive and user-friendly platform that enhances students' knowledge, refines their skills, and boosts their performance in entrance exams.

This online system includes practice questions, mock tests, and interactive quizzes aligned with popular exam syllabuses. It adopts a personalized learning approach, enabling students to identify strengths and weaknesses for targeted improvements. The platform also offers online access for self-paced study, fostering an engaging learning environment to maximize potential and boost confidence for entrance exams.

## Getting Started

If you are new to the project, here are some initial steps to get started:

## STEP 1 : Install python 3
- in our OS (Ubuntu or Windows, --> Install python 3)
- Activate the virtual Env : 
```
mkdir env_project
cd env_project

virtualenv venv 
source venv/bin/activate
```

**1. Clone the project**

```
git clone https://github.com/ghanteyyy/Online-Entrance-Preparation.git
```

**2. Install Dependencies**

```
pip install -r requirements.txt
```

**3. Configure Database**

```
python manage.py makemigrations
```

```
python manage.py migrate
```

**4. Run the server**

```
python manage.py runserver
```

**5. Open following URL in your web browser**

```
127.0.0.1:8000/
```

## Optional Database Configurations

The following configurations are necessary solely for the purpose of generating dummy data for testing.
<br><br>
**1. Populate Questions**

```
python mange.py PopulateQuestions
```

> If you encounter any errors, please ensure that the "Questions.json" file exists within the "static" directory and its contents are formatted correctly as JSON.

**2. Populate Users**

```
python manage.py PopulateUsers
```

**3. Populate Results for respective user**

```
python manage.py PopulateResults
```

## Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Django
- **Database:** sqlite3


# JIRA tickets Stories to Do

As a DevOps engineer tasked with deploying and integrating the described application, I will execute the following actions:

## 1. Deploy and Test Application:
- Follow the provided instructions to deploy and thoroughly test the application.

## 2. Automate Continuous Integration with Jenkins:
- Utilize Jenkins to automate continuous integration for this project.
- Implement containerization skills to create a Docker image of the application.
- Push the Docker image to both a public registry and a private registry.

## 3. Difference Between Public and Private Registries:
- What's the difference between a public and a private register? 
- Give a few examples of each

## 4. Tools for Docker Image Scanning:
- To obtain images that comply with safety standards, it is sometimes necessary to scan them. 
- Name some of the tools needed to scan docker images.
- Tell us which of these tools you can integrate into your CI/CD chain to automatically scan the image generated in the Jenkins pipeline before sending it to the registry.
- justify your choice

## 5. Integrate Image Scanning Tool:
- Integrate __Trivy__ into the CI/CD pipeline to automatically scan the generated Docker image for vulnerabilities.


## 6. Code Vulnerability Scanning Tools:
- Still on the subject of security and obtaining quality code, tell us what tools you know of for scanning and detecting code vulnerabilities. 
- While justifying your choice, tell us which of these tools can be adapted to scan the vulnerabilities of this project.

## 7. Integration of Code Scanning Tools:
- Integrate __SonarQube__ into the CI pipeline to automatically scan the code for vulnerabilities and quality issues.

## 8. Architecture Design using Draw.io:
- Use __Draw.io__ to design the architecture of the integration chain, illustrating the workflow from code commit to image deployment, incorporating Docker image scanning and code vulnerability detection.