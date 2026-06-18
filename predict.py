from dataclasses import dataclass
from typing import Dict, List, Tuple, Union


# -----------------------------
# ONLY VARIABLE INPUT
# -----------------------------
# Current standings, in the current official group order.
# If teams are tied beyond pts/GD/GF, the listed order is preserved.

current_standings = {
    "A": [
        {"team": "Mexico", "pts": 3, "gf": 2, "ga": 0},
        {"team": "Korea Republic", "pts": 3, "gf": 2, "ga": 1},
        {"team": "Czechia", "pts": 0, "gf": 1, "ga": 2},
        {"team": "South Africa", "pts": 0, "gf": 0, "ga": 2},
    ],
    "B": [
        {"team": "Switzerland", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Canada", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Qatar", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Bosnia and Herzegovina", "pts": 1, "gf": 1, "ga": 1},
    ],
    "C": [
        {"team": "Scotland", "pts": 3, "gf": 1, "ga": 0},
        {"team": "Morocco", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Brazil", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Haiti", "pts": 0, "gf": 0, "ga": 1},
    ],
    "D": [
        {"team": "United States", "pts": 3, "gf": 4, "ga": 1},
        {"team": "Australia", "pts": 3, "gf": 2, "ga": 0},
        {"team": "Turkiye", "pts": 0, "gf": 0, "ga": 2},
        {"team": "Paraguay", "pts": 0, "gf": 1, "ga": 4},
    ],
    "E": [
        {"team": "Germany", "pts": 3, "gf": 7, "ga": 1},
        {"team": "Ivory Coast", "pts": 3, "gf": 1, "ga": 0},
        {"team": "Ecuador", "pts": 0, "gf": 0, "ga": 1},
        {"team": "Curacao", "pts": 0, "gf": 1, "ga": 7},
    ],
    "F": [
        {"team": "Sweden", "pts": 3, "gf": 5, "ga": 1},
        {"team": "Japan", "pts": 1, "gf": 2, "ga": 2},
        {"team": "Netherlands", "pts": 1, "gf": 2, "ga": 2},
        {"team": "Tunisia", "pts": 0, "gf": 1, "ga": 5},
    ],
    "G": [
        {"team": "New Zealand", "pts": 1, "gf": 2, "ga": 2},
        {"team": "Iran", "pts": 1, "gf": 2, "ga": 2},
        {"team": "Belgium", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Egypt", "pts": 1, "gf": 1, "ga": 1},
    ],
    "H": [
        {"team": "Uruguay", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Saudi Arabia", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Spain", "pts": 1, "gf": 0, "ga": 0},
        {"team": "Cape Verde", "pts": 1, "gf": 0, "ga": 0},
    ],
    "I": [
        {"team": "Norway", "pts": 3, "gf": 4, "ga": 1},
        {"team": "France", "pts": 3, "gf": 3, "ga": 1},
        {"team": "Senegal", "pts": 0, "gf": 1, "ga": 3},
        {"team": "Iraq", "pts": 0, "gf": 1, "ga": 4},
    ],
    "J": [
        {"team": "Argentina", "pts": 3, "gf": 3, "ga": 0},
        {"team": "Austria", "pts": 3, "gf": 3, "ga": 1},
        {"team": "Jordan", "pts": 0, "gf": 1, "ga": 3},
        {"team": "Algeria", "pts": 0, "gf": 0, "ga": 3},
    ],
    "K": [
        {"team": "Colombia", "pts": 3, "gf": 3, "ga": 1},
        {"team": "Congo DR", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Portugal", "pts": 1, "gf": 1, "ga": 1},
        {"team": "Uzbekistan", "pts": 0, "gf": 1, "ga": 3},
    ],
    "L": [
        {"team": "England", "pts": 3, "gf": 4, "ga": 2},
        {"team": "Ghana", "pts": 3, "gf": 1, "ga": 0},
        {"team": "Panama", "pts": 0, "gf": 0, "ga": 1},
        {"team": "Croatia", "pts": 0, "gf": 2, "ga": 4},
    ],
}


# -----------------------------
# CONSTANTS
# -----------------------------
# Lower rank number = better FIFA ranking.

FIFA_RANK = {
    "Argentina": 1,
    "Spain": 2,
    "France": 3,
    "England": 4,
    "Portugal": 5,
    "Brazil": 6,
    "Morocco": 7,
    "Netherlands": 8,
    "Belgium": 9,
    "Germany": 10,
    "Croatia": 11,
    "Colombia": 13,
    "Mexico": 14,
    "Senegal": 15,
    "Uruguay": 16,
    "United States": 17,
    "Japan": 18,
    "Switzerland": 19,
    "Iran": 20,
    "Turkiye": 22,
    "Ecuador": 23,
    "Austria": 24,
    "Korea Republic": 25,
    "Australia": 27,
    "Algeria": 28,
    "Egypt": 29,
    "Canada": 30,
    "Norway": 31,
    "Ivory Coast": 33,
    "Panama": 34,
    "Sweden": 38,
    "Czechia": 40,
    "Scotland": 41,
    "Congo DR": 46,
    "Uzbekistan": 50,
    "Qatar": 56,
    "Iraq": 57,
    "South Africa": 60,
    "Saudi Arabia": 61,
    "Jordan": 63,
    "Bosnia and Herzegovina": 64,
    "Cape Verde": 67,
    "Ghana": 73,
    "Curacao": 82,
    "Haiti": 83,
    "New Zealand": 85,
    "Tunisia": 90,
    "Paraguay": 95,
}


# -----------------------------
# THIRD-PLACE ASSIGNMENT TABLE
# -----------------------------
# This currently supports the third-place combination from your standings:
# A, B, C, E, F, G, H, K.
#
# If standings change and another combination qualifies, add the corresponding
# FIFA Annex C mapping.

THIRD_PLACE_ASSIGNMENTS = {
    "ABCEFGHK": {
        74: "C",
        77: "F",
        79: "H",
        80: "K",
        81: "B",
        82: "A",
        85: "G",
        87: "E",
    }
}


# -----------------------------
# BRACKET STRUCTURE
# -----------------------------

R32_SLOTS = {
    73: (("A", 2), ("B", 2)),
    74: (("E", 1), ("third", 3, "ABCDF")),
    75: (("F", 1), ("C", 2)),
    76: (("C", 1), ("F", 2)),
    77: (("I", 1), ("third", 3, "CDFGH")),
    78: (("E", 2), ("I", 2)),
    79: (("A", 1), ("third", 3, "CEFHI")),
    80: (("L", 1), ("third", 3, "EHIJK")),
    81: (("D", 1), ("third", 3, "BEFIJ")),
    82: (("G", 1), ("third", 3, "AEHIJ")),
    83: (("K", 2), ("L", 2)),
    84: (("H", 1), ("J", 2)),
    85: (("B", 1), ("third", 3, "EFGIJ")),
    86: (("J", 1), ("H", 2)),
    87: (("K", 1), ("third", 3, "DEIJL")),
    88: (("D", 2), ("G", 2)),
}

R16_PAIRINGS = {
    89: (73, 75),
    90: (74, 77),
    91: (76, 78),
    92: (79, 80),
    93: (83, 84),
    94: (81, 82),
    95: (86, 88),
    96: (85, 87),
}

QF_PAIRINGS = {
    97: (89, 90),
    98: (93, 94),
    99: (91, 92),
    100: (95, 96),
}

SF_PAIRINGS = {
    101: (97, 98),
    102: (99, 100),
}


@dataclass(frozen=True)
class TeamPosition:
    team: str
    group: str
    place: int
    pts: int
    gf: int
    ga: int

    @property
    def gd(self) -> int:
        return self.gf - self.ga


Slot = Union[Tuple[str, int], Tuple[str, int, str]]


# -----------------------------
# STANDINGS LOGIC
# -----------------------------

def rank_group(group: str, rows: List[dict]) -> List[TeamPosition]:
    enriched = []

    for original_order, row in enumerate(rows):
        enriched.append((original_order, row))

    ranked = sorted(
        enriched,
        key=lambda item: (
            -item[1]["pts"],
            -(item[1]["gf"] - item[1]["ga"]),
            -item[1]["gf"],
            item[0],
        ),
    )

    return [
        TeamPosition(
            team=row["team"],
            group=group,
            place=i + 1,
            pts=row["pts"],
            gf=row["gf"],
            ga=row["ga"],
        )
        for i, (_, row) in enumerate(ranked)
    ]


def build_positions(standings: Dict[str, List[dict]]) -> Dict[Tuple[str, int], TeamPosition]:
    positions = {}

    for group, rows in standings.items():
        for pos in rank_group(group, rows):
            positions[(group, pos.place)] = pos

    return positions


def validate_inputs(standings: Dict[str, List[dict]]) -> None:
    expected_groups = list("ABCDEFGHIJKL")
    actual_groups = sorted(standings.keys())

    if actual_groups != expected_groups:
        raise ValueError(
            f"Expected groups {expected_groups}, but got {actual_groups}."
        )

    missing_rankings = []

    for group, rows in standings.items():
        if len(rows) != 4:
            raise ValueError(f"Group {group} should have exactly 4 teams.")

        for row in rows:
            team = row["team"]
            if team not in FIFA_RANK:
                missing_rankings.append(team)

            for key in ["pts", "gf", "ga"]:
                if key not in row:
                    raise ValueError(f"Missing '{key}' for {team} in Group {group}.")

    if missing_rankings:
        unique_missing = sorted(set(missing_rankings))
        raise ValueError(
            "Missing FIFA rankings for: " + ", ".join(unique_missing)
        )


def get_best_third_place_groups(
    positions: Dict[Tuple[str, int], TeamPosition],
    standings: Dict[str, List[dict]],
) -> List[str]:
    thirds = [positions[(group, 3)] for group in sorted(standings)]

    best_thirds = sorted(
        thirds,
        key=lambda t: (
            -t.pts,
            -t.gd,
            -t.gf,
            FIFA_RANK[t.team],
        ),
    )[:8]

    return sorted(t.group for t in best_thirds)


# -----------------------------
# KNOCKOUT LOGIC
# -----------------------------

def resolve_slot(
    slot: Slot,
    positions: Dict[Tuple[str, int], TeamPosition],
    third_assignment: Dict[int, str],
    match_no: int,
) -> TeamPosition:
    if slot[0] == "third":
        third_group = third_assignment[match_no]
        return positions[(third_group, 3)]

    group, place = slot
    return positions[(group, place)]


def winner(team_a: TeamPosition, team_b: TeamPosition) -> TeamPosition:
    return team_a if FIFA_RANK[team_a.team] < FIFA_RANK[team_b.team] else team_b


def loser(team_a: TeamPosition, team_b: TeamPosition) -> TeamPosition:
    return team_b if winner(team_a, team_b) == team_a else team_a


def make_match(match_no: int, team_a: TeamPosition, team_b: TeamPosition) -> dict:
    w = winner(team_a, team_b)
    l = loser(team_a, team_b)

    return {
        "match": match_no,
        "team_a": team_a.team,
        "team_b": team_b.team,
        "rank_a": FIFA_RANK[team_a.team],
        "rank_b": FIFA_RANK[team_b.team],
        "winner": w.team,
        "loser": l.team,
        "winner_rank": FIFA_RANK[w.team],
        "loser_rank": FIFA_RANK[l.team],
    }


def pos_from_winner(match: dict) -> TeamPosition:
    return TeamPosition(
        team=match["winner"],
        group="KO",
        place=0,
        pts=0,
        gf=0,
        ga=0,
    )


def pos_from_loser(match: dict) -> TeamPosition:
    return TeamPosition(
        team=match["loser"],
        group="KO",
        place=0,
        pts=0,
        gf=0,
        ga=0,
    )


def predict_knockout(standings: Dict[str, List[dict]]) -> Dict[str, object]:
    validate_inputs(standings)

    positions = build_positions(standings)
    third_groups = get_best_third_place_groups(positions, standings)
    combo = "".join(third_groups)

    if combo not in THIRD_PLACE_ASSIGNMENTS:
        raise ValueError(
            f"No third-place assignment table loaded for combo {combo}. "
            "Add the FIFA Annex C mapping for this combination."
        )

    third_assignment = THIRD_PLACE_ASSIGNMENTS[combo]

    r32 = {}

    for match_no, (slot_a, slot_b) in R32_SLOTS.items():
        team_a = resolve_slot(slot_a, positions, third_assignment, match_no)
        team_b = resolve_slot(slot_b, positions, third_assignment, match_no)
        r32[match_no] = make_match(match_no, team_a, team_b)

    r16 = {}

    for match_no, (m1, m2) in R16_PAIRINGS.items():
        r16[match_no] = make_match(
            match_no,
            pos_from_winner(r32[m1]),
            pos_from_winner(r32[m2]),
        )

    qf = {}

    for match_no, (m1, m2) in QF_PAIRINGS.items():
        qf[match_no] = make_match(
            match_no,
            pos_from_winner(r16[m1]),
            pos_from_winner(r16[m2]),
        )

    sf = {}

    for match_no, (m1, m2) in SF_PAIRINGS.items():
        sf[match_no] = make_match(
            match_no,
            pos_from_winner(qf[m1]),
            pos_from_winner(qf[m2]),
        )

    third_place = {
        103: make_match(
            103,
            pos_from_loser(sf[101]),
            pos_from_loser(sf[102]),
        )
    }

    final = {
        104: make_match(
            104,
            pos_from_winner(sf[101]),
            pos_from_winner(sf[102]),
        )
    }

    return {
        "qualifying_third_place_groups": third_groups,
        "third_place_combo": combo,
        "round_of_32": list(r32.values()),
        "round_of_16": list(r16.values()),
        "quarterfinals": list(qf.values()),
        "semifinals": list(sf.values()),
        "third_place": list(third_place.values()),
        "final": list(final.values()),
        "champion": final[104]["winner"],
    }


# -----------------------------
# TERMINAL OUTPUT
# -----------------------------

def print_standings(standings: Dict[str, List[dict]]) -> None:
    print("CURRENT STANDINGS")
    print()

    for group in sorted(standings):
        print(f"Group {group}")

        for row in rank_group(group, standings[group]):
            print(
                f"  {row.place}. {row.team} "
                f"{row.pts} pts, GF {row.gf}, GA {row.ga}, GD {row.gd:+}"
            )

        print()


def print_predictions(predictions: Dict[str, object]) -> None:
    print("QUALIFYING THIRD-PLACE GROUPS")
    print(predictions["qualifying_third_place_groups"])
    print()

    for round_name in [
        "round_of_32",
        "round_of_16",
        "quarterfinals",
        "semifinals",
        "third_place",
        "final",
    ]:
        print(round_name.upper())

        for m in predictions[round_name]:
            print(
                f"M{m['match']}: "
                f"{m['team_a']} (FIFA {m['rank_a']}) vs "
                f"{m['team_b']} (FIFA {m['rank_b']}) -> "
                f"{m['winner']} (FIFA {m['winner_rank']})"
            )

        print()

    print("PREDICTED CHAMPION")
    print(predictions["champion"])


# -----------------------------
# WEBSITE GENERATOR
# -----------------------------

def generate_website(
    standings: Dict[str, List[dict]],
    predictions: Dict[str, object],
    output_file: str = "index.html",
) -> None:
    def escape(text: object) -> str:
        return (
            str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    def standings_table(group: str, rows: List[dict]) -> str:
        ranked_rows = rank_group(group, rows)

        body = ""

        for row in ranked_rows:
            body += f"""
                <tr>
                    <td>{row.place}</td>
                    <td class="team-name">{escape(row.team)}</td>
                    <td>{row.pts}</td>
                    <td>{row.gf}</td>
                    <td>{row.ga}</td>
                    <td>{row.gd:+}</td>
                </tr>
            """

        return f"""
            <section class="card">
                <h3>Group {escape(group)}</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Pos</th>
                            <th>Team</th>
                            <th>Pts</th>
                            <th>GF</th>
                            <th>GA</th>
                            <th>GD</th>
                        </tr>
                    </thead>
                    <tbody>
                        {body}
                    </tbody>
                </table>
            </section>
        """

    def match_card(match: dict) -> str:
        team_a_is_winner = match["winner"] == match["team_a"]
        team_b_is_winner = match["winner"] == match["team_b"]

        return f"""
            <article class="match-card">
                <div class="match-number">M{match["match"]}</div>

                <div class="match-row {'winner' if team_a_is_winner else ''}">
                    <span>{escape(match["team_a"])}</span>
                    <small>FIFA {match["rank_a"]}</small>
                </div>

                <div class="match-row {'winner' if team_b_is_winner else ''}">
                    <span>{escape(match["team_b"])}</span>
                    <small>FIFA {match["rank_b"]}</small>
                </div>

                <div class="winner-label">
                    Winner: <strong>{escape(match["winner"])}</strong>
                </div>
            </article>
        """

    def knockout_section(title: str, key: str) -> str:
        cards = "\n".join(match_card(match) for match in predictions[key])

        return f"""
            <section class="section-block">
                <h2>{escape(title)}</h2>
                <div class="bracket-grid">
                    {cards}
                </div>
            </section>
        """

    standings_html = "\n".join(
        standings_table(group, standings[group])
        for group in sorted(standings)
    )

    knockout_html = "\n".join(
        [
            knockout_section("Round of 32", "round_of_32"),
            knockout_section("Round of 16", "round_of_16"),
            knockout_section("Quarterfinals", "quarterfinals"),
            knockout_section("Semifinals", "semifinals"),
            knockout_section("Third Place Match", "third_place"),
            knockout_section("Final", "final"),
        ]
    )

    qualifying_thirds = ", ".join(predictions["qualifying_third_place_groups"])
    champion = predictions["champion"]
    third_place_combo = predictions["third_place_combo"]

    html = f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>World Cup Knockout Predictor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        :root {{
            --bg: #0f172a;
            --panel: #111827;
            --panel-light: #1f2937;
            --text: #f9fafb;
            --muted: #9ca3af;
            --accent: #22c55e;
            --accent-soft: rgba(34, 197, 94, 0.12);
            --border: #374151;
            --danger: #f97316;
        }}

        * {{
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            margin: 0;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background:
                radial-gradient(circle at top left, rgba(34, 197, 94, 0.16), transparent 28rem),
                var(--bg);
            color: var(--text);
            line-height: 1.5;
        }}

        a {{
            color: inherit;
        }}

        header {{
            padding: 56px 24px 44px;
            text-align: center;
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.92), rgba(30, 41, 59, 0.92));
            border-bottom: 1px solid var(--border);
        }}

        header h1 {{
            margin: 0 0 12px;
            font-size: clamp(2.2rem, 5vw, 4.8rem);
            line-height: 1;
            letter-spacing: -0.05em;
        }}

        header p {{
            margin: 0 auto;
            max-width: 820px;
            color: var(--muted);
            font-size: 1.05rem;
        }}

        nav {{
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 28px;
        }}

        nav a {{
            text-decoration: none;
            color: var(--text);
            border: 1px solid var(--border);
            background: rgba(255, 255, 255, 0.04);
            padding: 9px 14px;
            border-radius: 999px;
            font-size: 0.9rem;
        }}

        main {{
            width: min(1240px, calc(100% - 32px));
            margin: 32px auto 72px;
        }}

        h2 {{
            margin: 0 0 18px;
            font-size: 1.8rem;
            letter-spacing: -0.03em;
        }}

        h3 {{
            margin: 0 0 12px;
            font-size: 1.1rem;
        }}

        .section-block {{
            margin-top: 52px;
        }}

        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 16px;
            margin-bottom: 44px;
        }}

        .summary-card {{
            background: linear-gradient(180deg, rgba(31, 41, 55, 0.9), rgba(17, 24, 39, 0.9));
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 22px;
            min-height: 120px;
        }}

        .summary-card span {{
            display: block;
            color: var(--muted);
            font-size: 0.9rem;
            margin-bottom: 8px;
        }}

        .summary-card strong {{
            display: block;
            font-size: 1.5rem;
            line-height: 1.2;
            color: var(--accent);
        }}

        .note {{
            background: rgba(249, 115, 22, 0.09);
            border: 1px solid rgba(249, 115, 22, 0.4);
            color: #fed7aa;
            border-radius: 18px;
            padding: 18px;
            margin-bottom: 36px;
        }}

        .group-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(285px, 1fr));
            gap: 18px;
        }}

        .card {{
            background: rgba(17, 24, 39, 0.92);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 18px;
            overflow: hidden;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
        }}

        th,
        td {{
            padding: 9px 7px;
            border-bottom: 1px solid var(--border);
            text-align: left;
            white-space: nowrap;
        }}

        th {{
            color: var(--muted);
            font-weight: 650;
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}

        td.team-name {{
            white-space: normal;
            font-weight: 650;
        }}

        tr:last-child td {{
            border-bottom: 0;
        }}

        .bracket-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
            gap: 16px;
        }}

        .match-card {{
            background: rgba(17, 24, 39, 0.92);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 16px;
        }}

        .match-number {{
            color: var(--muted);
            font-size: 0.82rem;
            margin-bottom: 10px;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }}

        .match-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
            padding: 11px 12px;
            margin: 7px 0;
            background: var(--panel-light);
            border-radius: 12px;
            border: 1px solid transparent;
        }}

        .match-row span {{
            font-weight: 650;
        }}

        .match-row small {{
            color: var(--muted);
            white-space: nowrap;
        }}

        .match-row.winner {{
            border-color: var(--accent);
            background: var(--accent-soft);
            color: var(--accent);
        }}

        .match-row.winner small {{
            color: var(--accent);
        }}

        .winner-label {{
            margin-top: 12px;
            font-size: 0.9rem;
            color: var(--muted);
        }}

        footer {{
            color: var(--muted);
            text-align: center;
            padding: 34px 16px;
            border-top: 1px solid var(--border);
            font-size: 0.9rem;
        }}

        @media print {{
            body {{
                background: white;
                color: black;
            }}

            header,
            .summary-card,
            .card,
            .match-card {{
                background: white;
                color: black;
                border-color: #ddd;
            }}

            .match-row {{
                background: #f6f6f6;
            }}

            .match-row.winner {{
                color: black;
                border-color: black;
            }}

            nav {{
                display: none;
            }}
        }}
    </style>
</head>

<body>
    <header>
        <h1>World Cup Predictor</h1>
        <p>
            Current group standings and a projected knockout bracket. 
            Knockout winners are selected by best FIFA ranking, where a lower ranking number is better.
        </p>

        <nav>
            <a href="#standings">Standings</a>
            <a href="#round-of-32">Round of 32</a>
            <a href="#final">Final</a>
        </nav>
    </header>

    <main>
        <section class="summary">
            <div class="summary-card">
                <span>Predicted Champion</span>
                <strong>{escape(champion)}</strong>
            </div>

            <div class="summary-card">
                <span>Qualifying Third-Place Groups</span>
                <strong>{escape(qualifying_thirds)}</strong>
            </div>

            <div class="summary-card">
                <span>Third-Place Mapping Combo</span>
                <strong>{escape(third_place_combo)}</strong>
            </div>
        </section>

        <div class="note">
            Best third-place fallback uses FIFA ranking when fair-play points are unavailable.
        </div>

        <section id="standings" class="section-block">
            <h2>Group Standings</h2>
            <div class="group-grid">
                {standings_html}
            </div>
        </section>

        <div id="round-of-32">
            {knockout_html}
        </div>
    </main>

    <footer>
        Generated by predict.py.
    </footer>
</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Website generated: {output_file}")


# -----------------------------
# MAIN
# -----------------------------

def main() -> None:
    predictions = predict_knockout(current_standings)

    print_standings(current_standings)
    print_predictions(predictions)

    generate_website(
        standings=current_standings,
        predictions=predictions,
        output_file="index.html",
    )


if __name__ == "__main__":
    main()