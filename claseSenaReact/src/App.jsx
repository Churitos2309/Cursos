// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import "./App.css";
import Buttoncom from "./components/ButtonCom.jsx";
import FormComponet from "./components/FormComponet.jsx";
import { BrowserRouter, useRoutes } from "react-router-dom";
import Login from "./pages/Login";
import NewCompoment from "./components/NewCompoment";
import HomePage from "./pages/HomePage.jsx";


function App() {
  const AppRoutes = () => {
    let router = useRoutes([
      { path: "/", element: <HomePage/> },
      { path: "/login", element: <Login/> },
      { path: "/HomePage", element: <HomePage/> },
    ]);
    return router;
  };

  return (
    <div className="App">
      <BrowserRouter>
        <NewCompoment/>
        <AppRoutes/>
      </BrowserRouter>
    </div>
  );
}
export default App;
