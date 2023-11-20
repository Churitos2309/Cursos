/* Cual es la dferencia entre un COMPONENTE y un ELEMENTO */
/* Un COMPONENTE es una FACTORIA de elementos; Es una funcion que al ejecutarla te devuelve 1 ELEMENTO */
/* Y el elemento es lo que se reenderiza */
/* React lo que Reenderiza son ELEMENTOS */

/* Las PROMS tiene que ser INNUTABLES */
import { useState } from "react";
import "./App.css";
import { TwitterFollowCard } from "./TwitterFollowCard";


export function App() {
  return(
    <section>

<TwitterFollowCard isFollowing = {false} userName = "JuanOchoa" name= "Juan Eduardo Ochoa">
  Juan children
</TwitterFollowCard>

<TwitterFollowCard isFollowing = {false} userName = "Juan" name= "Juan Eduardo Ochoa">
  Ochoa children
</TwitterFollowCard>
<TwitterFollowCard isFollowing userName = "JuanEduardo" name= "Juan Eduardo">
  Eduardo children
</TwitterFollowCard>

<TwitterFollowCard isFollowing userName = "Ochoa" name= "Juan">
  Cordoba children
</TwitterFollowCard>
      
      <button onClick={() => setName ('ElverCokel')}>
        Cambio Nombre
      </button>
    </section>
  )
}


/*
export function App() {
  const format = (userName) => `@${userName}`;
  return (
    <section className="App">
      <TwitterFollowCard
        formatUserName={format}
        isFollowing
        userName="Juan"
        name="Juan Ochoa"
      />
      <TwitterFollowCard
        formatUserName={format}
        isFollowing={false}
        userName="Khalifa"
        name="Diomedes Khalifa"
      />
      <TwitterFollowCard
        formatUserName={format}
        isFollowing
        userName="midudev"
        name="Miguel Angel Dural"
      />
      <TwitterFollowCard 
      formatUserName={format}
      isFollowing 
      userName="Frank" 
      name="Michael Frank" 
      />
    </section>
  );
}

*/