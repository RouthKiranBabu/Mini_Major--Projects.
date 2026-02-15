import mongoose from "mongoose"

// Creating a function that connects to the database
// Export to use it in server.js
export const connectDB = async () => {
    try {
        // connect by string we got earlier from MongoDB
        //"mongodb+srv://routhfamily123_db_user:dRoCEmJAW@cluster0.dxejp0q.mongodb.net/notes_db?appName=Cluster0"
        await mongoose.connect(process.env.MONGO_URI)
        console.log("MongoDB connected Successfully...")
    } catch (error) {
        console.log("Error connecting to MongoDB:", error)
        // 1 = exit with failure, if there's an error
        process.exit(1) // 0 = success
    }

}
