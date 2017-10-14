"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""
import Queue
import heapq
import json

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"


def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response

def BFS(start_id, finish_id):

    # print('neighbor loop')
    # for neighbor in get_state(start_id)['neighbors']:
    #     print neighbor['location']['name']


    queue = Queue.Queue()
    visited = []
    trail = []
    # visited = {}

    queue.put(get_state(start_id)['id'])

    while not queue.empty():
        current = queue.get()

        destination = get_state(finish_id)['id']

        if current is destination:
            trail.append(current)
            print('DESTINATION FOUND')
            break

        if not current in visited:
        #     visited[current] = True
            print ('not in list: ', current)
            visited.append(current)

            for neighbor in get_state(current)['neighbors']:
                queue.put(neighbor['id'])

    print ('VISiTED PRINT:', visited)
    result = []

    pass

def Dijkstra(art_id, finish_id):
    print (start_id, finish_id)

if __name__ == "__main__":
    # Your code starts here
    print("BFS Path")


    print("Dijkstra Path")

    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    # print(empty_room)

    end_room = get_state('f1f131f647621a4be7c71292e79613f9')
    # print(end_room)

    BFS('7f3dc077574c013d98b2de8f735058b4', 'f1f131f647621a4be7c71292e79613f9')

    # print (transition_state('7f3dc077574c013d98b2de8f735058b4', '44dfaae131fa9d0a541c3eb790b57b00'))
    # print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))

