// Run this server using -> npm run server1
// To stop -> ctrl + c -> y/Y
// Import the express library
const express = require("express")
const app = express()

app.get("/", (req, res) => {
    // Providing json response having {error: "You got 300"}
    // To see the actual status: ctrl + shift + i -> console
    res.status(300).json({error: "You got 300"})
    console.log("In the base page...")
})

// Setup port 3000
app.listen(3000)