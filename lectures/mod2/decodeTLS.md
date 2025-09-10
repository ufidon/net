# Decode TLS

## **Using the TLS Key Log File (`SSLKEYLOGFILE`)**

**Best for:** When you control the client (e.g., Chrome, Firefox, curl). Works with modern TLS (including ECDHE).
**Idea:** The client writes session keys (pre-master/master secrets) to a log file. Wireshark can use these keys to decrypt TLS traffic.

---

### **Steps**

1. **Create a key log file**

   * Example paths:

     * Linux/macOS: `~/sslkeys.log`
     * Windows: `C:\keys\sslkeys.log` (make sure the folder exists)

2. **Set the environment variable and launch the browser**

   * **Windows (Command Prompt, Chrome example):**

     ```cmd
     set SSLKEYLOGFILE=C:\keys\sslkeys.log
     "C:\Program Files\Google\Chrome\Application\chrome.exe"
     ```

   * **Windows (PowerShell):**

     ```powershell
     $env:SSLKEYLOGFILE="C:\keys\sslkeys.log"
     Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe"
     ```

   * **macOS (Terminal):**

     ```bash
     export SSLKEYLOGFILE=~/sslkeys.log
     open -a "Google Chrome"
     ```

   * **Linux:**

     ```bash
     export SSLKEYLOGFILE=~/sslkeys.log
     google-chrome &
     ```

   > 🔑 Important: You must start the browser from the same environment where the variable is set.

   Both **Chrome** and **Firefox** support this.

3. **Browse to your HTTPS target**
   The client will write session keys into the `sslkeys.log` file as connections are established.

4. **Configure Wireshark**

   * Open Wireshark → `Edit` → `Preferences` → `Protocols` → `TLS`
   * In **(Pre)-Master-Secret log filename**, enter the path to your `sslkeys.log` file.
   * Confirm and restart Wireshark (or reload your capture).

5. **Capture and view decrypted traffic**

   * Start a capture while visiting the HTTPS site.
   * If session keys are available, Wireshark will automatically show decrypted application data (`http`, `http2`, etc.).
   * You can right-click a packet → `Follow` → `HTTP Stream` to see plaintext.

---

### **Pros**

* Works with modern TLS (ECDHE, TLS 1.2, TLS 1.3).
* Doesn’t require the server’s private key.
* Relatively easy to set up for browsers.

### **Cons**

* You must control the client and set the environment variable.
* Doesn’t work retroactively (must capture traffic after enabling key logging).

---

⚠️ **Reminder:** Use this only on traffic you are authorized to analyze (your own systems, labs, or with explicit permission).

