import {useState} from 'react'
import {Link, useNavigate} from "react-router"
import { ArrowLeftIcon } from "lucide-react";
import toast from "react-hot-toast"
import api from "../lib/axios"

const CreatePage = () => {
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  // After submission, it set to true
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()
  // Called after submitting the form
  // async to use await
  const handleSubmit = async (e) => {
    e.preventDefault()
    // console.log(title)
    // console.log(content)

    // If title or content are not provided, even for empty value(use .trim())
    if (!title.trim() || !content.trim()){
      toast.error("All fields are Required")
      return
    }

    setLoading(true)
    try {
      // Send body {title, content}
      // await axios.post("http://localhost:5001/api/notes", {title, content})
      await api.post("/notes", {title, content})
      toast.success("Note Created Successfully!")
      navigate("/")
    } catch (error) {
      console.log("Error creating note:", error)
      // toast.error("Failed to Create Note")
      // 429 for rate limiting
      // 4000 milli Sec = 4 Sec
      if(error.response.status === 429){
        toast.error("Slow down! You're Creating Notes too fast", {
          duration: 4000,
          icon: "☠️"
        })
      }else{
        toast.error("Failed to Create Note")
      }
    } finally{
      setLoading(false)
    }
  }

  return <div className="min-h-screen bg-base-200">
    <div className="container mx-auto px-4 py-8">
      <div className="max-w-2xl mx-auto">
        <Link to={"/"} className="btn btn-ghost mb-6">
          <ArrowLeftIcon className="size-5" />
          Back to Notes
        </Link>

        <div className='card bg-base-100'>
          <div className='card-body'>
            <h2 className='card-title text-2xl mb-4'>Create New Note</h2>
            <form onSubmit={handleSubmit}>
              <div className='form-control mb-4'>
                <label className='label'>
                  <span className='label-text'>Title</span>
                </label>
                <input type="text"
                  placeholder='Note Title'
                  className="input input-bordered"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                />
              </div>

              <div className='form-control mb-4'>
                <label className='label'>
                  <span className='label-text'>Content</span>
                </label>
                <textarea 
                  placeholder='Write your notes here...'
                  className='textarea textarea-bordered h-32'
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                />
              </div>

              {/* justify-end <- to make the button available at right side 
              disabled at loading state*/}
              <div className='card-actions justify-end'>
                <button type="submit" className='btn btn-primary' disabled={loading}>
                  {loading? "Creating...": "Create Note"}
                </button>
              </div>
            </form>
          </div>

        </div>
      </div>
    </div>
  </div>
}

export default CreatePage
