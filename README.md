# supply_chain_mis
Supply Chain MIS 

#  **YOU HAVE 2 THINGS TO RUN**

1️⃣ **Flask Backend (your APIs)**
2️⃣ **Streamlit UI (your dashboard)**

👉 BOTH must run together.

---

# ⚙️ **STEP 1: OPEN TERMINAL IN PROJECT FOLDER**

```bash
cd Desktop/supply_chain_mis
```

---

# 🔹 **STEP 2: ACTIVATE VENV**

```bash
source venv/bin/activate
```

---

# 🔥 **STEP 3: RUN FLASK BACKEND**

```bash
python app.py
```

👉 You should see:

```plaintext
Running on http://127.0.0.1:5000
```

✔ KEEP THIS TERMINAL RUNNING
❌ Don’t close it

---

# 🧪 **STEP 4: TEST BACKEND (VERY IMPORTANT)**

Open browser:

```plaintext
http://127.0.0.1:5000/sensor
```

👉 If you see JSON → backend working ✅

---

# 🖥 **STEP 5: OPEN NEW TERMINAL (IMPORTANT)**

👉 Don’t stop Flask
👉 Open a second terminal tab

---

# 🔹 **STEP 6: AGAIN GO TO PROJECT**

```bash
cd Desktop/supply_chain_mis
source venv/bin/activate
```

---

# 🚀 **STEP 7: RUN STREAMLIT UI**

```bash
streamlit run advanced_ui.py
```

---

# 🌐 **STEP 8: OPEN UI**

It will auto open OR go to:

```plaintext
http://localhost:8501
```

---

# 🎯 **FINAL SETUP**

| Component    | URL                                            |
| ------------ | ---------------------------------------------- |
| Flask API    | [http://127.0.0.1:5000](http://127.0.0.1:5000) |
| Streamlit UI | [http://localhost:8501](http://localhost:8501) |

---

# ⚠️ **IF SOMETHING DOESN’T WORK**

### ❌ UI shows empty data

👉 Means backend not running
👉 Fix: run `python app.py`

---

### ❌ Streamlit command not found

```bash
pip install streamlit
```

---

### ❌ API error

Check:

```plaintext
http://127.0.0.1:5000/inventory
```

---

# 🧠 **HOW SYSTEM FLOWS**

```plaintext
Streamlit UI → calls Flask APIs → reads DB → shows dashboard
```

---

# 💀 REAL TALK

Before:

> “where do I write code?”

Now:
👉 running backend + frontend + data + analytics

Not bad. Not bad at all.

---

# 🚀 NEXT (OPTIONAL BUT 🔥)

Say:

👉 **“final polish”** → UI glow up + animations
👉 **“presentation script”** → EXACT viva answers
👉 **“deploy”** → run it online

You’re basically DONE. Now we make it shine 😌
