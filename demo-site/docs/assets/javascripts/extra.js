/* ============================================================
   Documentation Skills Toolkit — UX Enhancements v3

   3-tier page transitions:
   1. CSS fallback (all browsers)
   2. View Transitions API (Chrome 111+)
   3. Directional slide (Chrome 111+ with nav tracking)

   + Scroll reveal animations
   ============================================================ */

(function () {
  "use strict";

  var previousPath = window.location.pathname;

  /* ── Scroll Reveal ───────────────────────────────────────*/
  function initScrollReveal() {
    var targets = document.querySelectorAll(
      ".grid-cards .card, " +
      ".template-gallery .template-item, " +
      ".md-typeset .admonition, " +
      ".md-typeset details, " +
      ".md-typeset table, " +
      ".md-typeset pre, " +
      ".stats-bar .stat, " +
      ".hero-banner, " +
      ".md-content h2, " +
      ".md-content h3"
    );

    if (!targets.length) return;

    for (var i = 0; i < targets.length; i++) {
      var el = targets[i];
      if (el.classList.contains("reveal")) continue;
      el.classList.add("reveal");

      // Stagger for grid children
      var parent = el.parentElement;
      if (parent && (
        parent.classList.contains("grid-cards") ||
        parent.classList.contains("template-gallery") ||
        parent.classList.contains("stats-bar")
      )) {
        var idx = Array.prototype.indexOf.call(parent.children, el);
        el.style.transitionDelay = (idx * 0.08) + "s";
      }
    }

    if (!("IntersectionObserver" in window)) {
      for (var k = 0; k < targets.length; k++) {
        targets[k].classList.add("reveal-visible");
      }
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            requestAnimationFrame(function () {
              entry.target.classList.add("reveal-visible");
            });
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.06, rootMargin: "0px 0px -20px 0px" }
    );

    for (var j = 0; j < targets.length; j++) {
      observer.observe(targets[j]);
    }
  }

  /* ── View Transitions (Tier 2 & 3) ──────────────────────
     Hook into MkDocs Material instant navigation.
     Uses View Transitions API for smooth cross-fade.
     Detects navigation direction for directional slide.
  */
  function initViewTransitions() {
    if (!document.startViewTransition) return;

    // Track navigation direction based on tab order
    var navLinks = document.querySelectorAll(".md-tabs__link");
    var tabOrder = {};
    navLinks.forEach(function (link, i) {
      var href = link.getAttribute("href");
      if (href) tabOrder[href] = i;
    });

    // Store current tab index
    var activeLink = document.querySelector(".md-tabs__link--active");
    if (activeLink) {
      var activeHref = activeLink.getAttribute("href");
      if (activeHref) {
        document.documentElement.dataset.navIndex = tabOrder[activeHref] || 0;
      }
    }
  }

  function detectDirection() {
    var currentPath = window.location.pathname;
    var navLinks = document.querySelectorAll(".md-tabs__link");
    var currentIndex = -1;
    var previousIndex = -1;

    navLinks.forEach(function (link, i) {
      var href = link.href;
      if (href && currentPath.indexOf(new URL(href).pathname) !== -1) {
        currentIndex = i;
      }
      if (href && previousPath.indexOf(new URL(href).pathname) !== -1) {
        previousIndex = i;
      }
    });

    previousPath = currentPath;

    if (currentIndex > previousIndex) return "forward";
    if (currentIndex < previousIndex) return "backward";
    return "neutral";
  }

  /* ── Content Enter Animation ─────────────────────────────
     Fallback (Tier 1) for browsers without View Transitions.
     Also runs after View Transition completes.
  */
  function animateContentIn() {
    var content = document.querySelector(".md-content");
    if (!content) return;

    // Detect direction and apply appropriate animation
    var direction = detectDirection();
    content.classList.remove("content-enter", "content-enter-forward", "content-enter-backward");
    void content.offsetWidth; // Force reflow

    if (direction === "forward") {
      content.classList.add("content-enter-forward");
    } else if (direction === "backward") {
      content.classList.add("content-enter-backward");
    } else {
      content.classList.add("content-enter");
    }
  }

  /* ── Sidebar Active Smooth ───────────────────────────────*/
  function initSidebarScroll() {
    var active = document.querySelector(".md-nav__link--active");
    if (active && active.closest(".md-sidebar__scrollwrap")) {
      setTimeout(function () {
        active.scrollIntoView({ block: "center", behavior: "smooth" });
      }, 400);
    }
  }

  /* ── Initialize ──────────────────────────────────────────*/
  function init() {
    animateContentIn();
    initScrollReveal();
    initViewTransitions();
    initSidebarScroll();
  }

  // Initial load
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // MkDocs Material instant navigation
  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      setTimeout(init, 30);
    });
  }
})();
