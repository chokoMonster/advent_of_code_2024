"""
def find_patterns_1_1(d, p):
    if d in p:
        return True

    for i in reversed(range(1, len(d))):
        if d[0:i] in p:
            if find_patterns_1_1(d[i:], p):
                return True

    return False


def find_patterns_1_2(d, pat):
    if d in pat:
        return True

    possible_patterns = [p for p in pat if d.startswith(p)]

    for pp in possible_patterns:
        if find_patterns_1_2(d[len(pp):], pat):
            return True

    return False
"""

found_matches = {}

def find_patterns(d, pat):
    if d in pat:
        return True
    if d in found_matches:
        return found_matches[d]

    possible_patterns = [p for p in pat if d.startswith(p)]

    found = False
    for pp in possible_patterns:
        if find_patterns(d[len(pp):], pat):
            found = True

    found_matches[d] = found
    return found

def find_patterns_2(d, pat):
    if len(d) == 0:
        return 1

    if d in found_matches:
        return found_matches[d]

    possible_patterns = [p for p in pat if d.startswith(p)]

    found = 0
    for pp in possible_patterns:
        found += find_patterns_2(d[len(pp):], pat)

    found_matches[d] = found
    return found


if __name__ == "__main__":

    f = open("input/19.txt", "r")
    lines = f.readlines()
    designs = [line.strip() for line in lines]

    pattern_input = 'rrgwru, gwubwg, wgbbw, bwb, ugrgw, uwgguuw, wuggb, bgwb, ubrr, grruuub, rwbwgbub, wwwggg, uuw, gubuu, urwb, bubg, bubb, rruruuu, ubgr, uw, urugg, wubuu, brwb, buw, bgug, wgbwwrb, rwrgrr, gwgr, rrwrg, wwbwgbw, gguu, rgg, bwg, ruurrwg, wbu, ggg, wrw, brbw, wbb, rrbgg, gbb, gwwrubwu, rwgu, grgwwu, wguu, rwg, wbwug, rbur, gwg, wbrugu, wbwwgu, wbbuw, rwrg, rgru, rgb, bwwrg, bwur, rrubwu, gwb, ugwur, wbguwb, rbu, ubrwgw, ruwbr, wbbu, rrbwbg, rgub, rwgb, urwg, bbw, bugg, rugwg, rwbrwww, wuru, guu, brwbg, ug, ruuwruw, bguww, wwrgrurg, rrbgr, uubwurb, brrrwgg, bur, urg, rbg, wruw, gr, ugb, wwrbgrg, wbuuw, bbugu, uug, rrbb, rrbw, bgr, wwwru, rgu, urr, rg, wbgbru, brrgu, gubu, rurgr, wwbrgg, ruurwgwg, rbb, rbrugwb, gwwrbg, bwuuwrg, wu, b, bgwrb, uwggr, rgbb, rww, wgwb, gwgwr, uwbb, uww, gu, ubwuu, wbwwwug, rurwru, rr, rrg, uggr, bgwu, wbgbu, urggw, br, gubgugr, wgrb, bbgrrbu, brbg, wrg, bgrb, rwbwwur, uwr, bubu, grwb, ubb, wr, bbbgwr, bug, uwgwuwu, grb, bgw, uuu, ugr, wgbbgu, gbg, bgwub, urbgrw, rbruwg, gb, bbwgwur, uwbgwrr, ggrb, wbrrwrbu, gbbugrb, ub, rwb, gwr, ruwu, gurgu, rru, uuwwgwuw, bw, ruwbbb, rbgrgu, wuwu, grrugr, wgr, rbbr, rugr, rrrrbww, bwrr, wrbbr, uuwgr, gug, wwb, rgur, brbrr, gguw, grwubrg, rrrr, uwb, wuwwrrwg, gwbggr, rwrub, wuur, gub, rbgb, urrbubrr, uwubu, brbb, bwbr, bww, ruuubwu, ugbbbr, bub, rrug, wub, gruu, uu, bbu, gbbr, urrg, buwu, grw, grbbbu, bgb, ugubg, uwww, urw, wwubruww, buurb, www, bguurr, wwgu, wgb, ruwub, wggggbg, urrb, gbwuw, ubrrg, wrr, gbubgg, gw, wuw, wuug, wwrb, wgg, rgugrru, rgwrbr, guurrg, bgu, rurgb, gwggb, bwgbbw, ggwb, ubwgw, bbg, rbr, wgru, urwr, brr, rgbr, rgr, wwg, guwuru, uuggg, rrw, buu, urb, guwg, ugwwbuwb, rubb, brbuww, rwugru, ubu, wwub, bgwgb, wrug, rug, w, brgg, wwugwruw, ggrwb, bbwuwuu, uub, rrr, ggbrr, wbur, wurbru, wgu, brb, urbbb, gburbww, wbrgruru, rbugr, gubw, wgwgg, rwr, ugw, gggg, gwrwrg, rrub, gbwgg, grg, uwuur, gbwbbb, guw, gbwbb, uwu, ruw, bwr, rwgub, rbw, ggbwr, u, gwu, rrurrb, gwgg, uugwrbr, brw, ugburg, rwu, wwu, wbr, ruwgr, gbwbur, rwgr, rwbww, rbgr, rgbub, rbbuw, ruu, bwgw, bbwg, ubr, gurr, wwr, wwwguu, gbw, ggw, gru, wug, rubwrbrr, wbrrrr, uru, wbgw, wgur, uurgg, bbb, rbwgwbur, wwbwur, bbgubw, gww, brg, ugu, rgrgw, wwrrgugu, rrrwuww, uwwrb, wrb, rrgg, wubgrrb, bwwgrbww, gbr, gwrwu, brgwwbu, urrwub, rbru, bwrgrr, brwuwrb, guuur, wb, bbrb, brww, wuwrww, bu, rgw, rwbwug, bbug, urrgr, bg, bgg, wbgwbgru, wbrru, uwbbr, wbg, gwwur, gur, ubwb, gubbb, bb, wrugr, grur, rb, uwubrg, bwgrw, gbug, g, wuwubgw, ubw, urgu, rrrg, uwg, bbww, uwgrug, ww, ggu, gwbuwu, rgggwgr, wugw, gbrrg, ugg, bwu, ubuur, uurrw, uwwug, bgww, ubg, rw, gwgbwrg, wuu, rbgbg, buwbur, rub, ugbwwrgu, gbww, wbw, gurbwu, bruw, rggrbrgw, wguwu, ubwbwr, ru, uwur, ggb, uurwg, wguubgr, wru, rbrbr, rbwr, wwwrbb, urww, rur, bru, bbbwrw, uwrwrr, ruww, ububbgr, rrb, bggrwg, bbr, wrwrb, bwgwrbg, grbuwg, gg, ubuurwg, uur, guguwb, rugurgbw, bbuwbb'
    #pattern_input = 'r, wr, b, g, bwu, rb, gb, br'
    patterns = pattern_input.split(', ')

    patterns = sorted(patterns, key=len, reverse=True)

    matches = 0
    all_matches = 0
    for des in designs:
        pattern_subset = [p for p in patterns if p in des]

        print(des, pattern_subset, matches)
        m = find_patterns_2(des, pattern_subset)
        if m > 0:
            matches += 1
            all_matches += m

    print(matches)
    print(all_matches)

