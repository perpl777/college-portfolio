import React from "react";

import styles from "./button.module.css";

function Button(props) {
  return (
    <button className={`${styles.btn} text-small pt-2 pb-2 pl-4 pr-4 br-30`}>
      {props.children}
    </button>
  );
}

export default Button;
