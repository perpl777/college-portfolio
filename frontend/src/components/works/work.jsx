import React from "react";

import styles from "./works.module.css";

function Work({ image, title }) {
  return (
    <div className={styles.work}>
      <img className={styles.image} src={image} alt={title} />
    </div>
  );
}

export default Work;
