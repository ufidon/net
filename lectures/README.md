# The Application Layer

## HTTP
- [HTTP Header Live](https://addons.mozilla.org/en-US/firefox/addon/http-header-live/)
- [curl: command line tool and library for transferring data with URLs](https://curl.se/)
- [HTTP Prompt](https://http-prompt.com/)
  - [httpie](https://httpie.io/)
- [httpbin: A simple HTTP Request & Response Service](https://httpbin.org/)

### Browser cache
- [SQLite](https://sqlite.org/)
  ```bash
  # 1. Install sqlite3
  sudo apt-get install sqlite3

  # 2. Find Firefox cookie database cookies.sqlite then open it
  sqlite3 cookies.sqlite

  # 3. Find Chrome or Chromium cookie database Cookies then open it
  sqlite3 Cookies
  ```

### Web servers  
- [nginx](https://nginx.org/)
- [Apache](https://httpd.apache.org/)

### Web proxy
- [Varnish HTTP Cache](https://varnish-cache.org/)
- [HAProxy: The Reliable, High Performance TCP/HTTP Load Balancer](https://www.haproxy.org/)
- [SQUID Web Proxy Cache](https://github.com/squid-cache/squid)
- [ZAP: Zed Attack Proxy](https://www.zaproxy.org/)

## DNS

### Querying DNS Records

| **Task**              | **Windows Command**              | **Linux Command**                                |
| --------------------- | -------------------------------- | ------------------------------------------------ |
| Basic name resolution | `nslookup example.com`           | `nslookup example.com` or `host example.com`     |
| Query A record        | `nslookup -query=A example.com`  | `dig example.com A`                              |
| Query MX record       | `nslookup -query=MX example.com` | `dig example.com MX` or `host -t MX example.com` |
| Query NS record       | `nslookup -query=NS example.com` | `dig example.com NS`                             |
| Reverse lookup        | `nslookup 8.8.8.8`               | `dig -x 8.8.8.8` or `host 8.8.8.8`               |


### Tracing DNS Resolution

| **Task**                 | **Windows**                                               | **Linux**                                            |
| ------------------------ | --------------------------------------------------------- | ---------------------------------------------------- |
| Trace DNS path           | `nslookup` → inside interactive mode: `set d2` then query | `dig example.com +trace`                             |
| Show default DNS servers | `ipconfig /all`                                           | `systemd-resolve --status` or `cat /etc/resolv.conf` |


### Flushing & Managing DNS Cache

| **Task**        | **Windows**            | **Linux**                                                                                                                                              |
| --------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Flush DNS cache | `ipconfig /flushdns`   | Depends on resolver: <br>• `sudo systemd-resolve --flush-caches` (systemd) <br>• `sudo rndc flush` (BIND) <br>• `sudo /etc/init.d/nscd restart` (nscd) |
| Show cache      | `ipconfig /displaydns` | `sudo systemd-resolve --statistics` (systemd)                                                                                                          |


### Example Usage

**Windows (PowerShell or CMD):**

```cmd
nslookup -query=MX gmail.com
ipconfig /flushdns
```

**Linux (bash):**

```bash
dig gmail.com MX
sudo systemd-resolve --flush-caches
```
