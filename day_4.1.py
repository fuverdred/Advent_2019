L = 265275
U = 781584
part_1 = [str(i) for i in range(L, U)
          if len(set(str(i))) < 6 and
          str(i) == ''.join(sorted(list(str(i))))]
print(f'Part 1: No. possible passwords {len(part_1)}')
part_2 = [i for i in part_1 if
          2 in [i.count(c) for c in set(i)]]
print(f'Part 1: No. possible passwords {len(part_2)}')
