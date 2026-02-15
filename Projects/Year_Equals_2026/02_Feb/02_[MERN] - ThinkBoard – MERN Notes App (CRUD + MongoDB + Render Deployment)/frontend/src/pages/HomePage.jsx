import { useEffect } from 'react'
import { useState } from 'react';
import Navbar from '../components/Navbar'
import RateLimitedUI from '../components/RateLimitedUI';
import toast from "react-hot-toast";
import NoteCard from "../components/NoteCard"
import NotesNotFound from '../components/NotesNotFound';
import api from "../lib/axios"

const HomePage = () => {
  const [isRateLimited, setIsRateLimited] = useState(false);
  // fetching the notes
  const [notes, setNotes] = useState([])
  // to keep track of loading state, set to true, soon
  // as we load the page, we need to fetch the notes
  const [loading, setLoading] = useState(true)
  // To able to fetch that
  useEffect(() => {
    const fetchNotes = async () => {
      try {
        // For get method
        // const res = await axios.get("http://localhost:5001/api/notes")
        // For post method
        // const res = await axios.post("http://localhost:5001/api/notes")
        const res = await api.get("/notes")
        // const data = await res.json()
        // Which is lot more comfortable then fetch API
        console.log(res.data)// instead of console logging the data 
        // We want to update the notes state
        setNotes(res.data)
        // If we can get the data, ratelimited to false
        setIsRateLimited(false)
      } catch (erro) { 
        console.log("Error fetching notes")
        console.log(erro.response)
        // We want to check for the state in:
        // const [isRateLimited, setIsRateLimited] = useState(false);
        // 429 for rateLimited
        if(erro.response?.status === 429){
          setIsRateLimited(true)
        }else{
          toast.error("Failed to load Notes")
        }
      } finally{
        setLoading(false)
      }
    }

    fetchNotes()
  }, [])
  return (
    // min-h-screen = minimum height will be screen
    // takes entire screen
    <div className="min-h-screen">
      {/* First it will have navbar component */}
      <Navbar />
      {isRateLimited && <RateLimitedUI />}

      <div className="max-w-7xl mx-auto p-4 mt-6">
          {loading && <div className="text-center text-primary py-10">Loading notes...</div>}
          
          {notes.length === 0 && !isRateLimited && <NotesNotFound />}
          
          {notes.length > 0 && !isRateLimited && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {notes.map(note => (
                <NoteCard key={note._id} note={note} setNotes={setNotes} />
              ))}
            </div>
          )}
      </div>
    </div>
  );
};

export default HomePage;
