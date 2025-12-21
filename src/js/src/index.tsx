import React, { useEffect, useRef } from "react";
import ReactDOM from "react-dom";
import { render as renderGH } from "./buttons.esm";

interface BindConfig {}

interface BindResult {
  create: (type: any, props: any, children: any[]) => React.ReactElement;
  render: (element: React.ReactElement) => React.Component | Element | void;
  unmount: () => boolean;
}

export function bind(node: Element, config: BindConfig): BindResult {
  return {
    create: (type: any, props: any, children: any[]) => {
      if (node.childElementCount) {
        const firstChild = node.firstChild?.firstChild;
        if (firstChild) {
          ReactDOM.unmountComponentAtNode(firstChild as Element);
        }
      }
      return React.createElement(type, props, ...children);
    },
    render: (element: React.ReactElement) => {
      return ReactDOM.render(element, node);
    },
    unmount: () => {
      return ReactDOM.unmountComponentAtNode(node);
    },
  };
}

/**
 * Wrapper for github-buttons library. For API and
 * examples see:
 *
 * https://github.com/buttons/github-buttons
 *
 */

interface RactpyGithubButtonsProps {
  href?: string;
  title?: string;
  "aria-label"?: string;
  "data-icon"?: string;
  "data-color-scheme"?: string;
  data_text?: string;
  "data-size"?: string;
  "data-show-count"?: string;
  [key: string]: any;
}

export function RactpyGithubButtons(props: RactpyGithubButtonsProps) {
  const ref = useRef<HTMLAnchorElement>(null);

  // console.log('RactpyGithubButtons %o', props)

  // https://dmitripavlutin.com/react-useeffect-explanation/

  useEffect(() => {
    renderGH(ref.current, function (element: HTMLElement) {
      if (!ref.current) {
        return;
      }
      ref.current.replaceChild(element, ref.current.firstChild!);
    });

    return () => {
      // console.log('userEffect.unmount')
    };
  }, [props]);

  return (
    <a {...props} ref={ref}>
      <div {...props}>{props.data_text}</div>
    </a>
  );
}
