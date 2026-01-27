const express = require("express")
const router = express.Router()

// Made a function that prints url in terminal
function logger(req, res, next){
    console.log(req.originalUrl)
    // Lets move to the next phase
    next()
}
// Router start using logger
router.use(logger)

// Sending name and url to the ejs file called logsejs
router.get("/:userID", (req, res, next) => {
    res.render("logsejs", {user: req.user.name, userurl: req.originalUrl})
    next()
})

const users = [{name: "kiran"}, {name: "routh"}]
// Lets choosing the user when userID is provided
router.param("userID", (req, res, next, userID) => {
    req.user = users[userID]
    next()  
})

// Exporting the router to the server
module.exports = router