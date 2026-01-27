const express = require("express")
// Initializing the router
const router = express.Router()
// Initial values of variables
const users = []
let _id = 0
let getfn = (users.length - 1 <= 0)? "Enter user" : users[users.length - 1].name
let getgn = (users.length - 1 <= 0)? "Enter gender" : users[users.length - 1].gender

// http://localhost:3000/users <- shows initial-> Number of Users: 0. Users => {}. Gender(undefined): {}.
router.get("/", (req, res) => {
    // Variable that saves all the users
    let userstr = ""
    for (let i = 0; i < users.length; i++){
        userstr += `[ID: ${users[i].id}, Name: ${users[i].name}, Gender: ${users[i].gender}], `
    }
    // Gettng query like gender=male or female
    // eg: choose for male: http://localhost:3000/users?gender=male
    // eg: choose for female: http://localhost:3000/users?gender=female
    let _gend = req.query.gender
    // To store genders in variable
    let genderstr = ""
    for (let i = 0; i < users.length; i++){
        if (_gend === users[i].gender){
            genderstr += `[ID: ${users[i].id}, Name: ${users[i].name}], `
        }
    }
    // Shows in the users
    res.send(`Number of Users: ${users.length}. Users => {${userstr}}. Gender(${_gend}): {${genderstr}}.`)

    // users.push({name: req.body.firstName})
    // console.log(`First name: ${req.body.firstName}.`)
    // res.redirect(`/users/${users.length - 1}`)
    console.log(users.length)
})

// To add users -> http://localhost:3000/users/new
// provide name, choose gender, submit
// Which redirect you to corresponding url Example -> http://localhost:3000/users/new/0
router.get("/new", (req, res) => {
    getfn = (users.length - 1 < 0)? "Enter user" : users[users.length - 1].name
    res.render("users/new", {userID: _id, firstName: getfn})
})
// Use post method to render the showName ejs file
router.post("/new/:userID", (req, res) => {
    getfn = (users.length - 1 < 0)? "Enter user" : users[users.length - 1].name
    getgn = (users.length - 1 < 0)? "Enter user" : users[users.length - 1].gender
    res.render("users/showName", {userID: _id, userName: getfn, userGender: getgn})
})
// Adding users to the users list
router.param("userID", (req, res, next, userID) => {
    let name = (users.length == 0) ? "Empty User": users[users.length - 1].name
    console.log("Before:", users)
    users.push({id: _id, name: req.body.firstName, gender: req.body.Gender})
    _id += 1
    console.log("After:", users)
    next()
})

module.exports = router 