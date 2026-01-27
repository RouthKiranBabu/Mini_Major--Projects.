const express = require("express")
const app = express()
app.set("view engine", "ejs")

// Using public folder to show the static(does not having variable to change) html file
// use http://localhost:3000/ for index.html
// use http://localhost:3000/test/within_test.html for within_test.html
app.use(express.static("public"))

app.listen(3000)