import math
import sys


def numMatches(n):
    n = int(n)
    prev_root = math.floor(math.sqrt(n-1))
    next_root = math.ceil(math.sqrt(n))

    prev_square = prev_root**2
    next_square = next_root**2

    # base case
    if n == 1:
        return 4
    else:
        diff = n - prev_square
        sqdiff = next_square - prev_square
        halfseq = (sqdiff - 1)/2

        matches = num_matches(prev_root)  # + 2 * diff + (diff < halfseq) ? 1:2

        if diff <= halfseq:
            matches += 1 + 2 * diff
        else:
            matches += 2 + 2 * diff

    return matches


def main():
    n = sys.argv[1]
    print(numMatches(n))


main()



