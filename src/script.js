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
