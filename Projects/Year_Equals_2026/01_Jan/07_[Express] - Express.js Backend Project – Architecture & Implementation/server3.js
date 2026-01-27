// Run this server using -> npm run server1
// Import the express library
const express = require("express")
const app = express()
app.set("view engine", "ejs")

// Created a users router to stay organized
// where all the users operations taken into one place
// Available in routes folder then users.js
const userrouter = require("./routes/users")
// Choosen path for this router as /users
app.use("/users", userrouter)

app.listen(3000)