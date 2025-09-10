# How to disable HSTS upgrade?

 Modern browsers **auto-upgrade HTTP to HTTPS** when possible — often called **HTTPS-Only Mode** or **HSTS upgrade**. The behavior depends on the browser. Here’s how you can **disable auto-upgrade** so the browser actually uses plain `http://` when you type it.

---

## **Chrome / Edge (Chromium-based)**

1. Open `chrome://settings/security` (or `edge://settings/security`).
2. Scroll to **“Always use secure connections”**.
3. **Turn it off** (disable).

> ⚠️ Note: Chrome also uses **HSTS preload lists** for some sites (e.g., google.com, facebook.com). For those, you *cannot* force HTTP — the browser will always use HTTPS.

---

## **Firefox**

1. Open `about:preferences#privacy`.
2. Scroll to **HTTPS-Only Mode**.
3. Select **Don’t enable HTTPS-Only Mode**.

Optional (advanced): In `about:config`, set

* `dom.security.https_only_mode` → `false`
* `dom.security.https_only_mode_pbm` → `false` (for private browsing).

---

## **Safari (macOS / iOS)**

Safari doesn’t have a simple toggle. It automatically upgrades to HTTPS if:

* The site is on the **HSTS preload list**, or
* The server previously sent an **HSTS header**.

👉 You can’t fully disable this in Safari without using developer tools or a custom proxy that strips HSTS headers.

---
- Use [HTTP FOREVER](http://httpforever.com/) for testing.