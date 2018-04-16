import itertools

perm_cache = dict()
next_perm_cache = dict()
generated_cache = dict()


def check_permutation(nr1, nr2):
    return [i for i in sorted(str(nr1))] == [j for j in sorted(str(nr2))] and nr1 != nr2


def next_perm_over(nr):
    if nr in next_perm_cache:
        return next_perm_cache[nr]
    cache = 0
    nr_str = str(nr)
    nr_ll = len(str(nr))
    if nr_ll==1:
        return int(nr_str+"0")
    nr_last = nr_str[-1]
    index = -2
    while index > -len(nr_str) and nr_last >= nr_str[index]:
        if nr_last > nr_str[index]:
            # print("\t\tYes")
            cache = int(str(nr_str[:index]) + nr_last + str(nr_str[index]) + str(nr_str[nr_ll + index + 2:nr_ll]))
            next_perm_cache[nr] = cache
            return cache
        else:
            index -= 1
    digit_count = {str(x): 0 for x in range(10)}
    for s in nr_str:
        digit_count[s] += 1
    index = -1
    while not nr_str[index - 1] < nr_str[index]:
        index -= 1
        if -index == nr_ll:
            break
    index -= 1
    if -index <= nr_ll:
        popped = []
        for i in range(1, -index):
            popped += nr_str[-1]
            nr_str = nr_str[:-1]
        before = nr_str[-1]
        after = str(min([int(i) for i in popped if i > before]))
        popped.remove(after)
        popped.append(before)
        nr_str = nr_str[:-1] + after + "".join(sorted(popped))
        # print("\t\tYeah ", index+1)
        cache = int(nr_str)
        next_perm_cache[nr] = cache
        return cache
    # print("\t\tNEXT")
    next_ll = list(str(int("".join(sorted(nr_str)))))
    while len(next_ll) <= len(nr_str):
        next_ll.insert(1, "0")
    cache = int("".join(next_ll))
    next_perm_cache[nr] = cache
    return cache


def all_perm_over(nr, lower=None, in_lenght=None):
    if show_generation_progress:
        print("\t\t\tGENERATING ALL PERMUTATIONS LOWER THAN {} FOR {}".format(lower, nr))
    ll = len(str(nr))
    if lower is None:
        lower = int("9" * (ll + 1))
    if in_lenght is None:
        in_lenght = ll
    to_return = []
    while len(str(nr)) <= in_lenght and nr < lower:
        nr = next_perm_over(nr)
        if nr != 0:
            to_return += [nr]
    return to_return


def digit_perms(nr, stop_at=None):
    if nr in perm_cache:
        return perm_cache[nr]
    if nr == 10 ** (len(str(nr)) - 1):
        return [nr]
    ll = len(str(nr))
    adempt = list(str(int("".join(sorted(str(nr))))))
    while len(adempt) < ll:
        adempt.insert(1, "0")

    nr = int("".join(adempt))
    original = nr
    ll = len(str(original))
    perm_cache[original] = [nr]
    while True:
        nr = next_perm_over(nr)
        if len(str(nr)) > ll:
            break
        if stop_at is not None:
            if nr > stop_at:
                break
        perm_cache[original] += [nr]
    if show_generation_progress:
        print("\t\tRETURNING {}".format(perm_cache[original]))
    return perm_cache[original]


# import time
# start_nr = 13
# # start = time.time()
# # test_against = [i for i in sorted(digit_perms(start_nr)) if i >= start_nr]
# # print(test_against)
# # end = time.time() - start
# # print(end)
# start = time.time()
# aa = start_nr
# print(aa)
# correctness = True
# index = 1
# while True:
#     aa = next_perm_over(aa)
#     if len(str(aa)) > len(str(start_nr))+2:
#         break
#     #if aa != test_against[index]:
#     #   correctness = False
#     #print("\t\t", time.time() - start)
#     print(aa)
#     index += 1
# print(time.time() - start)
# #print(end)
# print(correctness)


def sum_all_digits(nr):
    ss = 0
    while nr > 0:
        ss += nr % 10
        nr //= 10
    return ss


def generate_candidates(sod, len_req):
    try:
        if (sod, len_req) in generated_cache and sod != 0:
            to_return = generated_cache[(sod, len_req)]
            min_len_returned = min([len(str(i)) for i in generated_cache[(sod, len_req)]])
            return to_return, min_len_returned
    except ValueError:
        pass
    to_return = []
    for i in range(sod // 9 + 1):
        if i > len_req:
            break
        for h in range(sod // 8 + 1 - i):
            if i + h > len_req:
                break
            for g in range(sod // 7 + 1 - i - h):
                if i + h + g > len_req:
                    break
                for f in range(sod // 6 + 1 - i - h - g):
                    if i + h + g + f > len_req:
                        break
                    for e in range(sod // 5 + 1 - i - h - g - f):
                        if i + h + g + f + e > len_req:
                            break
                        for d in range(sod // 4 + 1 - i - h - g - f - e):
                            if i + h + g + f + e + d > len_req:
                                break
                            for c in range(sod // 3 + 1 - i - h - g - f - e - d):
                                if i + h + g + f + e + d + c > len_req:
                                    break
                                for b in range(sod // 2 + 1 - i - h - g - f - e - d - c):
                                    if i + h + g + f + e + d + c + b > len_req:
                                        break
                                    for a in range(sod + 1 - i - h - g - f - e - d - c - b):
                                        if i + h + g + f + e + d + c + b + a > len_req:
                                            break
                                        try:
                                            to_return.append(int("1" * a + "2" * b + "3" * c + "4" * d
                                                                 + "5" * e + "6" * f + "7" * g + "8" * h + "9" * i))
                                            if show_generation_progress:
                                                print("GENERATED: " + "1" * a + "2" * b + "3" * c + "4" * d
                                                      + "5" * e + "6" * f + "7" * g + "8" * h + "9" * i)
                                        except ValueError:
                                            continue

    cc = to_return[:]
    for i in cc:
        if sum_all_digits(i) != sod:
            to_return.remove(i)
    min_len_returned = min([len(str(i)) for i in to_return] + [sod])
    if debug:
        print("\tMIN LEN RETURNED = {}".format(str(min_len_returned)))
        print("\tRETURNED: {}".format(str(to_return)))
    generated_cache[(sod, len_req)] = to_return
    return to_return, min_len_returned


def build_first(sod):
    if debug2:
        print("Build first entered with {}".format(sod))
    i = sod // 9
    h = (sod - i * 9) // 8
    g = (sod - i * 9 - h * 8) // 7
    f = (sod - i * 9 - h * 8 - g * 7) // 6
    e = (sod - i * 9 - h * 8 - g * 7 - f * 6) // 5
    d = (sod - i * 9 - h * 8 - g * 7 - f * 6 - e * 5) // 4
    c = (sod - i * 9 - h * 8 - g * 7 - f * 6 - e * 5 - d * 4) // 3
    b = (sod - i * 9 - h * 8 - g * 7 - f * 6 - e * 5 - d * 4 - c * 3) // 2
    a = (sod - i * 9 - h * 8 - g * 7 - f * 6 - e * 5 - d * 4 - c * 3 - b * 2)
    try:
        if show_generation_progress or True:
            print("BUILD FIRST: " + str(
                int("1" * a + "2" * b + "3" * c + "4" * d + "5" * e + "6" * f + "7" * g + "8" * h + "9" * i)))
        return int("1" * a + "2" * b + "3" * c + "4" * d + "5" * e + "6" * f + "7" * g + "8" * h + "9" * i)
    except ValueError:
        if debug2:
            print("BUILD FIRST: None")
        return None

def generate_mask(ll):
    if ll==1:
        return {(0)}
    if ll==2:
        return {(x,-x) for x in range(10)}.union({(-x,x) for x in range(1,10)})
    use_mask = generate_mask(ll-1)
    to_return = []
    for m in use_mask:
        mm = list(m[:])
        nn = list(m[:])
        for i in range(10):
            mm[-1] += i
            nn[-1] -= i
            to_return += [a for a in itertools.permutations(mm+[-i])] + [b for b in itertools.permutations(nn+[i])]
    to_return = sorted(set(to_return))
    for t in to_return[:]:
        ss = 0
        for s in t:
            if abs(s)>9:
                to_return.remove(t)
                break
            ss += s
        if ss!=0:
            if t in to_return:
                to_return.remove(t)
    return to_return

#print(generate_mask(4))




# all_bb = [10, 7, 6, 5, 9, 7, 4, 2, 10, 10, 6, 10, 5, 9, 9, 4, 8, 8, 5, 7, 8, 10, 9, 4, 5, 3, 8, 3, 8, 8, 2, 3, 7, 3, 8,
#           10, 6, 4, 6, 9, 7, 7, 4, 1, 2, 4, 1, 4, 10, 10, 7, 3, 8, 8, 6, 1, 2, 5, 6, 2, 1, 4, 3, 8, 6, 7, 1, 7, 7, 1, 8,
#           7, 4, 1, 9, 7, 2, 2, 5, 5, 9, 10, 1, 6, 7, 4, 8, 1, 10, 4, 4, 7, 2, 6, 7, 5, 1, 8, 1, 2, 1, 2, 10, 9, 3, 4, 9,
#           5, 9, 2, 6, 6, 5, 1, 1, 5, 1, 6, 9, 10, 6, 5, 9, 7, 7, 1, 1, 7, 10, 9, 4, 8, 10, 1, 6, 6, 3, 4, 9, 5, 3, 4, 4,
#           3, 6, 1, 7, 10, 5, 6, 10, 1, 6, 9, 3, 1, 2, 3, 10, 6, 10, 7, 7]
# all_bb = [18 for i in range(100)]
all_bb = [84, 60, 61, 97, 92, 53, 100, 77, 54, 59, 57, 55, 90, 83, 66, 97, 82, 63, 59, 71, 74, 81, 58, 79, 82, 66, 83,
          95, 73, 57, 90, 63, 80, 62, 58, 87, 72, 53, 81, 98, 85, 66, 68, 64, 70, 71, 56, 83, 70, 50, 52, 94, 74, 64,
          55, 65, 91, 68, 99, 68, 70, 64, 95, 74, 53, 93, 58, 66, 82, 76, 82, 68, 85, 55, 70, 98, 66, 92, 76, 59, 61,
          83, 82, 94, 57, 54, 86, 100, 62, 89, 60, 57, 92, 50, 77, 61, 99, 76, 57, 59, 50, 77, 59, 57, 56, 100, 66, 62,
          88, 71, 94, 88, 83, 81, 65, 69, 69, 75, 76, 54, 79, 82, 80, 87, 86, 70]
# all_bb = [8, 8, 5, 1, 2, 7, 3, 8, 9, 4]
all_bb = [300 for i in range(300)]
#all_bb = []
for a in range(int(input())):
    all_bb.append(int(input()))
debug, debug2, show_bbs, timer, show_generation_progress, show_builds = True, True, True, False, False, False
# debug, debug2, show_bbs, timer, show_generation_progress, show_builds = False, False, False, False, False, False
timer = True
if debug or timer:
    import time

    start = time.time()
aa = 1
last_output = dict()
last_bb = 0
index_bb = 0

for bb in all_bb:
    index_bb += 1
    if debug or show_bbs:
        print("{}. USING {} AS BB".format(index_bb, bb))
    if sum_all_digits(aa + 1) == bb:
        aa += 1
        print(aa)
        continue

    try_aa = build_first(bb)
    if show_builds:
        print("\t\tFIRST BUILT {}".format(try_aa))
    if try_aa > aa:
        if debug:
            print("\t\tFIRST BUILT {}".format(try_aa))
        aa = try_aa
        print(aa)
        continue

    current_sod = sum_all_digits(aa)
    if current_sod<bb:
        less_aa = aa + 1
        less_current_sod = sum_all_digits(less_aa)



    ll = len(str(aa))
    while True:
        candidates, min_ll = generate_candidates(bb, ll)
        accepted = [int(str(i).ljust(ll,"0")) for i in candidates]
        permutations = sorted(accepted[:])
        if debug:
            print("\t\tGOING TO GET PERMUTATIONS FOR:\n\t\t{}".format(permutations))
        if len(permutations)>0:
            maximum = permutations[-1]
            for i in permutations[:]:
                permutations = sorted(set(permutations + digit_perms(i, maximum)))
            if debug:
                print("\t\tGOT PERMUTATIONS:\n\t\t{}".format(permutations))

        possibles = sorted([i for i in permutations if i > aa])
        if len(possibles) > 0:
            aa = possibles[0]
            break
        ll += 1

    print(aa)

if debug or timer:
    end = time.time()
    print(str(end - start))
