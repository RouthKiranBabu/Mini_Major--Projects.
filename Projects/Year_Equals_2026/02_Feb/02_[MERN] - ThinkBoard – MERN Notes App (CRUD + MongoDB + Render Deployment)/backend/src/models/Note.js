import mongoose from "mongoose";

// 1st step: you need to create the schema
// 2nd step: you would create a model based off that schema

const noteSchema = new mongoose.Schema({
        title: {
            type:String,
            required: true
        },
        content: {
            type:String,
            required: true
        },
    },
    // for createdAt, updatedAt
    {timestamps: true}
)

// Create a Model based on the schema
// N is capital
const Note = mongoose.model("Note", noteSchema)

export default Note