/* Como se generan los proyectos en React desde cero  */
import React from "react"; /* Estamos importando React desde React Y lo mismo hacemos con el ReactDOM */
import ReactDOM from "react-dom/client";
import { App } from "./App";
import './index.css'

const root = ReactDOM.createRoot(document.getElementById('root'))


root.render(
  <App/>
)