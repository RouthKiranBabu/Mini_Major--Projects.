<h1 align="center">🚀 Cypress Automation – Auto Waiting Mechanism</h1>

<p align="center">
  <b>A real-world Cypress automation project demonstrating Auto-Waiting, BDD & TDD</b> 📌
</p>

<hr/>

<h2 align="center">📌 Project Overview</h2>

<p align="center">
This project demonstrates Cypress's powerful <b>Auto Waiting Mechanism</b> using a real application  
<b>(OrangeHRM Demo Login Page)</b>.
</p>

<p align="left">
✅ Validate Page Title <br/>
✅ Validate Application URL <br/>
✅ Validate Logo / Heading Text <br/>
✅ Cypress Auto-Waiting (No explicit waits for elements) <br/>
✅ BDD & TDD Assertions <br/>
</p>

<hr/>

<h2 align="center">🧠 Key Learning – Cypress Auto Waiting</h2>

<p align="center">
Cypress automatically waits for:
</p>

<p align="left">
⏳ Page to load <br/>
⏳ DOM elements to appear <br/>
⏳ Assertions to pass <br/>
⏳ Network requests to complete <br/>
</p>

<p align="center">
<b>👉 This eliminates flaky tests and manual synchronization.</b>
</p>

<hr/>

<h2 align="center">🛠 Tech Stack</h2>

<p align="left">
🔹 Cypress <br/>
🔹 JavaScript <br/>
🔹 Mocha Test Framework <br/>
🔹 Chai Assertions (BDD & TDD) <br/>
🔹 Cypress XPath Plugin <br/>
</p>

<hr/>

<h2 align="center">📂 Test Implementation</h2>

```javascript
describe('template spec', () => {

  beforeEach(() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
  });

  afterEach(() => {
    cy.wait(4000)
  });

  it('Validate Title', () => {
    cy.title().then((tle) => {
      cy.log(`Title is ${tle}`)
      expect(tle).to.equal("OrangeHRM")
      expect(tle == "OrangeHRM").to.be.true
    })
  })

  it('Validate URL', () => {
    cy.url().then((url) => {
      const actualUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
      cy.log(`URL is ${url}`)
      assert.equal(url, actualUrl)
      assert.notEqual(url, actualUrl + ".")
      assert.isTrue(url == actualUrl)
      assert.isFalse(url != actualUrl)
    })
  });

  it('Validate Logo Text', () => {
    cy.xpath("//h5").then((txt) => {
      const text = txt.text().trim()
      cy.log(text)
      expect(text == "Login").to.be.true
    })

    cy.xpath("//h5")
      .should("have.text", "Login")
      .and("contain", "Log")
      .and("include.text", "ogin")
      .and("be.visible")
  });

})
```

<hr/> <h2 align="center">🎥 Demo & 📄 Documentation</h2> <div align="center"> <table> <tr> <td align="center"> <b>🎬 Cypress Execution Demo</b><br/><br/> <a href="assets/demo.gif" target="_blank"> <img src="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2025/12_Means_December/02_Cypress%20Automation%20-%20To%20check%20Expected%20Title%2C%20URL%20and%20Logo%20Text__And%20Commonly%20used%20TDD%20and%20BDD%20styles/Document%20And%20Gif/Cypress_Fetures_AutoWaiting_Assertions.gif" width="400"/> </a> </td> <td align="center"> <b>📄 Project Documentation</b><br/><br/> <a href="https://github.com/RouthKiranBabu/Mini_Major--Projects./blob/main/Projects/Year_Equals_2025/12_Means_December/02_Cypress%20Automation%20-%20To%20check%20Expected%20Title%2C%20URL%20and%20Logo%20Text__And%20Commonly%20used%20TDD%20and%20BDD%20styles/Document%20And%20Gif/Cypress%20End-to-End%20Automation%20Project.pdf" target="_blank"> <img src="https://img.shields.io/badge/View%20PDF-Documentation-red?style=for-the-badge&logo=adobeacrobatreader"/> </a> </td> </tr> </table> </div> <hr/> 

<h2 align="center">📢 Support & Connect</h2> <p align="center"> If you find this project useful, please consider supporting 🙌 </p> <div align="center"> <a href="https://www.linkedin.com/posts/routhkiranbabu_im-happy-to-share-this-cypress-automation-activity-7409872664175247360-9lff?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC0fSW0BCXvPinW6E3cbBZFekfnprC0b-FU" target="_blank"> <img src="https://img.shields.io/badge/Like%20%7C%20Comment%20%7C%20Share-LinkedIn-blue?style=for-the-badge&logo=linkedin"/> </a> </div> <hr/> <h3 align="center">👨‍💻 Author</h3> <p align="center"> <b>Routh Kiran Babu</b><br/> Aspiring SDET | Cypress Automation Enthusiast </p> <p align="center"> ⭐ If this repository helped you, don't forget to star it! </p> 
