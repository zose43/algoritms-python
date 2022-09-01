import string
from collections import deque

# search in width
graph = {
    'me': ['Bob', 'Alissa', 'Clair'],
    'Bob': ['Peggi', 'Anuge'],
    'Clair': ['Tommy', 'Jonny'],
    'Alissa': ['Peggi'],
    'Peggi': ['Gvidom'],
    'Gvidom': [],
    'Tommy': [],
    'Jonny': [],
    'Anuge': []
}


def is_seller(person: string) -> bool:
    return person[-1] == 'm'


def search(person: string) -> bool:
    search_deque = deque()
    searched = [person]
    search_deque += graph[person]
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if is_seller(person):
                print('seller find!')
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    print('no one')
    return False


def main():
    search('me')


if __name__ == '__main__':
    main()
