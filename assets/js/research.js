/* Research portfolio interactions: scroll reveal, lazy video playback,
 * media tabs on project cards, and the BibTeX dialog. No dependencies. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasIO = "IntersectionObserver" in window;

  /* ---- Scroll reveal ---------------------------------------------------- */
  var reveals = document.querySelectorAll(".rh-reveal");
  if (!hasIO || reduceMotion) {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var revealIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("is-visible");
          revealIO.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    reveals.forEach(function (el) { revealIO.observe(el); });
  }

  /* ---- Lazy autoplay videos -------------------------------------------- */
  var videos = Array.prototype.slice.call(document.querySelectorAll("video[data-rh-autoplay]"));

  function isShown(v) {
    var pane = v.closest(".rh-media-pane");
    return !pane || pane.classList.contains("is-active");
  }
  function tryPlay(v) {
    if (reduceMotion || !isShown(v)) return;
    if (v.preload === "none") v.preload = "auto";
    var p = v.play();
    if (p && p.catch) p.catch(function () { v.controls = true; });
  }

  if (reduceMotion) {
    videos.forEach(function (v) { v.controls = true; v.removeAttribute("loop"); });
  } else if (hasIO) {
    var videoIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        v._rhVisible = e.isIntersecting;
        if (e.isIntersecting) tryPlay(v); else v.pause();
      });
    }, { threshold: 0.25 });
    videos.forEach(function (v) { videoIO.observe(v); });
  } else {
    videos.forEach(tryPlay);
  }

  /* ---- Media tabs ------------------------------------------------------- */
  document.querySelectorAll("[data-rh-tabs]").forEach(function (media) {
    var tabs = media.querySelectorAll(".rh-tab");
    var panes = media.querySelectorAll(".rh-media-pane");
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t, j) { t.setAttribute("aria-selected", j === i ? "true" : "false"); t.tabIndex = j === i ? 0 : -1; });
        panes.forEach(function (pane, j) {
          var on = j === i;
          pane.classList.toggle("is-active", on);
          pane.setAttribute("aria-hidden", on ? "false" : "true");
          var v = pane.querySelector("video");
          if (v) { if (on && v._rhVisible !== false) tryPlay(v); else v.pause(); }
        });
      });
      tab.addEventListener("keydown", function (ev) {
        var k = ev.key, n = tabs.length, next = null;
        if (k === "ArrowRight") next = (i + 1) % n;
        if (k === "ArrowLeft") next = (i - 1 + n) % n;
        if (next !== null) { ev.preventDefault(); tabs[next].focus(); tabs[next].click(); }
      });
    });
  });

  /* ---- BibTeX dialog ---------------------------------------------------- */
  var dialog = document.getElementById("rh-bib-dialog");
  var body = document.getElementById("rh-bib-dialog-body");
  if (dialog && body) {
    var copyBtn = dialog.querySelector("[data-rh-copy]");
    document.addEventListener("click", function (ev) {
      var btn = ev.target.closest && ev.target.closest("[data-rh-bib]");
      if (!btn) return;
      ev.preventDefault();
      var src = btn.closest(".rh-pub").querySelector(".rh-pub-bibsrc");
      body.textContent = src ? src.textContent.trim() : "";
      copyBtn.textContent = "Copy";
      if (typeof dialog.showModal === "function") dialog.showModal();
      else dialog.setAttribute("open", "");
    });
    dialog.querySelector("[data-rh-close]").addEventListener("click", function () { dialog.close(); });
    dialog.addEventListener("click", function (ev) { if (ev.target === dialog) dialog.close(); });
    copyBtn.addEventListener("click", function () {
      var text = body.textContent;
      var done = function () { copyBtn.textContent = "Copied"; };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { copyBtn.textContent = "Select and copy"; });
      } else {
        var r = document.createRange(); r.selectNodeContents(body);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
        copyBtn.textContent = "Selected";
      }
    });
  }
})();
