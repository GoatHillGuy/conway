#!/usr/bin/env python3
import cgol
import plaintext


def test_grid():
    g = cgol.Grid()
    assert g.get(1, 1) == 0

    g.set(1, 2, 1)
    assert g.count_neighbours(1, 1, 3) == 1
    # State:
    #   0 0 0
    #   0 0 0
    #   0 X 0
    assert g.get(1, 2) == 1
    assert g.count_neighbours(1, 2, 3) == 0


def test_getset():
    g = cgol.Grid()
    assert not g.get(1, 1)

    g.set(1, 2, 1)

    assert g.get(1, 2) == 1


def test_rules():
    g = cgol.Grid()

    g.set(1, 0, 1)
    g.set(1, 1, 1)
    g.set(1, 2, 1)
    g2 = cgol.conwayslife(g, 3)

    assert g2.get(0, 1) == 1
    assert g2.get(1, 1) == 1
    assert g2.get(2, 1) == 1


def test_ccoords():
    g = cgol.Grid()
    r_pos1 = g.ccoords((0, 0), 10)
    r_pos2 = g.ccoords((30, 30), 10)
    r_pos3 = g.ccoords((0, 30), 10)
    r_pos4 = g.ccoords((30, 0), 10)
    r_pos5 = g.ccoords((0, 20), 10)
    r_pos6 = g.ccoords((20, 10), 10)
    r_pos7 = g.ccoords((25, 15), 10)
    r_pos8 = g.ccoords((5, 5), 10)

    assert r_pos1 == (0, 0)
    assert r_pos2 == (3, 3)
    assert r_pos3 == (0, 3)
    assert r_pos4 == (3, 0)
    assert r_pos5 == (0, 2)
    assert r_pos6 == (2, 1)
    assert r_pos7 == (2, 1)
    assert r_pos8 == (0, 0)


def test_read_plaintext():
    g1 = cgol.Grid([
        [0, 0, 1],
        [0, 0, 0],
        [0, 1, 0]
    ])

    g1_pt = """
        !Name: Test bro >:)
        !
        ..O
        ...
        .O.
    """

    assert g1 == plaintext.read_plaintext(g1_pt)

    g2 = cgol.Grid([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])

    g2_pt = """
        !Name: Test bro >:)
        !
    """

    assert g2 == plaintext.read_plaintext(g2_pt)

    g3 = cgol.Grid([
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ])

    g3_pt = """
        !Name: Test bro >:)
        !
        O.O
        ...
        O.O
    """

    assert g3 == plaintext.read_plaintext(g3_pt)

    g4 = cgol.Grid([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])

    g4_pt = """
        !Name: Test bro >:)
        !
        OOO
        OOO
        OOO
    """

    assert g4 == plaintext.read_plaintext(g4_pt)

    g5 = cgol.Grid([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])

    g5_pt = """
        ...
        ...
        ...
    """

    assert g5 == plaintext.read_plaintext(g5_pt)


def test_pan():
    v1 = cgol.View(3, 1, 1)
    v1.pan(5, 1, 0)
    assert v1.x == 2
    assert v1.y == 1

    v2 = cgol.View(3, 1, 1)
    v2.pan(5, -1, 0)
    assert v2.x == 0
    assert v2.y == 1

    v3 = cgol.View(3, 1, 1)
    v3.pan(5, 0, -1)
    assert v3.x == 1
    assert v3.y == 0

    v4 = cgol.View(3, 1, 1)
    v4.pan(5, 0, 1)
    assert v4.x == 1
    assert v4.y == 2

    v5 = cgol.View(3, 1, 1)
    v5.pan(5, 1, -5)
    assert v5.x == 2
    assert v5.y == 0

    v6 = cgol.View(3, 1, 1)
    v6.pan(5, -1, -1)
    assert v6.x == 0
    assert v6.y == 0

    v7 = cgol.View(3, 1, 1)
    v7.pan(5, 10, 2)
    assert v7.x == 2
    assert v7.y == 2

    v8 = cgol.View(3, 1, 1)
    v8.pan(5, -2, 1)
    assert v8.x == 0
    assert v8.y == 2

def test_zoom():
    v1 = cgol.View(3, 1, 1)
    v1.zoom(5, 4/3)
    assert v1.view_size == 4

    v1 = cgol.View(3, 1, 1)
    v1.zoom(5, 4/3)
    assert v1.view_size == 4

    v2 = cgol.View(3, 1, 1)
    v2.zoom(5, 2/3)
    assert v2.view_size == 2

    v3 = cgol.View(3, 1, 1)
    v3.zoom(5, 5/3)
    assert v3.view_size == 5
    assert v3.x == 0
    assert v3.y == 0

    v4 = cgol.View(3, 0, 2)
    v4.zoom(5, 4/3)
    assert v4.view_size == 4
    assert v4.x == 0
    assert v4.y == 1
