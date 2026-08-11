(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');
  var submenuToggles = document.querySelectorAll('.sidebar-submenu-toggle');

  function setSubmenuState(button, submenu, isExpanded) {
    var group = button.closest('.sidebar-nav-group');

    button.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
    submenu.hidden = !isExpanded;

    if (group) {
      group.classList.toggle('is-open', isExpanded);
    }
  }

  // Sidebar stays collapsed by default on all viewports.
  // Users open it via the toggle control.
  if (checkbox) {
    checkbox.checked = false;
  }

  Array.prototype.forEach.call(submenuToggles, function(button) {
    var submenuId = button.getAttribute('aria-controls');
    var submenu = submenuId ? document.getElementById(submenuId) : null;

    if (!submenu)
      return;

    setSubmenuState(button, submenu, button.getAttribute('aria-expanded') === 'true');

    button.addEventListener('click', function(e) {
      e.preventDefault();

      setSubmenuState(button, submenu, button.getAttribute('aria-expanded') !== 'true');
    });
  });

  document.addEventListener('click', function(e) {
    var target = e.target;

    if(!checkbox.checked ||
       sidebar.contains(target) ||
       (target === checkbox || target === toggle)) return;

    checkbox.checked = false;
  }, false);
})(document);
