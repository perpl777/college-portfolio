import React from "react";

import Button from "../button/button";

import styles from "./header.module.css";

function Header({typesOfWorks}) {
  return (
    <header className={styles.container}>
      <h1 className="text-extra-big bold">Работы студентов</h1>
      <div className={styles.filters}>
        <Button>Все работы</Button>
        {
          typesOfWorks.map((type) =>
            <Button key={type.id}>{type.type}</Button>
          )
        }
      </div>
    </header>
  );
}

export default Header;
