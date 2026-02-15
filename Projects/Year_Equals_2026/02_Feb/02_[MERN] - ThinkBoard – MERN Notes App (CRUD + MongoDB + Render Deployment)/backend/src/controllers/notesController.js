import Note from "../models/Note.js"

export async function getAllNotes(req, res) {
    try {
        // Note.find(), to get every single note
        // sort({createdAt: -1}) <= newest first
        // by default createdAt: 1
        const notes = await Note.find().sort({createdAt: -1})
        // Send status, send notes as json
        res.status(200).json(notes)
    } catch (error) {
        // For debugging purpose
        console.error("Error in getAllNotes controller", error)
        res.status(500).json({message: "Internal Server Error"})
    }
}

export async function getNoteById(req, res) {
    try {
        const note = await Note.findById(req.params.id)
        if(!note) return res.status(404).json({message: "Note not Found!"})
        res.json(note)
    } catch (error) {
        console.error("Error in getNoteById controller", error)
        res.status(500).json({message: "Internal Server Error"})
    }
}

export async function createNote(req, res) {
    // If user want to create a notes:
    // includes title, content
    try {
        // title and content comes from req.body
        const {title, content} = req.body
        // by default we can't access this value
        // To access them(or console it),
        // Go to server.js, just before the routes
        // add the code -> app.use(express.json())
        // which is a middleware that we add
        // console.log(title, content)

        // const newNote = new Note({title:title, content: content})
        // Since key and value are the same, so the above code can
        // be replaced as
        // const newNote = new Note({title, content})
        // await newNote.save()

        // const newNote = new Note({title, content})
        // await newNote.save()
        // res.status(201).json({message: "Note Created successfully!"})
        
        const note = new Note({title, content})
        const savedNote = await note.save()
        res.status(201).json(savedNote)
        
    } catch (error) {
        console.error("Error in createNote controller", error)
        res.status(500).json({message: "Internal Server Error"})
    }
}

export async function updateNote(req, res) {
    try {
        const {title, content} = req.body
        // How do we know id that user sends, so that we can update
        // based on id
        // {title, content} <- things to update
        // {new: true} <- to get fields
        const updatedNote = await Note.findByIdAndUpdate(req.params.id, {title, content}, {new: true})
        // For false value, 404=not found, 
        if(!updatedNote) return res.status(404).json({message: "Note not found!"})
        // res.status(200).json({message: "Note updated successfully."})
        res.status(200).json(updatedNote)

    } catch (error) {
        console.error("Error in updateNote controller", error)
        res.status(500).json({message: "Internal Server Error"})
    }
}

export async function deleteNote(req, res) {
    try {
        const deletedNote = await Note.findByIdAndDelete(req.params.id)
        if (!deleteNote) return res.status(404).json({message: "Note not found!"})
        res.status(200).json({message: "Note deleted successfully!"})
    } catch (error) {
        console.error("Error in deleteNote controller", error)
        res.status(500).json({message: "Internal Server Error"})
    }
}
