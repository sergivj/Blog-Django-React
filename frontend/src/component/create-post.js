import axios from "axios";
import {useEffect, useState} from "react";

export const CreatePost = () => {
    const [username, setUsername] = useState(0);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/home/');
                setUsername(response.data.user.id);
            }
            catch (error) {
                console.log(error);
            }
        };
        fetchData();
    }, []);

    const submit = async e => {
        e.preventDefault();
        const user = {
            title: title,
            content: content,
            author: username,
        };

        const {register} = await axios.post('http://localhost:8000/new-entry/', user ,{headers: {
            'Content-Type': 'application/json'
        }}, {withCredentials: true});

        window.location.href = '/';

    }

    return(
        <div className="Auth-form-container">
            <form className="Auth-form" onSubmit={submit}>
              <div className="Auth-form-content">
                <h3 className="Auth-form-title">Write a Post!</h3>
                <div className="form-group mt-3">
                  <label>Title</label>
                  <input
                    className="form-control mt-1"
                    placeholder=""
                    name='user'
                    type='hidden'
                    value={username}
                    required
                  />
                  <input
                    className="form-control mt-1"
                    placeholder="Enter Title"
                    name='title'
                    type='text'
                    value={title}
                    required
                    onChange={e => setTitle(e.target.value)}
                  />
                </div>
                <div className="form-group mt-3">
                  <label>Content</label>
                  <textarea
                    className="form-control mt-1"
                    placeholder="Enter Content"
                    name='first_name'
                    value={content}
                    required
                    onChange={e => setContent(e.target.value)}
                  />
                </div>
                <div className="d-grid gap-2 mt-3">
                  <button type="submit" className="btn btn-primary">
                    Create new entry
                  </button>
                </div>
              </div>
            </form>
        </div>
    );
}
