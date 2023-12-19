import React from "react";

import Work from "./work"

import styles from "./works.module.css";

function Works({ works }) {
  return (
    <div className={`${styles.container} mt-5`}>
      <div className={styles.works}>
        {
          works.map((work) =>
            <Work key={work.id} image={work.image} title={work.title} />
          )
        }
      </div>
    </div>
  );
}

export default Works;
