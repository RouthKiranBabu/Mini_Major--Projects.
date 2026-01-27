// Run this server using -> npm run server1
// Import the express library
const express = require("express")
const app = express()

// To view the html page as ejs
app.set("view engine", "ejs")

app.get("/", (req, res) => {
    // Choosing index.ejs in views folder
    res.render("index", {rendertext:"render text"})
    console.log("ejs started...")
})

app.listen(3000)