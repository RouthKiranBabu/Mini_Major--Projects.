const express = require("express")
const app = express()
app.set("view engine", "ejs")
// URL can extend
app.use(express.urlencoded({extended: true}))

const router = require("./routes/server6users")
app.use("/users", router)

app.listen(3000)