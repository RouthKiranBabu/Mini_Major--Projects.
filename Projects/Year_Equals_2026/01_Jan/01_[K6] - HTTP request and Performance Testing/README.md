## 📚 Table of Contents
<details>
<summary><strong>Click to expand</strong></summary>

- 🚀 [Project Title](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing#-k6-performance-testing--load-test-with-virtual-users)  
- ⚡ One-Line Project Summary  
- 🎯 Aim / Objective  
- 🔥 Real-World Problem Statement  
- 🧠 [Core Concept Demonstrated – k6 Load Testing](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing#-core-concept-demonstrated--k6-load-testing)  
- 🧪 Test Scenarios Covered  
- 📂 [Actual Performance Test Code (With Comments)](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing#-actual-performance-test-code-with-comments)  
- 🧰 Tech Stack Used  
- 🧩 k6 Features Utilized  
- 🛠️ [Challenges Faced & Solutions](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing#%EF%B8%8F-challenges-faced--solutions)  
- 📂 Project Structure Overview  
- ▶️ [Execution Demo & Documentation](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing#%EF%B8%8F-execution-demo---documentation)  
- 🧠 Key Learnings for SDET Role  
- 🔗 [Proof of Work — Support & Connect](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing#-proof-of-work--support--connect)  
- 👨‍💻 Author  

</details>

---

<h1 align="center">🚀 k6 Performance Testing – Load Test with Virtual Users</h1>

<h3 align="center">
Real-World Performance Testing Project Using k6, Virtual Users & HTTP Checks
</h3>

---

<h3 align="center">📌 One-Line Project Summary</h3>

<p align="center">
A real-world k6 performance testing project demonstrating how to simulate concurrent users, validate API responses, and analyze system stability under load.
</p>

---

<h3 align="center">🎯 Aim / Objective</h3>

<p align="center">
To demonstrate how an SDET can design and execute a basic yet production-relevant load test using k6 by simulating multiple virtual users and validating HTTP response behavior.
</p>

---

<h3 align="center">🔥 Real-World Problem Statement</h3>

<p align="center">
In real-world applications, systems must handle multiple users simultaneously without failures or performance degradation.  
This project demonstrates how k6 helps identify system stability by applying load and validating response correctness — a critical SDET responsibility.
</p>

---

<h3 align="center">🧠 Core Concept Demonstrated – k6 Load Testing</h3>

<p align="center"><b>This project demonstrates:</b></p>

<p align="left">
⏳ Virtual Users (VUs) simulation <br/>
⏳ Concurrent HTTP request handling <br/>
⏳ Response status validation <br/>
⏳ Realistic user behavior using sleep <br/>
⏳ Time-based load execution <br/>
</p>

<p align="center">
<b>✅ Non-UI performance testing<br/>
✅ Scalable load generation<br/>
✅ Fast CLI-based execution</b>
</p>

---

<h3 align="center">🧪 Test Scenarios Covered</h3>

<p align="left">
✔ Simulate 10 concurrent virtual users <br/>
✔ Execute test for a fixed duration (15 seconds) <br/>
✔ Send HTTP GET requests to production-like URL <br/>
✔ Validate HTTP 200 status using checks <br/>
✔ Introduce think time using sleep <br/>
</p>

---

<h3 align="center">📂 Actual Performance Test Code (With Comments)</h3>

<p align="center">
This section provides direct access to the <b>actual k6 performance test script</b>, including
<b>clear comments</b> explaining load configuration, checks, and execution flow.
</p>

<p align="center">
👉 <b>Click the button below to view the source code</b>
</p>

<p align="center">
<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing/JavaScript.js" target="_blank">
  <img src="https://img.shields.io/badge/View%20Actual%20k6%20Code-Click%20Here-2EA44F?style=for-the-badge&logo=github&logoColor=white"/>
</a>
</p>

<p align="center">
<b>🔍 What reviewers will find inside:</b><br/>
✔ Virtual Users configuration<br/>
✔ HTTP request execution<br/>
✔ Response validation using <code>check()</code><br/>
✔ Realistic load behavior using <code>sleep()</code>
</p>

---

<h3 align="center">🛠️ Tech Stack Used</h3> <p align="left"> 🔹 k6 <br/> 🔹 JavaScript <br/> 🔹 HTTP Protocol <br/> 🔹 CLI-based Test Execution <br/> </p>

---

<h3 align="center">🧩 k6 Features Utilized</h3> <p align="left"> 🔹 Virtual Users (VUs) <br/> 🔹 Duration-based load execution <br/> 🔹 HTTP module <br/> 🔹 Checks for validation <br/> 🔹 Sleep for realistic traffic simulation <br/> </p>

---

<h3 align="center">🛠️ Challenges Faced & Solutions</h3>

<div align="center">

| Challenge Faced | Solution Implemented |
|----------------|---------------------|
| Understanding Virtual User (VU) behavior | Used simple VU + duration-based load configuration |
| Validating performance correctness | Applied k6 <code>check()</code> assertions |
| Simulating real-world user behavior | Introduced controlled <code>sleep()</code> intervals |

</div>


---

<h3 align="center">📂 Project Structure Overview</h3> <p align="left"> 📄 <code>performance-test.js</code> – k6 test script <br/> 📁 <code>Document And Gif/</code> – Execution proof & documentation <br/> 📄 <code>README.md</code> – Project documentation <br/> </p>

---

<h3 align="center">▶️ Execution Demo & 📄 Documentation</h3> <table align="center"> <tr> <td align="center" width="50%">

<b>🎬 k6 Execution Demo</b><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing/Document%20and%20Gif/video.gif" width="100%"/>

<p align="center"> Shows writing the test → executing via CLI → observing real-time results </p> </td> <td align="center" width="50%">

<b>📘 Step-by-Step Documentation</b><br/><br/>
<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/01_Jan/01_%5BK6%5D%20-%20HTTP%20request%20and%20Performance%20Testing/Document%20and%20Gif/%F0%9F%9A%80%20k6%20Performance%20Testing%20Project.pdf" target="_blank">
<img src="https://img.shields.io/badge/View%20PDF-Installation%20&%20Usage-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a>

<p align="center"> Includes installation, commands, configuration & output explanation </p> </td> </tr> </table>

---

<h3 align="center">🧠 Key Learnings for SDET Role</h3> <p align="left"> ✔ Performance testing fundamentals <br/> ✔ Writing scalable load tests using k6 <br/> ✔ Validating system behavior under load <br/> ✔ CLI-based automation execution <br/> ✔ Industry-relevant SDET performance skills <br/> </p>

---

<h3 align="center">🔗 Proof of Work — Support & Connect</h3>

<p align="center">
<strong>If this project added value to you, please support by <b>liking</b>, <b>commenting(rating ⭐ out of 5)</b>, and <b>sharing</b> the LinkedIn post below 🚀</strong>
</p>

<p align="center">
  <a href="https://www.linkedin.com/posts/routhkiranbabu_im-happy-to-share-this-k6-load-testing-activity-7412396236294565888-RTA4?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC0fSW0BCXvPinW6E3cbBZFekfnprC0b-FU" target="_blank">
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

<h3 align="center">👨‍💻 Author</h3> <p align="center"> <b>Routh Kiran Babu</b><br/> Aspiring SDET | Performance & Automation Testing Enthusiast </p> <p align="center"> ⭐ If this repository helped you, don't forget to star it! </p> 
