## 📚 Table of Contents
<details>
<summary><strong>Click to expand</strong></summary>

- 🚀 [Project Title](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs#-docker-fundamentals--beginner-devops-project)
- ⚡ One-Line Project Summary  
- 🎯 Aim / Objective  
- 🔥 [Real-World Problem Statement](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs#-real-world-problem-statement)  
- 🧠 Core Concept Demonstrated – Docker Fundamentals  
- 🧪 Practical Scenarios Covered  
- 📂 [Learning Implementation (Commands & Examples)](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs#-learning-implementation-commands--examples)  
- 🧰 Tech Stack Used  
- 🧩 Docker Features Utilized  
- 🛠️ [Challenges Faced & Solutions](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs#%EF%B8%8F-challenges-faced--solutions)  
- ▶️ [Execution Demo & Documentation](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs#%EF%B8%8F-execution-demo---documentation)  
- 🧠 Key Learnings for DevOps / SDET Role  
- 🔗 [Proof of Work — Support & Connect](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs#-proof-of-work--support--connect)  
- 👨‍💻 Author  

</details>

---

<h1 align="center">🐳 Docker Fundamentals – Beginner DevOps Project</h1>

<h3 align="center">
Real-World Beginner Project Demonstrating Docker Concepts, Container Lifecycle, Images, Networking & Storage
</h3>

---

<h3 align="center">⚡ One-Line Project Summary</h3>

<p align="center">
A beginner-friendly DevOps learning project demonstrating Docker fundamentals including container lifecycle, Docker commands, image creation using Dockerfile, networking, storage volumes, and environment variables.
</p>

---

<h3 align="center">🎯 Aim / Objective</h3>

<p align="center">
To understand Docker fundamentals from a DevOps perspective by practicing container lifecycle operations, image management, Dockerfile creation, networking, and data persistence.
</p>

---

<h3 align="center">🔥 Real-World Problem Statement</h3>

<p align="center">
In traditional software deployment environments, applications often behave differently across development, testing, and production systems due to dependency conflicts and configuration differences.
</p>

<p align="center">
Docker solves this problem by packaging applications along with their dependencies into containers, ensuring consistent behavior across all environments.
</p>

---

<h3 align="center">🧠 Core Concept Demonstrated – Docker Fundamentals</h3>

<p align="center"><b>Key Docker Concepts Covered</b></p>

<p align="left">
⏳ Containers vs Virtual Machines <br/>
⏳ Docker Images & Docker Hub <br/>
⏳ Container Lifecycle Management <br/>
⏳ Docker CLI Commands <br/>
⏳ Dockerfile & Image Creation <br/>
⏳ Docker Networking <br/>
⏳ Docker Volumes & Data Persistence <br/>
⏳ Environment Variables in Containers <br/>
</p>

<p align="center">
<b>✅ Lightweight containers<br/>
✅ Consistent environments<br/>
✅ Faster deployments</b>
</p>

---

<h3 align="center">🧪 Practical Scenarios Covered</h3>

<p align="left">
✔ Install Docker Community Edition <br/>
✔ Pull images from Docker Hub <br/>
✔ Run containers using <code>docker run</code> <br/>
✔ View running containers using <code>docker ps</code> <br/>
✔ Stop containers using <code>docker stop</code> <br/>
✔ Remove containers using <code>docker rm</code> <br/>
✔ Pull images using <code>docker pull</code> <br/>
✔ Remove images using <code>docker rmi</code> <br/>
✔ Execute commands inside containers using <code>docker exec</code> <br/>
✔ Run containers in detached mode (<code>-d</code>) <br/>
✔ Map container ports using <code>-p</code> <br/>
✔ Pass environment variables using <code>-e</code> <br/>
✔ Persist data using Docker volumes <br/>
✔ Inspect containers using <code>docker inspect</code> <br/>
✔ View container logs using <code>docker logs</code> <br/>
</p>

---

<h3 align="center">📂 Learning Implementation (Commands & Examples)</h3>

<div align="center">

| 🐳 Docker Command | 🎯 Purpose of Command | 🛠️ When It Is Most Commonly Used in Real Projects |
|------------------|----------------------|---------------------------------------------------|
| `docker run nginx` | Creates and starts a new container using the **nginx image** | Used when quickly launching an application container to test containerized services |
| `docker ps` | Displays **all currently running containers** | Used by DevOps engineers to monitor active containers in the environment |
| `docker ps -a` | Lists **all containers (running + stopped)** | Used when debugging container issues or checking container lifecycle history |
| `docker stop <container_id>` | Gracefully stops a running container | Used during deployment updates, maintenance, or when stopping services |
| `docker rm <container_id>` | Removes a stopped container from the system | Used to clean up unused containers and maintain a clean environment |
| `docker pull ubuntu` | Downloads an image from **Docker Hub** to the local machine | Used when preparing base images for building containers or running quick environments |
| `docker run -d nginx` | Runs a container in **detached (background) mode** | Used in production environments where containers must run continuously in the background |
| `docker run -p 80:5000 my-web-app` | Maps **host port to container port** for external access | Used when exposing containerized applications to users or other services |
| `docker run -e APP_COLOR=blue my-web-app` | Passes **environment variables** to configure container behavior | Used for dynamic configuration such as database credentials, API keys, or app settings |
| `docker run -v /opt/data:/var/lib/mysql mysql` | Mounts a **Docker volume for persistent data storage** | Used when containers require persistent data such as databases or logs |

</div>

---

<h3 align="center">🧰 Tech Stack Used</h3> <p align="left"> 🔹 Docker Community Edition <br/> 🔹 Docker CLI <br/> 🔹 Linux / Ubuntu Environment <br/> 🔹 Docker Hub <br/> 🔹 Dockerfile <br/> </p>

---

<h3 align="center">🧩 Docker Features Utilized</h3> <p align="left"> 🔹 Containerization <br/> 🔹 Docker Images <br/> 🔹 Dockerfile <br/> 🔹 Container Lifecycle Management <br/> 🔹 Docker Networking <br/> 🔹 Docker Volumes <br/> 🔹 Environment Variables <br/> 🔹 Image Layering Architecture <br/> </p>

---

<h3 align="center">🛠️ Challenges Faced & Solutions</h3> <div align="center">
Challenge Faced	Solution Implemented
Containers exiting immediately	Learned containers run only while main process is active
Difficulty accessing containerized apps	Used port mapping (-p)
Data lost after container removal	Implemented Docker volumes
Need dynamic container configuration	Used environment variables
</div>

---

<h3 align="center">▶️ Execution Demo & 📄 Documentation</h3>

<table align="center">
<tr>

<td align="center" width="50%">

<b>🎬 Docker Execution Demo</b><br/><br/>

<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/03_Mar/01_%5BDocker%5D%20-%20%F0%9F%90%B3%20Docker%20Fundamentals%20%E2%80%93%20Beginner%20DevOps%20Project/Documents%20and%20Gifs/Extended.gif" width="100%"/>

</td>

<td align="left" width="50%">

<b>📘 Step-by-Step Docker Learning Documentation</b><br/><br/>

<a href="YOUR_REPO_LINK/What%20is%20Docker%20and%20Features_.pdf" target="_blank">
<img src="https://img.shields.io/badge/What%20is%20Docker%20%26%20Features-Open%20PDF-blue?style=for-the-badge&logo=adobeacrobatreader"/>
</a>


<a href="YOUR_REPO_LINK/01_Install%20Docker.pdf" target="_blank">
<img src="https://img.shields.io/badge/01%20Install%20Docker-Open%20Guide-green?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/02_Docker%20Commands_Docker%20run.pdf" target="_blank">
<img src="https://img.shields.io/badge/02%20Docker%20Commands%20(Docker%20Run)-Open%20Guide-blue?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/03_Volume%20Mapping.pdf" target="_blank">
<img src="https://img.shields.io/badge/03%20Docker%20Volume%20Mapping-Open%20Guide-orange?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/04_Environmental%20Variables.pdf" target="_blank">
<img src="https://img.shields.io/badge/04%20Environment%20Variables-Open%20Guide-yellow?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/05_Docker%20Images.pdf" target="_blank">
<img src="https://img.shields.io/badge/05%20Docker%20Images-Open%20Guide-blue?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/06_Docker%20CMD%20vs%20EntryPoint.pdf" target="_blank">
<img src="https://img.shields.io/badge/06%20CMD%20vs%20ENTRYPOINT-Open%20Guide-purple?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/07_Docker%20Networking.pdf" target="_blank">
<img src="https://img.shields.io/badge/07%20Docker%20Networking-Open%20Guide-informational?style=for-the-badge&logo=docker"/>
</a>



<a href="YOUR_REPO_LINK/08_Docker%20Storage.pdf" target="_blank">
<img src="https://img.shields.io/badge/08%20Docker%20Storage-Open%20Guide-red?style=for-the-badge&logo=docker"/>
</a>

</td>

</tr>
</table>

---

<h3 align="center">🧠 Key Learnings for DevOps / SDET Role</h3> <p align="left"> ✔ Understanding containerization fundamentals <br/> ✔ Managing Docker containers and images <br/> ✔ Implementing networking and port mapping <br/> ✔ Persisting application data using volumes <br/> ✔ Configuring containers with environment variables <br/> </p>

---

<h3 align="center">🔗 Proof of Work — Support & Connect</h3>

<p align="center">
<strong>If this project added value to you, please support by <b>liking</b>, <b>commenting(rating ⭐ out of 5)</b>, and <b>sharing</b> the LinkedIn post below 🚀</strong>
</p>

<p align="center">
  <a href="" target="_blank">
    <img src="https://img.shields.io/badge/👍%20Like%20|%20💬%20Comment%20|%20🔁%20Share%20the%20LinkedIn%20Post-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a></br>
  <a href="https://github.com/RouthKiranBabu/LeetCode-Using-Java-JavaScript-and-Python/blob/main/Submissions/README.md#-submissions-by-year--month" target="_blank">
    <img src="https://img.shields.io/badge/Upvote%20My%20LeetCode%20Submission-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/>
  </a>
  <a href="https://routhkiranbabu.github.io/Strava_stats/" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20My%20Live%20Strava%20Stats-FC4C02?style=for-the-badge&logo=strava&logoColor=white"/>
  </a>
  <a href="https://github.com/RouthKiranBabu" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20Me%20on%20GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>


---

<h3 align="center">👨‍💻 Author</h3> <p align="center"> <b>Routh Kiran Babu</b><br/> Aspiring DevOps Engineer | SDET | Automation Enthusiast </p> <p align="center"> ⭐ If this repository helped you, don't forget to star it! </p> `
