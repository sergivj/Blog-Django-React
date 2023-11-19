import axios from "axios";
import {Navigate, useSearchParams} from "react-router-dom";
import {useState} from "react";

export const Register = () => {
    const [username, setUsername] = useState('');
    const [first_name, setName] = useState('');
    const [last_name, setLastname] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const submit = async e => {
        e.preventDefault();
        const user = {
            username: username,
            first_name: first_name,
            last_name: last_name,
            email: email,
            password: password
        };

        const {register} = await axios.post('http://localhost:8000/register/register-user/', user ,{headers: {
            'Content-Type': 'application/json'
        }}, {withCredentials: true});

        window.location.href = '/login';
    }

    return(
        <div className="Auth-form-container">
            <form className="Auth-form" onSubmit={submit}>
              <div className="Auth-form-content">
                <h3 className="Auth-form-title">Sign Up!</h3>
                <div className="form-group mt-3">
                  <label>Username</label>
                  <input
                    className="form-control mt-1"
                    placeholder="Enter Username"
                    name='username'
                    type='text'
                    value={username}
                    required
                    onChange={e => setUsername(e.target.value)}
                  />
                </div>
                <div className="form-group mt-3">
                  <label>Name</label>
                  <input
                    className="form-control mt-1"
                    placeholder="Enter First Name"
                    name='first_name'
                    type='text'
                    value={first_name}
                    required
                    onChange={e => setName(e.target.value)}
                  />
                </div>
                <div className="form-group mt-3">
                  <label>Last name</label>
                  <input
                    className="form-control mt-1"
                    placeholder="Enter Lastname"
                    name='last_name'
                    type='text'
                    value={last_name}
                    required
                    onChange={e => setLastname(e.target.value)}
                  />
                </div>
                <div className="form-group mt-3">
                  <label>Email</label>
                  <input
                    className="form-control mt-1"
                    placeholder="Enter Email"
                    name='email'
                    type='email'
                    value={email}
                    required
                    onChange={e => setEmail(e.target.value)}
                  />
                </div>
                <div className="form-group mt-3">
                  <label>Password</label>
                  <input
                    name='password'
                    type="password"
                    className="form-control mt-1"
                    placeholder="Enter password"
                    value={password}
                    required
                    onChange={e => setPassword(e.target.value)}
                  />
                </div>
                <div className="d-grid gap-2 mt-3">
                  <button type="submit" className="btn btn-primary">
                    Submit
                  </button>
                </div>
              </div>
            </form>
        </div>
    );
}
