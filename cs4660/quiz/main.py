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

    queue = Queue.Queue()
    visited = []
    trail = []
    came_from = {}

    queue.put(get_state(start_id)['id'])
    came_from[get_state(start_id)['id']] = None

    destination = get_state(finish_id)['id']

    while not queue.empty():
        current = queue.get()

        if current is destination:
            trail.append(current)
            print('DESTINATION FOUND')
            break

        if not current in visited:
            print ('checking room: {}'.format(current))
            visited.append(current)

            for neighbor in get_state(current)['neighbors']:
                if not neighbor['id'] in visited:
                    queue.put(neighbor['id'])
                    came_from[neighbor['id']] = current

    current = get_state(finish_id)['id']
    begin = get_state(start_id)['id']


    while not came_from[current] is None:
        trail.append(current)
        current = came_from[current]

    trail.append(begin)
    trail.reverse()


    for i, nexti in zip(trail, trail[1::]):
        print transition_state(i, nexti)

    return trail


def Dijkstra(start_id, finish_id):

    begin = get_state(start_id)['id']
    destination = get_state(finish_id)['id']

    heap = []
    heapq.heappush(heap, (0, begin))
    trail = []

    came_from = {}
    cost_so_far = {}

    came_from[begin] = None
    cost_so_far[begin] = 0

    while not heap == []:
        current = heapq.heappop(heap)

        print ('checking room: {}'.format(current))

        if current[-1] == destination:
            break

        for neighbor in get_state(current[-1])['neighbors']:
            new_cost = cost_so_far[current[-1]] + transition_state(current[-1], neighbor['id'])['event']['effect']
            # temp = transition_state(current[-1], neighbor['id'])['event']['effect']

            if neighbor['id'] not in cost_so_far or new_cost > cost_so_far[neighbor['id']]:
                if neighbor['id'] not in cost_so_far:
                    cost_so_far[neighbor['id']] = new_cost
                    priority = -new_cost
                    print (priority, neighbor['id'])
                    heapq.heappush(heap, (priority, neighbor['id']))
                    came_from[neighbor['id']] = current[-1]

    result = []

    current = destination

    print ('came from path')
    trail.append(current)
    while came_from[current] is not begin:
        trail.append(came_from[current])
        current = came_from[current]

    trail.append(begin)

    trail.reverse()

    for i, nexti in zip(trail, trail[1::]):
        print transition_state(i, nexti)

    return trail

if __name__ == "__main__":
    # Your code starts here

    end_room = get_state('f1f131f647621a4be7c71292e79613f9')

    print('BFS path: {}'.format(BFS('7f3dc077574c013d98b2de8f735058b4', 'f1f131f647621a4be7c71292e79613f9')))

    print('Dijkstra path: {}'.format(Dijkstra('7f3dc077574c013d98b2de8f735058b4', 'f1f131f647621a4be7c71292e79613f9')))


