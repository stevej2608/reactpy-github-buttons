import React, { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import { render as renderGH } from "github-buttons";

export function bind(node, config) {
  return {
    create: (type, props, children) => {
      console.log('create')
      React.createElement(type, props, ...children)
    },
    render: (element) => {
      console.log('render')
      ReactDOM.render(element, node)
    },
    unmount: () => {
      console.log('unmount')
      ReactDOM.unmountComponentAtNode(node)
    },
  }
}

/**
 * Wrapper for github-buttons library. For API and
 * examples see:
 *
 * https://github.com/buttons/github-buttons
 *

 */

export function RactpyGithubButtons(props) {
  const ref = useRef(null);

  useEffect(() => {

    renderGH(ref.current, function (element) {
      if (!ref.current) {
        return;
      }
      ref.current.parentNode.replaceChild(element, ref.current);
    })

    return () => {


      console.log('RactpyGithubButtons.unmount')
      // Anything in here is fired on component unmount.
      // https://robertmarshall.dev/blog/componentwillunmount-functional-components-react/
      ReactDOM.unmountComponentAtNode(ref.current);
    }


  }, []);

  return (
    <a {...props} ref={ref}>
      {props.data_text}
    </a>
  );
}