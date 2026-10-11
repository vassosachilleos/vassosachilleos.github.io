---
title:
date: 2026-10-11
type: landing

sections:
  # 1. Who we are
  - block: hero
    content:
      title: |
        Wave Physics Team
      text: |
        <br>
        We study <strong>non-Hermitian and active wave physics</strong> at the
        Laboratoire d'Acoustique de l'Université du Mans (LAUM, UMR 6613 CNRS):
        non-Hermitian skin effect, nonreciprocal lattices, exceptional points,
        PT-symmetry, coherent perfect absorption and scattering-matrix methods.
      cta:
        label: Research themes
        url: research/
      cta_alt:
        label: Meet the team
        url: people/

  # 2a. Research themes (figure cards — the modern version of "Recent Works")
  - block: collection
    content:
      title: Research Themes
      count: 6
      filters:
        folders:
          - research
      order: desc
    design:
      view: showcase
      flip_alt_rows: true
      columns: '1'

  # 2. Projects I participate in now (any project page tagged "current")
  - block: collection
    content:
      title: Current Projects
      count: 6
      filters:
        folders:
          - project
        tag: current
      order: desc
    design:
      view: card
      columns: '2'

  # 3. Activities of the whole team (news posts with category "Team")
  - block: collection
    content:
      title: Team Activities
      subtitle: Papers, grants, conferences, visits
      count: 5
      filters:
        folders:
          - post
        category: Team
      order: desc
    design:
      view: compact
      columns: '2'

  # 4. Updates of individual members (news posts with category "Members")
  - block: collection
    content:
      title: Member Updates
      subtitle: Arrivals, defences, awards
      count: 5
      filters:
        folders:
          - post
        category: Members
      order: desc
    design:
      view: compact
      columns: '2'

#  # 5. Latest publications (imported from BibTeX / HAL)
#  - block: collection
#    content:
#      title: Latest Publications
#      count: 5
#      filters:
#        folders:
#          - publication
#    design:
#      view: citation
#      columns: '2'

  # 6. Funding, as on the CAPS homepage
  - block: markdown
    content:
      title: Funding
      text: |
        European Research Council (ERC) — project NASA · CNRS · Le Mans Université
    design:
      columns: '2'
---
