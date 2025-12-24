describe('template spec', () => {
  // Executes before each it block
  beforeEach(() => {
    // Visits to URL
    cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
  });
  // Executes after each it block
  afterEach(() => {
    // Wait for 4 seconds after it block
    cy.wait(4000)
  });
  it('Validate Title', () => {
    // Calling the title method
    cy.title().then(($tle) => {
      // Get title element
      const tle = $tle
      cy.log(`Title is ${tle}.`)
      // BDD(Behavior Driven Development): human readable. Examples describe(), it(), should(), before(), beforeEach(), after(), afterEach()
      expect(tle).to.equal("OrangeHRM")
      expect(tle == "OrangeHRM").to.be.true
    })
  })
  it('Validate URL', () => {
    cy.url().then(($ul) => {
      const [ul, actual_ul] = [$ul, "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"] 
      // To show something in log we use cy.log
      cy.log(`URL is ${ul}.`)
      // TDD(Test Driven Development): Eg: assert.equal(), assert.notEqual(), assert.isTrue(), assert.isFalse(), assert.isNull(), assert.isNotNull(), assert.typeOf(), assert.lengthOf(), assert.include()
      assert.equal(ul, actual_ul)
      assert.notEqual(ul, actual_ul + ".")
      assert.isTrue(ul == actual_ul)
      assert.isFalse(ul != actual_ul)
    })
  });
  it('Validate Logo Text', () => {
    // Use xpath to test selected element directly in the browser
    cy.xpath("//h5").then(($txt) => {
      // Get the text
      const txt = $txt.text().trim()
      // Print the text
      cy.log(txt)
      // TDD to check the text as expected
      expect(txt == "Login").to.be.true
    })
    // BDD to check everything in one move, no need to use should multiple times use, 'and' instead
    cy.xpath("//h5").should("have.text", "Login")
    .should("contain", "Log")
    .should("include.text", "ogin")
    .and("be.visible")
  });
})