## 📚 Table of Contents
<details>
<summary><strong>Click to expand</strong></summary>

- 🚀 [Project Title](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management#-mongodb-query-lab--crud-indexing-and-collection-management)  
- ⚡ One-Line Project Summary  
- 🎯 Aim / Objective  
- 🔥 [Real-World Problem Statement](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management#-real-world-problem-statement)  
- 🧠 Core Concepts Demonstrated – MongoDB Collections, Queries & Indexing  
- 🧪 Operations & Scenarios Covered  
- 📂 [Exported Sample Dataset (MongoDB Compass JSON)](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management#-exported-sample-dataset-mongodb-compass-json)  
- 🧰 Tech Stack Used  
- 🧩 MongoDB Features Utilized  
- 🛠️ [Challenges Faced & Solutions](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management#%EF%B8%8F-challenges-faced--solutions)  
- 📂 Project Structure Overview  
- ▶️ [Execution Demo & Documentation (PDFs + GIF)](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management#%EF%B8%8F-execution-demo---documentation)  
- 🧠 Key Learnings for SDET / Backend Role  
- 🔗 [Proof of Work — Support & Connect](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management#-proof-of-work--support--connect)  
- 👨‍💻 Author  

</details>

---

<h1 align="center">🚀 MongoDB Query Lab – CRUD, Indexing, and Collection Management</h1>

<h3 align="center">
A real-world MongoDB hands-on project demonstrating Collections, CRUD operations, Query Operators, and Index Optimization using mongosh + VS Code + Compass
</h3>

---

<h3 align="center">📌 One-Line Project Summary</h3>

<p align="center">
A practical MongoDB project showcasing database creation, collection management, CRUD operations, filtering, sorting, projection, logical/comparison operators, capped collections, and indexing with performance validation using <code>explain("executionStats")</code>.
</p>

---

<h3 align="center">🎯 Aim / Objective</h3>

<p align="center">
To demonstrate real-world MongoDB database handling by building a structured dataset, performing advanced queries, managing collections, and improving query performance using indexes — exactly what backend and SDET candidates must understand in modern applications.
</p>

---

<h3 align="center">🔥 Real-World Problem Statement</h3>

<p align="center">
In real-world backend systems, poor database design and inefficient queries lead to slow APIs and performance bottlenecks.  
This project demonstrates how MongoDB collections are structured, how queries work in production, and how indexes reduce document scans to improve query speed.
</p>

---

<h3 align="center">🧠 Core Concepts Demonstrated – MongoDB Collections, Queries & Indexing</h3>

<p align="center"><b>This project covers MongoDB fundamentals with real commands and proof:</b></p>

<p align="left">
📌 Database vs Collection vs Document <br/>
📌 CRUD Operations (Insert, Find, Update, Delete) <br/>
📌 Projection & Filtering <br/>
📌 Sorting & Limiting <br/>
📌 Comparison Operators (<code>$gt</code>, <code>$gte</code>, <code>$lt</code>, <code>$lte</code>, <code>$ne</code>, <code>$in</code>, <code>$nin</code>) <br/>
📌 Logical Operators (<code>$or</code>, <code>$nor</code>, <code>$not</code>) <br/>
📌 Capped Collections (Size + Max documents) <br/>
📌 Indexing + Query Performance (<code>COLLSCAN</code> vs <code>IXSCAN</code>) <br/>
</p>

<p align="center">
<b>✅ Real mongosh commands<br/>
✅ Compass GUI operations<br/>
✅ Exportable dataset for reuse</b>
</p>

---

<h3 align="center">🧪 Operations & Scenarios Covered</h3>

<p align="left">
✔ Install MongoDB + Setup mongosh + Environment Variables <br/>
✔ Create Database and Collections (<code>school</code>, <code>students</code>, <code>teachers</code>, <code>courses</code>) <br/>
✔ Insert Documents (<code>insertOne</code>, <code>insertMany</code>) <br/>
✔ Read Documents (<code>find</code>, filters, projection) <br/>
✔ Sort & Limit results (<code>sort</code>, <code>limit</code>) <br/>
✔ Update Documents (<code>updateOne</code>, <code>updateMany</code>, <code>$set</code>, <code>$unset</code>, <code>$exists</code>) <br/>
✔ Delete Documents (<code>deleteMany</code>) + Recovery via export <br/>
✔ Comparison Queries (<code>$gte</code>, <code>$lte</code>, <code>$in</code>, <code>$nin</code>) <br/>
✔ Logical Operators (<code>$or</code>, <code>$nor</code>, <code>$not</code>) <br/>
✔ Index Creation + Explain Stats (<code>explain("executionStats")</code>) <br/>
✔ Drop Index + Verify Index List <br/>
✔ Drop Collection (<code>db.courses.drop()</code>) <br/>
</p>

---

<h3 align="center">📂 Exported Sample Dataset (MongoDB Compass JSON)</h3>

<p align="center">
This project includes a <b>real MongoDB Compass exported JSON dataset</b> that anyone can import and use to reproduce the queries, sorting, filtering, updates, deletes, and indexing demos.
</p>

<p align="center">
👉 <b>Click the button below to download/view the dataset</b>
</p>

<p align="center">
<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/school.students.json" target="_blank">
  <img src="https://img.shields.io/badge/View%20MongoDB%20Exported%20JSON%20Dataset-Click%20Here-2EA44F?style=for-the-badge&logo=mongodb&logoColor=white"/>
</a>
</p>

<p align="center">
<b>📌 Dataset Includes:</b><br/>
✔ ObjectId fields (<code>$oid</code>)<br/>
✔ Nested objects (<code>address</code>)<br/>
✔ Arrays (<code>courses</code>)<br/>
✔ Date fields (<code>$date</code>)<br/>
✔ Null handling (<code>gradutionDate</code>)<br/>
</p>

---

<h3 align="center">🛠️ Tech Stack Used</h3>

<p align="left">
🔹 MongoDB Community Edition <br/>
🔹 MongoDB Shell (mongosh) <br/>
🔹 MongoDB Compass (GUI) <br/>
🔹 VS Code Terminal <br/>
🔹 JSON Dataset Export (Compass) <br/>
</p>

---

<h3 align="center">🧩 MongoDB Features Utilized</h3>

<p align="left">
🔹 Collections & Documents <br/>
🔹 BSON Data Types <br/>
🔹 Projection Queries <br/>
🔹 Sorting & Limiting <br/>
🔹 Comparison Operators <br/>
🔹 Logical Operators <br/>
🔹 Update Operators (<code>$set</code>, <code>$unset</code>, <code>$exists</code>) <br/>
🔹 Capped Collections <br/>
🔹 Indexing (<code>createIndex</code>, <code>getIndexes</code>, <code>dropIndex</code>) <br/>
🔹 Query Performance Validation (<code>explain("executionStats")</code>) <br/>
</p>

---

<h3 align="center">🛠️ Challenges Faced & Solutions</h3>

<div align="center">

| Challenge Faced | Solution Implemented |
|----------------|---------------------|
| MongoDB database not showing after creation | Understood MongoDB behavior: DB appears only after inserting data |
| mongosh not recognized in terminal | Added mongosh path to Windows Environment Variables |
| Slow query scan (COLLSCAN) | Created index and validated improvement using explain executionStats |
| Risk of losing data while deleting documents | Exported collection from Compass before delete operations |
| Confusion between collection drop vs database drop | Practiced both: db.collection.drop() and db.dropDatabase() |

</div>

---

<h3 align="center">📂 Project Structure Overview</h3>

<p align="left">
📁 <code>PDF_Documentation/</code> – Step-by-step learning + execution PDFs <br/>
📁 <code>Dataset/</code> – Exported MongoDB Compass JSON file <br/>
📁 <code>Gif_Demo/</code> – 5-second MongoDB definition + key features GIF <br/>
📄 <code>README.md</code> – Recruiter-friendly documentation <br/>
</p>

---

<h3 align="center">▶️ Execution Demo & 📄 Documentation</h3>

<table align="center">
<tr>

<td align="center" width="50%">

<b>[DaVinci Resolve] - 🎬 MongoDB Features (GIF)</b><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/DefKeyFeatures.gif" width="100%"/>

</td>

<td align="left" width="50%">

<b>📘 Step-by-Step MongoDB Documentation (11 PDFs)</b><br/><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/01_Installating%20MongoDB%20and%20Start%20Using%20VS%20Code%20or%20mongosh.exe.pdf" target="_blank">
  <img src="https://img.shields.io/badge/01%20-%20Install%20MongoDB%20%26%20Start%20Using%20mongosh-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/02_Database%2C%20Collection%2C%20and%20Documents%20in%20MongoDB%20using%20VS%20Code%20Terminal%20and%20MongoDB%20Compass.pdf" target="_blank">
  <img src="https://img.shields.io/badge/02%20-%20Database%2C%20Collection%20%26%20Documents-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/03_Data%20Types.pdf" target="_blank">
  <img src="https://img.shields.io/badge/03%20-%20MongoDB%20Data%20Types-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/04_Sorting%20and%20Limiting.pdf" target="_blank">
  <img src="https://img.shields.io/badge/04%20-%20Sorting%20%26%20Limiting-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/05_Find(%7Bquery%7D%2C%20%7BProjection%7D)%20Method%20in%20MongoDB.pdf" target="_blank">
  <img src="https://img.shields.io/badge/05%20-%20Find(Query%2C%20Projection)-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/06_Update%20Method%20in%20MongoDB.pdf" target="_blank">
  <img src="https://img.shields.io/badge/06%20-%20Update%20Method-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/07_Delete%20Method%20in%20MongoDB.pdf" target="_blank">
  <img src="https://img.shields.io/badge/07%20-%20Delete%20Method-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/08_Comparison%20Query%20Parameter.pdf" target="_blank">
  <img src="https://img.shields.io/badge/08%20-%20Comparison%20Query%20Operators-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/09_Logical%20Operators%20in%20MongoDB.pdf" target="_blank">
  <img src="https://img.shields.io/badge/09%20-%20Logical%20Operators-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/10_Indexes%20in%20MongoDB.pdf" target="_blank">
  <img src="https://img.shields.io/badge/10%20-%20Indexes%20in%20MongoDB-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a><br/>

<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2026/02_Feb/01_%5BMongoDB%5D-%20Query%20Lab%20%E2%80%93%20CRUD%2C%20Indexing%2C%20and%20Collection%20Management/Documents%20%26%20Gif/11_Collections%20in%20MongoDB.pdf" target="_blank">
  <img src="https://img.shields.io/badge/11%20-%20Collections%20in%20MongoDB-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a>

</td>

</tr>
</table>

---

<h3 align="center">🧠 Key Learnings for SDET / Backend Role</h3>

<p align="left">
✔ Strong understanding of MongoDB fundamentals used in real applications <br/>
✔ Ability to write production-style queries with filters, projection, sorting and limits <br/>
✔ Practical experience with MongoDB Compass and mongosh workflows <br/>
✔ Indexing knowledge to optimize database queries and reduce scan time <br/>
✔ Data modeling basics: nested objects, arrays, null values, and date types <br/>
</p>

---

<h3 align="center">🔗 Proof of Work — Support & Connect</h3>

<p align="center">
<strong>If this project added value to you, please support by <b>liking</b>, <b>commenting (rating ⭐ out of 5)</b>, and <b>sharing</b> the LinkedIn post below 🚀</strong>
</p>

<p align="center">
  <a href="https://www.linkedin.com/posts/routhkiranbabu_im-happy-to-share-this-mongodb-query-ugcPost-7425048750131326977-r-Vl?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC0fSW0BCXvPinW6E3cbBZFekfnprC0b-FU" target="_blank">
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
Aspiring SDET | MongoDB + Automation Enthusiast
</p>

<p align="center">
⭐ If this repository helped you, don't forget to star it!
</p>

