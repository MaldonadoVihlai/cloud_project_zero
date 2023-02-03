import logo from './logo.svg';
import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigbar from './pages/Navigbar'
import { SingUp } from './pages/SingUp';
import Login from './pages/Login';
import { Events } from './pages/Events';
import SingOut from './pages/SingOut';
import './App.css';


function App() {
  const [token, setToken] = useState('')
  const [userId, setUserId] = useState('')

  useEffect( ()=>{
    const newToken = localStorage.getItem('token')
    const userId = localStorage.getItem('id')
    if (newToken && newToken != "" && newToken != undefined) setToken(newToken)
  }, [token]);
  useEffect( ()=>{
    const newUserId = localStorage.getItem('id')
    if (newUserId && newUserId != "" && newUserId != undefined) setUserId(newUserId)
  }, [userId]);
  return (
    <Router>
      <Navigbar />
      <div>
        <Routes>
          <Route exact path="/" element={<Login/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/singup" element={<SingUp/>} />
          <Route path="/singout" element={<SingOut/>} />
          <Route path="/events" element={<Events token={token} userId={userId}/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
