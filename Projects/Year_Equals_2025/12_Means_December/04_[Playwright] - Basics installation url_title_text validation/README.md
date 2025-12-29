## 📚 Table of Contents
<details>
<summary><strong>Click to expand</strong></summary>

- 🎭 [Project Title](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation#-playwright-automation--title-url--text-validation)
- ⚡ One-Line Project Summary  
- 🎯 Aim / Objective  
- 🔥 [Real-World Problem Statement](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation#-real-world-problem-statement)  
- 🧠 Core Concept Demonstrated – Playwright Test Lifecycle  
- 🧪 Test Scenarios Covered  
- 📂 [Actual Automation Code (With Comments)](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation#-actual-automation-code-with-comments)  
- 🧰 Tech Stack Used  
- 🧩 Playwright Features Utilized  
- 🛠️ [Challenges Faced & Solutions](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation#%EF%B8%8F-challenges-faced--solutions)  
- 📂 Project Structure Overview  
- ▶️ [Execution Demo & Documentation](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation#%EF%B8%8F-execution-demo---documentation)  
- 🧠 Key Learnings for SDET Role  
- 🔗 [Proof of Work — Support & Connect](https://github.com/RouthKiranBabu/Mini_Major--Projects./tree/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation#-proof-of-work--support--connect)  
- 👨‍💻 Author  

</details>

---

<h1 align="center">🎭 Playwright Automation – Title, URL & Text Validation</h1>

<h3 align="center">
Real-World Playwright Test Automation Using Hooks, Assertions & Debug Mode
</h3>

---

<h3 align="center">📌 One-Line Project Summary</h3>

<p align="center">
A real-world Playwright automation mini project validating application title, URL, and UI text using
Playwright Test lifecycle hooks and TDD-style assertions.
</p>

---

<h3 align="center">🎯 Aim / Objective</h3>

<p align="center">
To demonstrate modern UI automation using <b>Playwright Test</b> by validating critical application attributes
with <code>beforeEach</code>, <code>afterEach</code>, and Playwright’s built-in <code>expect</code> assertions.
</p>

---

<h3 align="center">🔥 Real-World Problem Statement</h3>

<p align="center">
Modern applications demand fast, reliable, and flake-free automation.
This project demonstrates how Playwright ensures clean browser lifecycle handling,
precise UI validations, and powerful debugging — core expectations for SDET roles.
</p>

---

<h3 align="center">🧠 Core Concept Demonstrated – Playwright Test Lifecycle</h3>

<p align="center"><b>This project clearly demonstrates:</b></p>

<p align="left">
🔹 Browser & page setup using <code>test.beforeEach()</code> <br/>
🔹 Clean teardown using <code>test.afterEach()</code> <br/>
🔹 Page navigation using Playwright API <br/>
🔹 UI validation using Playwright <code>expect</code> <br/>
🔹 Debug-friendly automation execution <br/>
</p>

<p align="center">
<b>✅ Fast execution<br/>
✅ Clean lifecycle handling<br/>
✅ Modern SDET-ready automation</b>
</p>

---

<h3 align="center">🧪 Test Scenarios Covered</h3>

<p align="left">
✔ Validate Application Title using <code>page.title()</code> <br/>
✔ Validate Application URL using <code>page.url()</code> <br/>
✔ Validate Login Page Heading Text (<code>&lt;h5&gt;</code>) <br/>
✔ Lifecycle handling using <code>beforeEach</code> & <code>afterEach</code> <br/>
✔ Assertions using Playwright <code>expect()</code> <br/>
</p>

---

<h3 align="center">📂 Actual Automation Code (With Comments)</h3>

<p align="center">
This section provides direct access to the <b>actual Playwright test implementation</b>,
with <b>clear inline comments</b> explaining hooks, assertions, and validations.
</p>

<p align="center">
👉 <b>Click the button below to view the source code</b>
</p>

<p align="center">
<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation/tests/spec_file.spec.js" target="_blank">
  <img src="https://img.shields.io/badge/View%20Actual%20Playwright%20Code-Click%20Here-2EA44F?style=for-the-badge&logo=github&logoColor=white"/>
</a>
</p>

<p align="center">
<b>🔍 What reviewers will find inside:</b><br/>
✔ Playwright test hooks in action<br/>
✔ Title, URL & Text validations<br/>
✔ Clean & readable test structure<br/>
✔ Debug-friendly automation code
</p>

---

<h3 align="center">🛠️ Tech Stack Used</h3>

<p align="left">
🔹 JavaScript (Node.js) <br/>
🔹 Playwright Test <br/>
🔹 VS Code <br/>
🔹 Chromium / Firefox / WebKit <br/>
</p>

---

<h3 align="center">🧩 Playwright Features Utilized</h3>

<p align="left">
🔹 Playwright Test Runner <br/>
🔹 Test Hooks (<code>beforeEach</code>, <code>afterEach</code>) <br/>
🔹 Built-in Assertions (<code>expect</code>) <br/>
🔹 Locator Strategy (<code>locator()</code>) <br/>
🔹 Debug Mode Execution <br/>
</p>

---

<h3 align="center">🛠️ Challenges Faced & Solutions</h3>

<div align="center">

| Challenge Faced | Solution Implemented |
|----------------|---------------------|
| Repeated navigation logic | Centralized using `beforeEach` |
| Cleanup after test execution | Handled using `afterEach` |
| Debugging test failures | Used Playwright `--debug` mode |
| UI text validation | Implemented Playwright locators |

</div>

---

<h3 align="center">📂 Project Structure Overview</h3>

<p align="left">
📁 <code>tests/</code> – Playwright test specs <br/>
📁 <code>Documents and Gifs/</code> – Execution proof & documentation <br/>
📄 <code>playwright.config.js</code> – Playwright configuration <br/>
</p>

---

<h3 align="center">▶️ Execution Demo & 📄 Documentation</h3>

<table align="center">
<tr>
<td align="center" width="50%">

<b>🎬 Playwright Installation Demo</b><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation/Document%20and%20Gifs/Formula%20To%20Remember.gif" width="100%"/>

</td>

<td align="center" width="50%">

<b>🐞 Playwright Debug Mode Demo</b><br/><br/>
<img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation/Document%20and%20Gifs/How%20to%20Execute%20Gif.gif" width="100%"/>

</td>
</tr>
</table>

<br/>

<p align="center">
<b>📘 Step-by-Step Installation & Setup Guide</b><br/><br/>
<a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2025/12_Means_December/04_%5BPlaywright%5D%20-%20Basics%20installation%20url_title_text%20validation/Document%20and%20Gifs/%F0%9F%8E%AF%20Playwright%20Automation.pdf" target="_blank">
  <img src="https://img.shields.io/badge/View%20PDF-Documentation-red?style=for-the-badge&logo=adobeacrobatreader"/>
</a>
</p>

---

<h3 align="center">🧠 Key Learnings for SDET Role</h3>

<p align="left">
✔ Understanding Playwright fundamentals <br/>
✔ Modern test lifecycle management <br/>
✔ Reliable UI validations using Playwright <br/>
✔ Debugging automation efficiently <br/>
</p>

---

<h3 align="center">🔗 Proof of Work — Support & Connect</h3>

<p align="center">
<strong>If this project added value to you, please support by <b>liking</b>, <b>commenting (rating ⭐ out of 5)</b>, and <b>sharing</b> the LinkedIn post below 🚀</strong>
</p>

<p align="center">
  <a href="https://www.linkedin.com/posts/routhkiranbabu_im-happy-to-share-this-playwright-title-activity-7411398173933572096-QScN?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC0fSW0BCXvPinW6E3cbBZFekfnprC0b-FU" target="_blank">
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
Aspiring SDET | Playwright & Automation Testing Enthusiast
</p>

<p align="center">
⭐ If this repository helped you, don't forget to star it!
</p>
