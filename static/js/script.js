function wrapNumbersWithSpan(node) {
    if (node.nodeType === Node.TEXT_NODE) {
      const replaced = node.textContent.replace(/\d+/g, match => {
        return `<span class="number">${match}</span>`;
      });
  
      if (replaced !== node.textContent) {
        const temp = document.createElement('span');
        temp.innerHTML = replaced;
        node.parentNode.replaceChild(temp, node);
      }
    } else {
      node.childNodes.forEach(wrapNumbersWithSpan);
    }
  }
  
  wrapNumbersWithSpan(document.body);
  