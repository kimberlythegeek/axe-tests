/* Modified from https://github.com/lsmith/a11y-css-highlight/blob/master/js/a11y-css.js */


/*
 * CSS

[tabindex="0"] {
  background:yellow
}
[tabindex]:before {
  content:attr(tabindex);
  color:red;
  font-weight:bold
}
[role] {
  border: 3px dashed gold;
}
[role]:before {
  content:attr(role);
  color:green;
  font-weight:bold
}
article,
header,
footer,
nav,
section,
sidebar {
  border: 3px dashed aqua;
}
article:before,
header:before,
footer:before,
nav:before,
section:before,
sidebar:before {
  color:green;
  font-weight:bold;
}
header:before {
  content:"header";
}
article:before {
  content:"article";
}
section:before {
  content:"section";
}
nav:before {
  content:"nav";
}
footer:before {
  content:"footer";
}
 */
(function (document) {
  var css = '[role]:before,article:before,footer:before,header:before,nav:before,section:before,sidebar:before{color:green;font-weight:700}[tabindex="0"]{background:#ff0}[tabindex]:before{content:attr(tabindex);color:red;font-weight:700}[role]{border:3px dashed gold}[role]:before{content:attr(role)}article,footer,header,nav,section,sidebar{border:3px dashed #0ff}header:before{content:"header"}article:before{content:"article"}section:before{content:"section"}nav:before{content:"nav"}footer:before{content:"footer"}'
  var style = document.getElementById('aria-highlight');

  if (style) {
      style.disabled = !style.disabled;
  } else {
      style = document.createElement('style');
      style.id = 'aria-highlight';
      style.type = 'text/css';
      if (style.styleSheet) {
          style.styleSheet.cssText = css;
      } else {
          style.appendChild(document.createTextNode(css));
      }
      document.getElementsByTagName('head')[0].appendChild(style);
  }
})(document);
