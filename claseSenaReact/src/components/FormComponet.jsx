import { useState } from "react";
import { useNavigate } from 'react-router-dom';

const FormComponet = () => {
  const navigate = useNavigate()
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");

  const ClickButtonInicio = () => {
  console.log(user);
    console.log(pass);
    navigate('/')
  }

  return (
    <div className='conteiner'>
      <h2>Formulario</h2>

      <label htmlFor="username" className="form-label">Usuario:</label>
      <input
        value={user}
        onChange={(event) => setUser(event.target.value)}
        type="text"
        className="form-control"
        id="username"
        name="username" />

      <label htmlFor="password" className="form-label">Contraseña:</label>
      <input
        value={pass}
        onChange={(valor) => setPass(valor.target.value)}
        type="password"
        className="form-control"
        id="password"
        name="password" />
      {/* <button className="button"> {textButton}</button> */}
      <button
        onClick={ClickButtonInicio}
        className="btn btn-primary" >
        {" "}
        Inicio </button>
    </div >
  )
}
export default FormComponet;