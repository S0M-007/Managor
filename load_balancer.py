from flask import Flask, redirect
import random

app = Flask(__name__)

# List of available edge servers (adjust as needed)
edge_servers = ['http://localhost:5001', 'http://localhost:5002', 'http://localhost:5003']

@app.route('/')
def load_balancer():
    # Randomly select an edge server
    selected_server = random.choice(edge_servers)
    return redirect(selected_server)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
