# To install cypress:
```bash
npm -i init
npm install cypress --save -dev
npx cypress open
```

# To run spec file:
```bash
npx cypress run --spec "cypress/e2e/Spec_File.cy.js" --browser chrome --headed
```

# To save the result as video:
```
    Add the below three line into cypress.config.js:
        video: true,
        videoCompression: 32,
        videoUploadOnPasses: true,
```

# To run in headless mode(without test visual):
```bash
    Add the below line into cypress.config.js:
        specPattern: "cypress/e2e/Spec_File.cy.{js,ts,jsx,tsx}"
    then start executing using: npx cypress run
    instead of typing ["npx cypress run --spec "cypress/e2e/Spec_File.cy.js" --browser chrome --headed"] - which is too lengthy
```

# To use xpath:
```bash
    In terminal: npm install cypress-xpath
    command.js(at last line): ///<reference types="cypress"/>
    e2e.js(at last line): require("cypress-xpath")
    Then use: cy.xpath(...)

```
