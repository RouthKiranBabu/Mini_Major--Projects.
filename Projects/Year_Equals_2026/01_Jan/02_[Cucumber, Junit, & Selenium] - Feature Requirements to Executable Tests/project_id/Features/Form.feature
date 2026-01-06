Feature: Form

Scenario: Single User Fills the Form
Given Maximized Chrome Browser
And URL is "https://v1.training-support.net/selenium/simple-form"
Then Check Title is "Simple Form"
And Check URL is "https://v1.training-support.net/selenium/simple-form"
And Enter first name as "Routh"
And Enter last name as "Kiran Babu"
And Enter email as "routhfamily123@gmail.com"
And Enter contact number as "1234322343"
And Enter message as "Good Form!"
# There are two button, "submit" to show alert, "clear" to clears the data entered
And Click button named "cleaR"
Then Check alert text as "Thank You for reaching out to us, Routh Kiran Babu"
And Click button named OK
And Wait "3" seconds then close browser 

#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
#@tag
#Feature: Title of your feature
  #I want to use this template for my feature file
#
  #@tag1
  #Scenario: Title of your scenario
    #Given I want to write a step with precondition
    #And some other precondition
    #When I complete action
    #And some other action
    #And yet another action
    #Then I validate the outcomes
    #And check more outcomes
#
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |
