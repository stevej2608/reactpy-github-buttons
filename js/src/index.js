import React, { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import { render as renderGH } from "./buttons.esm";

export function bind(node, config) {
  return {
    create: (type, props, children) => {
      if (node.childElementCount){
        ReactDOM.unmountComponentAtNode(node.firstChild.firstChild)
      }
      return React.createElement(type, props, ...children)
    },
    render: (element) => {
      return ReactDOM.render(element, node)
    },
    unmount: () => {
      return ReactDOM.unmountComponentAtNode(node)
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

  // console.log('RactpyGithubButtons %o', props)

  // https://dmitripavlutin.com/react-useeffect-explanation/

  useEffect(() => {

    renderGH(ref.current, function (element) {
      if (!ref.current) {
        return;
      }
      ref.current.replaceChild(element, ref.current.firstChild);
    })

    return () => {
      // console.log('userEffect.unmount')
    }

  }, [props]);


  return (
    <a {...props} ref={ref}>
      <div {...props}>
        {props.data_text}
      </div>
    </a>
  );
}