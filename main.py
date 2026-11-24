import os

# The funniest toaster error message: one line, under 120 characters.
# Setup is a real toaster failure (the lever sticks); the laugh is the
# betrayal — the toaster sides with the toast against its owner.
LINE = "Error: lever stuck. Your toast has chosen to stay. I support its decision."

# Gate self-check: the sealed scorer requires UTF-8 text of 1-120
# characters, not only whitespace. Fail loudly here rather than ship
# an entry the gate would refuse.
assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
