const express = require("express")
const app = express()
app.set("view engine", "ejs")

const loggers = require("./routes/loggersjs")
app.use("/logs", loggers)

app.listen(3000)