import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {Link} from 'react-router-dom'

const API = process.env.REACT_APP_API;

export const SingUp = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");


  const handleSubmit = async (e) => {
    e.preventDefault();
    {
      const res = await fetch(`${API}/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email,
          password,
        }),
      });
      await res.json();
      if (res.status == 200) {
        alert("Usuario creado exitosamente")
        navigate("/login")
      }
      if (res.status == 409) {
        alert("El email ya está registrado en el servidor, intente uno nuevo")
      }
    }

    setEmail("");
    setPassword("");
  };


  return (
    <div>
      <div className="row center">
        <div className={`col-md-4`}>
          <h2>Registration</h2>
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
                  required="True"
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
                  required="True"
                />
              </label>
            </div>
            <button className="btn btn-primary btn-block">
              Create
            </button>
            <br/>
                    ¿Ya tienes una cuenta?, inicia sesión  <Link to="/login">aquí</Link>
          </form>
        </div>

      </div>
    </div>
  );
};