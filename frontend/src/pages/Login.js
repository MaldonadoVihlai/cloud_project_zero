import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {Link} from 'react-router-dom'

const API = process.env.REACT_APP_API;

const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const res = await fetch(`${API}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email,
                password,
            }),
        })
        const response = await res.json();
        console.log(res.ok)
        localStorage.setItem('token', response.access_token)
        localStorage.setItem('id', response.id)
        if (!res.ok) {
            alert("Usuario o contraseña incorrectas")
        } else {
            navigate("/events");
        }


    };

    return (
        <div className="row center">
            <div className="col-md-4">
                <h2>Login</h2>
                <form onSubmit={handleSubmit} className="card card-body">
                    <div className="form-group">
                        <label>
                            Email:
                            <input
                                type="email"
                                onChange={(e) => setEmail(e.target.value)}
                                value={email}
                                className="form-control"
                                placeholder="User's Email"
                            />
                        </label>
                    </div>
                    <div className="form-group">
                        <label>
                            Password:
                            <input
                                type="password"
                                onChange={(e) => setPassword(e.target.value)}
                                value={password}
                                className="form-control"
                                placeholder="User's Password"
                            />
                        </label>
                    </div>
                    <button className="btn btn-primary btn-block">
                        Log In
                    </button>
                    <br/>
                    ¿No tienes una cuenta creada?, regístrate  <Link to="/singup">aquí</Link>
                </form>
            </div>

        </div>
    );
};

export default Login