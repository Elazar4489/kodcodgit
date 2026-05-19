import copy


def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")


# =====================================================================
# 1. LIST DEMO (With Nested List)
# =====================================================================
print_separator("LIST DEMO")

# We use a nested list [2, 3] to show how shallow vs deep copy handle inner objects
a = [1, [2, 3]]
b = a
c = a.copy()  # Shallow copy
d = copy.deepcopy(a)  # Deep copy

print(f"Original (a)        : {a} | ID: {hex(id(a))} | Inner ID: {hex(id(a[1]))}")
print(f"Assignment (b)      : {b} | ID: {hex(id(b))} | Inner ID: {hex(id(b[1]))}")
print(f"Shallow Copy (c)    : {c} | ID: {hex(id(c))} | Inner ID: {hex(id(c[1]))}")
print(f"Deep Copy (d)       : {d} | ID: {hex(id(d))} | Inner ID: {hex(id(d[1]))}")

print("\n--- Making a change to the nested item: a[1][0] = 'X' ---")
a[1][0] = "X"

print(f"Original (a)        : {a}")
print(f"Assignment (b)      : {b}  <- Changed (Shares 100% same memory)")
print(
    f"Shallow Copy (c)    : {c}  <- Changed! (Outer wrapper is new, but inner items still point to original)"
)
print(f"Deep Copy (d)       : {d}  <- Safe! (Entirely independent clone)")


# =====================================================================
# 2. DICTIONARY DEMO (With Nested Dictionary)
# =====================================================================
print_separator("DICTIONARY DEMO")

a_dict = {"items": [4, 5], "status": "active"}
b_dict = a_dict
c_dict = a_dict.copy()
d_dict = copy.deepcopy(a_dict)

print(
    f"Original (a)        : {a_dict} | ID: {hex(id(a_dict))} | Inner ID: {hex(id(a_dict['items']))}"
)
print(
    f"Assignment (b)      : {b_dict} | ID: {hex(id(b_dict))} | Inner ID: {hex(id(b_dict['items']))}"
)
print(
    f"Shallow Copy (c)    : {c_dict} | ID: {hex(id(c_dict))} | Inner ID: {hex(id(c_dict['items']))}"
)
print(
    f"Deep Copy (d)       : {d_dict} | ID: {hex(id(d_dict))} | Inner ID: {hex(id(d_dict['items']))}"
)

print("\n--- Making a change to the nested item: a_dict['items'][0] = 'Y' ---")
a_dict["items"][0] = "Y"

print(f"Original (a)        : {a_dict}")
print(f"Assignment (b)      : {b_dict}")
print(f"Shallow Copy (c)    : {c_dict}  <- Changed!")
print(f"Deep Copy (d)       : {d_dict}  <- Safe!")


# =====================================================================
# 3. SET DEMO
# =====================================================================
print_separator("SET DEMO")
# Note: Sets cannot contain mutable items (like lists or dicts),
# so shallow vs deep copy behave identically on standard sets.
# However, the ID rules for the container itself still apply!

a_set = {6, 7, 8}
b_set = a_set
c_set = a_set.copy()
d_set = copy.deepcopy(a_set)

print(f"Original (a)        : {a_set} | ID: {hex(id(a_set))}")
print(f"Assignment (b)      : {b_set} | ID: {hex(id(b_set))}")
print(f"Shallow Copy (c)    : {c_set} | ID: {hex(id(c_set))}")
print(f"Deep Copy (d)       : {d_set} | ID: {hex(id(d_set))}")

print("\n--- Adding an item to the original set: a_set.add(9) ---")
a_set.add(9)

print(f"Original (a)        : {a_set}")
print(f"Assignment (b)      : {b_set}  <- Changed")
print(f"Shallow Copy (c)    : {c_set}  <- Safe (New outer object)")
print(f"Deep Copy (d)       : {d_set}  <- Safe (New outer object)")