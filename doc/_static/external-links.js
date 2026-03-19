// Copyright 2026 the contributors of APPXC (github.com/alexander-nbg/appxc)
// SPDX-License-Identifier: 0BSD

/* Mostly AI generated and maintained */

(function () {
  function isExternalHttpLink(anchor) {
    const href = anchor.getAttribute("href");
    if (!href) {
      return false;
    }

    let resolvedUrl;
    try {
      resolvedUrl = new URL(href, window.location.href);
    } catch {
      return false;
    }

    if (resolvedUrl.protocol !== "http:" && resolvedUrl.protocol !== "https:") {
      return false;
    }

    return resolvedUrl.host !== window.location.host;
  }

  function decorateExternalLinks() {
    const anchors = document.querySelectorAll("a.reference.external[href]");

    for (const anchor of anchors) {
      if (!isExternalHttpLink(anchor)) {
        continue;
      }

      anchor.setAttribute("target", "_blank");
      anchor.setAttribute("rel", "noopener noreferrer");
      anchor.classList.add("external-link-global");

      if (anchor.querySelector(".external-link-icon")) {
        continue;
      }

      const icon = document.createElement("i");
      icon.className = "external-link-icon fa-solid fa-up-right-from-square";
      icon.setAttribute("aria-hidden", "true");
      anchor.append(icon);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", decorateExternalLinks);
  } else {
    decorateExternalLinks();
  }
})();
