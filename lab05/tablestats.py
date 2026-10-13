def read_rows(lines):
    rows = []
    headers = None

    for line in lines:
        cleaned_line = line.strip()

        if not cleaned_line:
            continue
        parts = cleaned_line.split(',')
        parts = [p.strip() for p in parts]

        if headers is None:
            headers = parts
            continue

        if len(parts) != len(headers):
            continue

        row_dict = dict(zip(headers, parts))
        rows.append(row_dict)
    return rows

def count_types(rows):
    counts = {}

    for row in rows:
        kind = row.get('тип')
        if kind:
            counts[kind] = counts.get(kind, 0) + 1

    return counts

def total_minutes(rows, kind):
    total = 0.0
    has_kind = False

    for row in rows:
        if row.get('тип') == kind:
            has_kind = True
            minutes_str = row.get('минуты', '')

            minutes_str = minutes_str.replace(',','.')

            try:
                total += float(minutes_str)
            except ValueError:
                continue

    if not has_kind:
        return 0.0

    return round(total,1)

def to_csv(counts):
    lines = ['тип,количество']

    for kind in sorted(counts.keys()):
        lines.append(f'{kind},{counts[kind]}')

    return '\n'.join(lines) + '\n'


