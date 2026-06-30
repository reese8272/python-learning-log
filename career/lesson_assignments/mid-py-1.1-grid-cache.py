"""
BUILD — "Value object as a cache key" (Mid-Python Prep §1.1, build-before-bank)
Pairs with: mid-py-1.1-data-model.py  |  Concept: __eq__/__hash__ contract, FOR REAL

────────────────────────────────────────────────────────────────────────────
WHY THIS BUILD EXISTS
────────────────────────────────────────────────────────────────────────────
The worksheet PROVED you understand the __eq__/__hash__ contract. This banks it:
the contract doing real work in your actual job's domain.

The job = "high-performance FastAPI serving weather datasets." The first lever
you reach for is a read-cache. But a cache is just a dict — and a dict can only
return a cached value if a NEW request object hashes/compares EQUAL to the one
you stored under. Two requests for the same lat/lon must be the SAME key.

That is exactly __eq__ + __hash__. Get it right -> repeat lookups HIT the cache.
Get it wrong (the default, identity-based) -> every request is a fresh object,
nothing ever matches, and the cache silently thrashes (0% hit rate). The contract
isn't academic here; it's the difference between a cache that works and one that
quietly does nothing.

────────────────────────────────────────────────────────────────────────────
YOUR JOB
────────────────────────────────────────────────────────────────────────────
Write the GridCell value object below — __init__, __eq__, __hash__ — so that two
GridCells with the same (lat, lon) are equal AND hash equal. The cache and the
scenario are already written. Run it; green means your value object makes the
cache actually cache.

  Run:  python mid-py-1.1-grid-cache.py

Struggle-first: write it cold from what you owned in the worksheet. No peeking
back at the worksheet's GridPoint unless you're truly stuck for 10 min.
"""


# ─── YOU WRITE THIS ─────────────────────────────────────────────────────────
# A GridCell is a point on the weather grid, identified BY VALUE: two cells with
# the same lat/lon ARE the same cell, even if they're different objects. Make it
# usable as a dict key so the cache can find it again.
#
# TODO: implement __init__(lat, lon), __eq__, and __hash__ so that equal cells
#       compare equal and hash equal (hash the SAME fields you compare on).

class GridCell:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return isinstance(other, GridCell) and (self.lat == other.lat and self.lon == other.lon)
    
    def __hash__(self):
        return hash((self.lat, self.lon))


# ─── GIVEN — the cache (don't change this) ──────────────────────────────────
# A dead-simple read-through cache. It counts hits and misses so you can SEE
# whether your value object is doing its job.

class WeatherCache:
    def __init__(self, fetch):
        self._fetch = fetch          # the "expensive" data source, called on a miss
        self._store = {}             # GridCell -> forecast value
        self.hits = 0
        self.misses = 0

    def get(self, cell: "GridCell"):
        if cell in self._store:      # <- this membership test IS __hash__ + __eq__
            self.hits += 1
            return self._store[cell]
        self.misses += 1
        value = self._fetch(cell)
        self._store[cell] = value
        return value


# ─── GIVEN — the scenario + red/green check ─────────────────────────────────
def _run():
    fetch_calls = []

    def expensive_fetch(cell):       # pretend this hits S3 / reads a GRIB file
        fetch_calls.append(cell)
        return f"forecast@{cell.lat},{cell.lon}"

    cache = WeatherCache(expensive_fetch)

    # Two SEPARATE requests for the SAME cell (as if two API calls came in).
    a = cache.get(GridCell(40.0, -80.0))
    b = cache.get(GridCell(40.0, -80.0))      # different object, same value
    # A different cell — must NOT collide with the first.
    c = cache.get(GridCell(41.0, -80.0))

    checks = [
        ("same-cell second request HITS the cache", cache.hits == 1),
        ("expensive fetch ran only for the 2 distinct cells", len(fetch_calls) == 2),
        ("cache returned the same value for the same cell", a == b),
        ("distinct cells are distinct keys", cache.misses == 2),
        ("equal cells dedupe in a set", len({GridCell(40.0, -80.0),
                                             GridCell(40.0, -80.0)}) == 1),
    ]

    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'} — {name}")

    passed = sum(1 for _, ok in checks if ok)
    print(f"\n{passed}/{len(checks)} green.",
          "Build banked — §1.1 owned." if passed == len(checks)
          else "Not yet — your GridCell isn't honoring the contract.")


if __name__ == "__main__":
    _run()
