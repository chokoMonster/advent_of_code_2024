def check_reports(report_list, mode='smaller', skip=0):
    r = report_list[0]
    for i, _ in enumerate(report_list):
        if i == len(reports) - 1:
            return True

        valid = False
        r1 = report_list[i + 1]

        if mode == 'smaller':
            if r1 > r >= (r1 - 3):
                valid = True
        else:
            if r1 < r <= (r1 + 3):
                valid = True

        if valid:
            r = r1
        elif skip > 0:
            skip -= 1
        else:
            return False


if __name__ == "__main__":
    f = open("input/ferdi02.txt","r")
    lines = f.readlines()

    counter = 0
    for line in lines:
        reports = line.strip().split(' ')
        reports = [int(r) for r in reports]

        """
        gr = all(reports[i + 1] > reports[i] >= reports[i + 1] - 3 for i in range(len(reports) - 1))
        sm = all(reports[i + 1] < reports[i] <= reports[i + 1] + 3 for i in range(len(reports) - 1))
        if gr or sm:
            counter += 1
        """

        if check_reports(reports, 'smaller', 1) or check_reports(reports, 'greater', 1):
            counter += 1
        else:
            reports.pop(0)
            if check_reports(reports) or check_reports(reports, 'greater'):
                counter += 1

    print(counter)
    # 665
