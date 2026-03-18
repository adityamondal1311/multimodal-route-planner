from flask import Flask, request, jsonify
from graph import load_graph
from algorithms import dijkstra, astar

app = Flask(__name__)
G = load_graph()


@app.route("/route")
def route():

    start = request.args.get("start")
    end = request.args.get("end")
    algo = request.args.get("algo", "dijkstra")

    if algo == "astar":
        path = astar(G, start, end)
    else:
        path = dijkstra(G, start, end)

    return jsonify({
        "path": path
    })


if __name__ == "__main__":
    app.run(debug=True)