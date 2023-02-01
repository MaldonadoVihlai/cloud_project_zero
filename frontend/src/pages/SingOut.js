import React from 'react'
import {Link} from 'react-router-dom'
import { useNavigate } from "react-router-dom";

const SingOut = () => {
    const navigate = useNavigate();
    localStorage.removeItem('token');
    navigate("/login");
  }
  
  export default SingOut