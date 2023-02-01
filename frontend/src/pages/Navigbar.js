import React from 'react'
import {Link} from 'react-router-dom'

const Navigbar = () => {
    return (
        <nav class="navbar-padding navbar navbar-expand-lg navbar-light bg-light" style = {{'padding-left': '10vh'}}>
        <Link class="navbar-brand" to="/singup">Create an account</Link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <Link class="nav-item nav-link active" to="/">Log in </Link>
            <Link class="nav-item nav-link" to="/events">Events</Link>
            <Link class="nav-item nav-link" to="/singout">Sing out</Link>
          </div>
        </div>
      </nav>
    )
  }
  
  export default Navigbar
  