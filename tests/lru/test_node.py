from betbright.lru import Node


def test_can_create_list_head():
    head = Node.make_head()
    assert head.next == head
    assert head.prev == head
    assert head.key is None
    assert head.value is None


def test_can_create_list_node():
    node = Node(key=42, value='spam')
    assert node.key == 42
    assert node.value == 'spam'
    assert node.next is None
    assert node.prev is None
    assert repr(node) == 'Node(42, spam)'


def test_can_push_into_list():
    head = Node.make_head()
    n1 = head.push(key=42, value='spam')
    n2 = head.push(key=32, value='eggs')
    n3 = head.push(key=22, value='albatroz')

    assert head.next == n1
    assert head.prev == n3
    assert head.key is None
    assert head.value is None

    assert n1.next == n2
    assert n1.prev == head
    assert n1.key == 42
    assert n1.value == 'spam'

    assert n2.next == n3
    assert n2.prev == n1
    assert n2.key == 32
    assert n2.value == 'eggs'

    assert n3.next == head
    assert n3.prev == n2
    assert n3.key == 22
    assert n3.value == 'albatroz'


def test_can_pop_last_item():
    head = Node.make_head()
    n1 = head.push(key=42, value='spam')
    n2 = head.push(key=32, value='eggs')
    n3 = head.push(key=22, value='albatroz')

    popped = head.pop()
    assert n1 == popped

    assert head.next == n2
    assert head.prev == n3
    assert head.key is None
    assert head.value is None

    assert n2.next == n3
    assert n2.prev == head
    assert n2.key == 32
    assert n2.value == 'eggs'

    assert n3.next == head
    assert n3.prev == n2
    assert n3.key == 22
    assert n3.value == 'albatroz'


def test_can_move_node_to_start():
    head = Node.make_head()
    n1 = head.push(key=42, value='spam')
    n2 = head.push(key=32, value='eggs')
    n3 = head.push(key=22, value='albatroz')
    head.move_node_to_start(n1)

    assert head.next == n2
    assert head.prev == n1
    assert head.key is None
    assert head.value is None

    assert n1.next == head
    assert n1.prev == n3
    assert n1.key == 42
    assert n1.value == 'spam'

    assert n2.next == n3
    assert n2.prev == head
    assert n2.key == 32
    assert n2.value == 'eggs'

    assert n3.next == n1
    assert n3.prev == n2
    assert n3.key == 22
    assert n3.value == 'albatroz'
