## 📚 Table of Contents
<details>
<summary><strong>Click to expand</strong></summary>

- 🚀 ThinkBoard – MERN Notes App (CRUD + MongoDB + Render Deployment)
- ⚡ One-Line Project Summary
- 🎯 Aim / Objective
- 🔥 Real-World Problem Statement
- 🧠 Core Concepts Demonstrated (MERN + REST API + Rate Limiting)
- 🧪 Features Implemented (End-to-End)
- 🔗 Live Demo
- 🧰 Tech Stack Used
- 📂 Project Structure Overview
- 🛠️ API Endpoints (Tested via Postman)
- 🧩 Highlights That Recruiters Look For
- ▶️ Execution Demo & 📄 Documentation
- 🧠 Key Learnings for SDET / Full Stack Role
- 🔗 Proof of Work — Support & Connect
- 👨‍💻 Author

</details>

---

<h1 align="center">🧠 ThinkBoard – MERN Notes App</h1>

<h3 align="center">
A production-ready MERN Notes application with REST API, MongoDB persistence, rate limiting, and cloud deployment on Render.
</h3>

---

<h3 align="center">📌 One-Line Project Summary</h3>

<p align="center">
ThinkBoard is a full-stack MERN Notes application that supports complete CRUD operations, MongoDB Atlas persistence, Postman-tested REST APIs, and production deployment on Render with a responsive modern UI.
</p>

---

<h3 align="center">🎯 Aim / Objective</h3>

<p align="center">
To build and deploy a real-world MERN application that demonstrates strong backend API design, database integration, frontend routing, middleware handling, and cloud deployment — aligned with modern industry expectations.
</p>

---

<h3 align="center">🔥 Real-World Problem Statement</h3>

<p align="center">
Many beginner projects stop at UI-only apps and never reach real production standards.  
In real software engineering roles, companies expect candidates to build full-stack systems with real APIs, real databases, testing, error handling, security, and deployment.
</p>

<p align="center">
<b>ThinkBoard solves this by delivering a complete MERN project from development → testing → deployment.</b>
</p>

---

<h3 align="center">🧠 Core Concepts Demonstrated (MERN + REST API + Rate Limiting)</h3>

<p align="left">
✅ React Frontend with Routing (Home / Create / Detail) <br/>
✅ Express REST API (GET / POST / PUT / DELETE) <br/>
✅ MongoDB Atlas + Mongoose Schema + Model <br/>
✅ Postman API Testing on localhost before deployment <br/>
✅ Middleware-based architecture (controllers + routes separation) <br/>
✅ Upstash Redis Rate Limiting (429 protection against spam requests) <br/>
✅ Production Build Serving (frontend dist served via backend) <br/>
✅ Environment Variables & Secure Config (.env) <br/>
</p>

---

<h3 align="center">🧪 Features Implemented (End-to-End)</h3>

<p align="left">
✔ Create Notes (Title + Content) <br/>
✔ View Notes in Responsive Grid Layout <br/>
✔ View Note Detail Page (Edit & Update) <br/>
✔ Delete Notes from Card UI <br/>
✔ Delete Notes from Detail Page <br/>
✔ Toast Notifications for CRUD Success/Failure <br/>
✔ Rate Limit UI Screen (429 Handling) <br/>
✔ MongoDB Persistence (Notes remain after refresh) <br/>
✔ Production Deployment on Render Free Plan <br/>
</p>

---

<h3 align="center">🔗 Live Demo</h3>

<p align="center">
<a href="https://mern-thinkboard-cc2l.onrender.com" target="_blank">
  <img src="https://img.shields.io/badge/🌍%20Live%20Demo%20(ThinkBoard)-Click%20Here-00C853?style=for-the-badge&logo=render&logoColor=white"/>
</a>
</p>

<p align="center">
<b>⚠️ Render Free Plan Notice:</b> This demo may automatically go inactive after ~15 minutes of inactivity.<br/>
To keep it responsive, please interact with the application at least once every 15 minutes.<br/>
If the demo is sleeping, feel free to message me on LinkedIn — I’ll activate it immediately.
</p>

<p align="center">
<a href="https://www.linkedin.com/in/routhkiranbabu/" target="_blank">
  <img src="https://img.shields.io/badge/Message%20Me%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
</p>

---

<h3 align="center">🧰 Tech Stack Used</h3>

<p align="left">
🔹 Frontend: React + React Router <br/>
🔹 UI Styling: Tailwind CSS + DaisyUI <br/>
🔹 Backend: Node.js + Express.js <br/>
🔹 Database: MongoDB Atlas + Mongoose <br/>
🔹 API Testing: Postman <br/>
🔹 Deployment: Render (Free Plan) <br/>
🔹 Security & Stability: Upstash Redis Rate Limiting <br/>
</p>

---

<h3 align="center">📂 Project Structure Overview</h3>

<p align="left">
📁 <code>backend/</code> <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/config/</code> → MongoDB + Upstash setup <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/controllers/</code> → Notes CRUD logic <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/middleware/</code> → Rate limiter middleware <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/models/</code> → Mongoose Note Schema <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/routes/</code> → Notes REST routes <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📄 <code>src/server.js</code> → Express server + production config <br/><br/>

📁 <code>frontend/</code> <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/components/</code> → Navbar, NoteCard, UI states <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/pages/</code> → Home, Create, NoteDetail pages <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📁 <code>src/lib/</code> → Axios baseURL + helpers <br/>
&nbsp;&nbsp;&nbsp;&nbsp;📄 <code>src/App.jsx</code> → Routing setup <br/>
</p>

---

<h3 align="center">🛠️ API Endpoints (Tested via Postman)</h3>

<div align="center">

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/notes` | Fetch all notes |
| GET | `/api/notes/:id` | Fetch note by ID |
| POST | `/api/notes` | Create a new note |
| PUT | `/api/notes/:id` | Update note by ID |
| DELETE | `/api/notes/:id` | Delete note by ID |

</div>

<br/>

<p align="center">
<b>📌 Postman Collection (Exported JSON)</b><br/>
<i>Recruiters / reviewers can instantly import this collection and validate the complete CRUD API flow on localhost.</i>
</p>

<p align="center">
<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Notes_CRUD_API_Testing.postman_collection.json" target="_blank">
  <img src="https://img.shields.io/badge/⬇️%20Download%20Postman%20Collection%20(JSON)-CRUD%20API%20Testing-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
</a>
</p>

---

<h3 align="center">🧩 Highlights That Recruiters Look For</h3>

<p align="left">
⭐ Full Stack Project (Frontend + Backend + Database) <br/>
⭐ Clean separation of concerns (routes, controllers, models, middleware) <br/>
⭐ Postman-tested REST APIs (local validation before deployment) <br/>
⭐ Production deployment with correct build serving configuration <br/>
⭐ Middleware-based rate limiting (enterprise practice) <br/>
⭐ Error handling flow (429 / 404 / 500) <br/>
⭐ Responsive UI + clean modern design (Tailwind + DaisyUI) <br/>
</p>

---

<h3 align="center">▶️ Execution Demo & 📄 Step-by-Step Documentation</h3>

<table align="center">
<tr>

<td align="center" width="50%">

<b>🎬 Execution Proof (3 GIFs)</b><br/><br/>

<b>✅ 01) API Tested via Postman (CRUD)</b><br/>
<i>Create • Read • Update • Delete Notes using REST API</i><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Gifs/API_Tested_In_Postman.gif" width="100%"/><br/><br/>

<b>✅ 02) Application CRUD Flow (MongoDB Atlas Persistence)</b><br/>
<i>UI CRUD operations + data persists after refresh</i><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Gifs/CRUD_Note_Document.gif" width="100%"/><br/><br/>

<b>✅ 03) Responsive UI + MERN Interaction Block Diagram</b><br/>
<i>Responsive layout + architecture showing React ↔ Node/Express ↔ MongoDB</i><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Gifs/mern.gif" width="100%"/>

</td>

<td align="left" width="50%">

<b>📘 Step-by-Step Beginner Documentation (13 PDFs)</b><br/>
<i>From development → API testing → production deployment (Render + MongoDB Atlas)</i><br/><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/01_Setting%20Up%20Our%20Backend%20%26%20Basics.pdf" target="_blank">
  <img src="https://img.shields.io/badge/01%20-%20Setting%20Up%20Our%20Backend%20%26%20Basics-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/02_Nodemon%20and%20Setting%20up%20Our%20Routes.pdf" target="_blank">
  <img src="https://img.shields.io/badge/02%20-%20Nodemon%20%26%20Setting%20Up%20Our%20Routes-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/03_Optimizing%20Our%20File%20and%20Folder%20Structure.pdf" target="_blank">
  <img src="https://img.shields.io/badge/03%20-%20Optimizing%20Our%20File%20and%20Folder%20Structure-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/04_Setting%20Up%20Our%20Database(MongoDB).pdf" target="_blank">
  <img src="https://img.shields.io/badge/04%20-%20Setting%20Up%20Our%20Database%20(MongoDB)-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/05_Completing%20Our%20Controllers.pdf" target="_blank">
  <img src="https://img.shields.io/badge/05%20-%20Completing%20Our%20Controllers-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/06_Middleware%20and%20Rate%20Limiting.pdf" target="_blank">
  <img src="https://img.shields.io/badge/06%20-%20Middleware%20and%20Rate%20Limiting-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/07_Frontend%20Setup_React.js.pdf" target="_blank">
  <img src="https://img.shields.io/badge/07%20-%20Frontend%20Setup%20(React.js)-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/08_Home%20Page.pdf" target="_blank">
  <img src="https://img.shields.io/badge/08%20-%20Home%20Page-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/09_Create%20Page.pdf" target="_blank">
  <img src="https://img.shields.io/badge/09%20-%20Create%20Page-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/10_Delete%20Functionality.pdf" target="_blank">
  <img src="https://img.shields.io/badge/10%20-%20Delete%20Functionality-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/11_Note%20Detail%20Page.pdf" target="_blank">
  <img src="https://img.shields.io/badge/11%20-%20Note%20Detail%20Page-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/12_Super%20Detailed%20Deployment.pdf" target="_blank">
  <img src="https://img.shields.io/badge/12%20-%20Super%20Detailed%20Deployment-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/02_%5BMERN%5D%20-%20ThinkBoard%20%E2%80%93%20MERN%20Notes%20App%20(CRUD%20%2B%20MongoDB%20%2B%20Render%20Deployment)/Documents%20and%20Gifs/Documents/13_Making%20Live%20After%2015%20minutes%20of%20Inactivity.pdf" target="_blank">
  <img src="https://img.shields.io/badge/13%20-%20Making%20Live%20After%2015%20Minutes%20of%20Inactivity-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a>

</td>

</tr>
</table>

---

<h3 align="center">🧠 Key Learnings for SDET / Full Stack Role</h3>

<p align="left">
✔ Built a complete REST API with Express.js <br/>
✔ Designed schema-driven persistence using MongoDB + Mongoose <br/>
✔ Implemented middleware-based rate limiting (enterprise practice) <br/>
✔ Tested APIs using Postman before UI integration <br/>
✔ Learned production deployment flow (frontend build + backend serving) <br/>
✔ Implemented proper error handling (404, 429, 500) <br/>
✔ Developed real-world debugging skills (CORS, headers, API failures) <br/>
</p>

---

<h3 align="center">🔗 Proof of Work — Support & Connect</h3>

<p align="center">
<strong>If this project added value to you, please support by <b>liking</b>, <b>commenting (rating ⭐ out of 5)</b>, and <b>sharing</b> the LinkedIn post below 🚀</strong>
</p>

<p align="center">
  <a href="linkedin_link" target="_blank">
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

<h3 align="center">👨‍💻 Author</h3>

<p align="center">
<b>Routh Kiran Babu</b><br/>
Aspiring SDET | MERN Stack Developer | Automation Enthusiast
</p>

<p align="center">
⭐ If this repository helped you, don't forget to star it!
</p>
