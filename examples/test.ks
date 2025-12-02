print:'--- STARTING SYSTEM TEST ---'

# TEST 1: Mathematics & PEMDAS
# Expectation: 5 + 10 = 15, then * 2 = 30.
# If PEMDAS works: 10 * 2 = 20, then + 5 = 25.
print:'Test 1: Math (5 + 10 * 2)'
res = 5 + 10 * 2
print:res

if: res = 25 do:
    print:'[PASS] Math works correctly.'

if: res = 30 do:
    print:'[FAIL] Math order is wrong.'

# TEST 2: Nested Logic
print:' '
print:'Test 2: Logic'
val = 100

if: val > 50 do:
    if: val < 200 do:
        print:'[PASS] Nested If-Statements work.'

# TEST 3: Functions
print:' '
print:'Test 3: Functions'

def: sub_task do:
    print:'[PASS] Function executed successfully.'

run: sub_task

print:' '
print:'--- ALL TESTS COMPLETED ---'