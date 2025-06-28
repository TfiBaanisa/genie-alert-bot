from flask import Flask
from telegram import send_alert
from strategies import run_all_strategies
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Genie Alert Bot is running!"

def schedule_runner():
    while True:
        print("🔁 Running all strategies...")
        messages = run_all_strategies()
        for msg in messages:
            send_alert(msg)
        time.sleep(300)  # Run every 5 minutes

threading.Thread(target=schedule_runner, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)