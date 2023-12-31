import React from "react";
import { Link } from 'react-router-dom'

const NewCompoment = () => {
  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <Link className="navbar-brand">Navbar</Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link
                to="./HomePage"
                className="nav-link active"
                aria-current="page"
              >
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link to="./Login" className="nav-link">
                Login
              </Link>
            </li>
            <li className="nav-item dropdown">
              <Link
                to="./ProfilePage"
                className="nav-link dropdown-toggle"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Profile
              </Link>
              <ul className="dropdown-menu">
                <li>
                  <Link to="./ProfilePage" className="dropdown-item">
                    Action
                  </Link>
                </li>
                <li>
                  <Link className="dropdown-item">Another action</Link>
                </li>
                <li>
                  <Link className="dropdown-item">Something else here</Link>
                </li>
              </ul>
            </li>
            <li className="nav-item">
              <Link className="nav-link disabled" aria-disabled="true">
                Disabled
              </Link>
            </li>
          </ul>
          <form className="d-flex" role="search">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button className="btn btn-outline-success" type="submit">
              Search
            </button>
          </form>
        </div>
      </div>
    </nav>
  );
};

export default NewCompoment;
