import React, { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import { render as renderGH } from "github-buttons";

export function bind(node, config) {
  return {
    create: (type, props, children) => React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

/**
 * Wrapper for github-buttons library. For API and
 * examples see:
 *
 * https://github.com/buttons/github-buttons
 *

 */

export function RactpyGithubBtn(props) {
  const ref = useRef(null);

  useEffect(() => {
    renderGH(ref.current, function (element) {
      if (!ref.current) {
        return;
      }
      ref.current.parentNode.replaceChild(element, ref.current);
    });
  }, []);

  return (
    <a {...props} ref={ref}>
      {props.data_text}
    </a>
  );
}