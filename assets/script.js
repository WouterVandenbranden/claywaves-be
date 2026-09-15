// ClayWaves — kleine interacties: mobiel menu + lightbox voor de galerijen.
(function () {
  'use strict';

  // --- mobiel menu -------------------------------------------------------
  var knop = document.querySelector('.nav-knop');
  var nav = document.getElementById('hoofdnav');
  if (knop && nav) {
    var sluitOpBreed = window.matchMedia('(min-width: 821px)');
    var zetOpen = function (open) {
      knop.setAttribute('aria-expanded', open ? 'true' : 'false');
      nav.hidden = !open && !sluitOpBreed.matches;
    };
    zetOpen(false);
    knop.addEventListener('click', function () {
      zetOpen(knop.getAttribute('aria-expanded') !== 'true');
    });
    var pasAan = function () { nav.hidden = sluitOpBreed.matches ? false : knop.getAttribute('aria-expanded') !== 'true'; };
    sluitOpBreed.addEventListener('change', pasAan);
    pasAan();
  }

  // --- lightbox ----------------------------------------------------------
  var dialoog = document.getElementById('lichtbak');
  if (!dialoog || typeof dialoog.showModal !== 'function') return;

  var beeld = dialoog.querySelector('img');
  var bijschrift = dialoog.querySelector('.bijschrift');

  document.querySelectorAll('[data-licht]').forEach(function (knopje) {
    knopje.addEventListener('click', function () {
      var img = knopje.querySelector('img');
      if (!img) return;
      beeld.src = img.currentSrc || img.src;
      beeld.alt = img.alt || '';
      bijschrift.textContent = knopje.getAttribute('data-bijschrift') || img.alt || '';
      dialoog.showModal();
    });
  });

  dialoog.querySelector('.sluit').addEventListener('click', function () { dialoog.close(); });
  dialoog.addEventListener('click', function (e) {
    if (e.target === dialoog) dialoog.close();
  });
  dialoog.addEventListener('close', function () { beeld.removeAttribute('src'); });
})();
