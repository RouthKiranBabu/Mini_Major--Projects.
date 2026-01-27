## 📚 Table of Contents
<details>
<summary><strong>Click to expand</strong></summary>

- 🚀 Project Title  
- ⚡ One-Line Project Summary  
- 🎯 Aim / Objective  
- 🔥 Real-World Problem Statement  
- 🧠 Core Concepts Demonstrated – Express.js Backend  
- 🧩 Backend Features Implemented  
- 📂 Server & Router Code Overview  
- 🔀 User ↔ Browser ↔ Express Flow  
- 🧪 Functional Scenarios Covered  
- 🛠️ Challenges Faced & Solutions  
- 📂 Project Structure Overview  
- ▶️ Execution Demo & Documentation  
- 🧠 Key Learnings for Backend / SDET Role  
- 🔗 Proof of Work — Support & Connect  
- 👨‍💻 Author  

</details>

---

<h1 align="center">🚀 Express.js Backend – User Management & Routing Architecture</h1>

<h3 align="center">
Real-World Express.js Backend Project Demonstrating Routing, Middleware, Query Parameters, EJS Rendering & Data Flow
</h3>

---

<h3 align="center">📌 One-Line Project Summary</h3>

<p align="center">
A hands-on Express.js backend project showcasing modular routing, form handling, query-based filtering, middleware execution, and browser-to-server interaction using EJS templates.
</p>

---

<h3 align="center">🎯 Aim / Objective</h3>

<p align="center">
To design and implement a structured Express.js backend that demonstrates real-world server concepts such as routing, middleware, form submissions, query parameters, dynamic rendering, and user interaction flow.
</p>

---

<h3 align="center">🔥 Real-World Problem Statement</h3>

<p align="center">
In backend development, managing user input, routing complexity, and request flow between browser and server is critical.  
This project demonstrates how Express.js handles HTTP requests, form data, dynamic routing, and query-based filtering in a clean and scalable way.
</p>

---

<h3 align="center">🧠 Core Concepts Demonstrated – Express.js Backend</h3>

<p align="left">
✔ Express server setup & lifecycle <br/>
✔ Modular routing using <code>express.Router()</code> <br/>
✔ Handling GET, POST & dynamic routes <br/>
✔ Middleware execution flow <br/>
✔ Query parameters for filtering data <br/>
✔ Form handling using <code>express.urlencoded()</code> <br/>
✔ Dynamic UI rendering using EJS <br/>
</p>

---

<h3 align="center">🧩 Backend Features Implemented</h3>

<p align="left">
🔹 User creation via HTML form <br/>
🔹 Dynamic URL-based user navigation <br/>
🔹 Gender-based user filtering using query params <br/>
🔹 Incremental user ID management <br/>
🔹 Server-side rendering with fallback defaults <br/>
🔹 Data persistence using in-memory arrays <br/>
</p>

---

<h3 align="center">📂 Server & Router Code Overview</h3>

<p align="left">
<b>🔹 Server Responsibilities:</b><br/>
• Initialize Express server<br/>
• Configure middleware for form parsing<br/>
• Configure EJS view engine<br/>
• Attach modular user router<br/>
• Start HTTP server on port 3000<br/><br/>

<b>🔹 Router Responsibilities:</b><br/>
• Handle user listing requests<br/>
• Handle user creation workflow<br/>
• Manage dynamic user IDs<br/>
• Process query parameters<br/>
• Execute route-specific middleware using <code>router.param</code><br/>
</p>

---

<h3 align="center">🔀 User ↔ Browser ↔ Express Flow</h3>

<p align="center">
This project visually explains how a user request flows from the browser to the Express server and back.
</p>

<p align="center">
<b>📊 Interaction Flow Diagram</b><br/><br/>
<img src="GIF_LINK_1_HERE" width="90%"/>
</p>

<p align="center">
<b>🎬 Live User Interaction Demo</b><br/><br/>
<img src="GIF_LINK_2_HERE" width="90%"/>
</p>

---

<h3 align="center">🧪 Functional Scenarios Covered</h3>

<p align="left">
✔ Add users via browser form <br/>
✔ Auto-increment user IDs <br/>
✔ Redirect users after submission <br/>
✔ Retrieve all users via GET request <br/>
✔ Filter users using query parameters (gender) <br/>
✔ Render dynamic values using EJS <br/>
✔ Handle empty and default states safely <br/>
</p>

---

<h3 align="center">🛠️ Challenges Faced & Solutions</h3>

<div align="center">

| Challenge Faced | Solution Implemented |
|----------------|---------------------|
| Managing dynamic user IDs | Used controlled ID incrementation |
| Handling form data | Used <code>express.urlencoded()</code> middleware |
| Route complexity | Modularized routes using <code>express.Router()</code> |
| Dynamic data rendering | Used EJS with fallback defaults |
| Query-based filtering | Implemented <code>req.query</code> logic |

</div>

---

<h3 align="center">📂 Project Structure Overview</h3>

<p align="left">
📁 <code>routes/</code> – Modular route handling logic <br/>
📁 <code>views/</code> – EJS templates for UI rendering <br/>
📁 <code>public/</code> – Static assets <br/>
📄 <code>server.js</code> – Express server entry point <br/>
</p>

---

<h3 align="center">▶️ Execution Demo & 📄 Documentation</h3>

<table align="center">
<tr>
<td align="center" width="50%">

<b>📘 Step-by-Step Implementation Guide</b><br/><br/>
<a href="PDF_LINK_1_HERE" target="_blank">
  <img src="https://img.shields.io/badge/View%20PDF-Step--by--Step%20Guide-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a>

</td>

<td align="center" width="50%">

<b>📐 Architecture & Backend Design</b><br/><br/>
<a href="PDF_LINK_2_HERE" target="_blank">
  <img src="https://img.shields.io/badge/View%20PDF-Architecture%20Design-blue?style=for-the-badge&logo=adobeacrobatreader"/>
</a>

</td>
</tr>
</table>

---

<h3 align="center">🧠 Key Learnings for Backend / SDET Role</h3>

<p align="left">
✔ Understanding Express.js request lifecycle <br/>
✔ Writing clean, modular backend code <br/>
✔ Handling real-world form submissions <br/>
✔ Query parameter usage for data filtering <br/>
✔ Middleware-based request processing <br/>
✔ Backend debugging & flow tracing <br/>
</p>

---

<h3 align="center">🔗 Proof of Work — Support & Connect</h3>

<p align="center">
<strong>If this project added value to you, please support by <b>liking</b>, <b>commenting (⭐ out of 5)</b>, and <b>sharing</b> 🚀</strong>
</p>

<p align="center">
  <a href="LINKEDIN_POST_LINK" target="_blank">
    <img src="https://img.shields.io/badge/👍%20Like%20|%20💬%20Comment%20|%20🔁%20Share-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a><br/>
  <a href="https://github.com/RouthKiranBabu" target="_blank">
    <img src="https://img.shields.io/badge/Follow%20Me%20on%20GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

<h3 align="center">👨‍💻 Author</h3>

<p align="center">
<b>Routh Kiran Babu</b><br/>
Backend Developer | Express.js Enthusiast | Aspiring SDET
</p>

<p align="center">
⭐ If this repository helped you, don't forget to star it!
</p>
