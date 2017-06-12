/*!
 * Your use of this Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 *
 * This entire copyright notice must appear in every copy of this file you
 * distribute or in any file that contains substantial portions of this source
 * code.
 */

// Get axe-core rules
// Default setting is all rules
axe.getRules();
// Run axe
axe.run()
// On success, process results
.then(function(result){
  console.log(result);
  // Get <html> element
  var window = document.getElementsByTagName('html');
  // Create new div element
  var node = document.createElement('DIV');
  // Populate div with results text
  var textNode = document.createTextNode(JSON.stringify(result));
  node.appendChild(textNode);
  // Add selector to element
  node.setAttribute('id', 'axe-result');
  // And append to <html> element
  window[0].appendChild(node);
});
