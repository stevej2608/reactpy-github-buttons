import React, { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import { render as renderGH } from "github-buttons";

export function bind(node, config) {
  return {
    create: (type, props, children) => {
      console.log('bind.create %s, props=%o', type.name, props)

      if (node.childElementCount){
        console.log('bind.create - remove children')
        ReactDOM.unmountComponentAtNode(node.firstChild.firstChild)
        console.log('bind.create - removed children')
      }

      const result = React.createElement(type, props, ...children)

      console.log('bind.create - done')
      return result

    },
    render: (element) => {
      console.log('bind.render')
      return ReactDOM.render(element, node)
    },
    unmount: () => {
      console.log('bind.unmount')
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

  console.log('RactpyGithubButtons %o', props)

  // https://dmitripavlutin.com/react-useeffect-explanation/

  useEffect(() => {

    renderGH(ref.current, function (element) {
      if (!ref.current) {
        console.log('render.GH - null')
        return;
      }
      console.log('render.GH - replaceChild')
      // ref.current.parentNode.replaceChild(element, ref.current);
      ref.current.replaceChild(element, ref.current.firstChild);
    })

    return () => {

      console.log('userEffect.unmount')

      // Anything in here is fired on component unmount.
      // https://robertmarshall.dev/blog/componentwillunmount-functional-components-react/
      // if (ref) {
      //   console.log('RactpyGithubButtons.unmount')
      //   ReactDOM.unmountComponentAtNode(ref);
      // }
    }


  }, [props]);


  useEffect(() => {
    return () => {
      console.log('Anything in here is fired on component UNMOUNT.');
     }
   }, []);


  console.log('RactpyGithubButtons.render')

  return (
    <div className="button-container" ref={ref}>
      <a {...props}>
        {props.data_text}
      </a>
    </div>
  );
}