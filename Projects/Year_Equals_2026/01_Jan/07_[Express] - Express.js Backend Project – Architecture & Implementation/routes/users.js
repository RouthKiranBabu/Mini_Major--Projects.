const express = require("express")
const router = express.Router()

router.get("/", (req, res) => {
    res.send("Users Base")
    console.log("In the base...")
})

router.get("/new", (req, res) => {
    res.send("New form fillup")
    console.log("In the new fillup...")
})

router.route("/new/:userID")
.get((req, res) => {
    // res.send(`ID: ${req.params.userID}. User: ${req.user.name}`)
    res.render("index", {rendertext: req.user.name, id: req.params.userID})
})
.post((req, res) => {

})
.delete((req, res) => {

})

let users = [{name: "kiran"}, {name: "routh"}]
router.param("userID", (req, res, next, userID) => {
    req.user = users[userID]
    next()
})

// router.get("/new/:userID", (req, res) => {
//     res.send(`User id is ${req.params.userID}.`)
//     console.log("In users id...")
// })

module.exports = router