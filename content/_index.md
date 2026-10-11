---
title:
date: 2026-10-11
type: landing

sections:
  # 1. Who we are
  - block: hero
    content:
      title: |
        Vassos Achilleos
      text: |
        <p class="mb-2">Chargé de recherche</p>
        <p class="text-muted mb-4" style="font-size:0.72em; line-height:1.5;">Non-Hermitian and active wave physics · non-Hermitian skin effect · nonreciprocal lattices · exceptional points &amp; PT-symmetry · coherent perfect absorption · scattering-matrix methods</p>
      cta:
        label: Research themes
        url: research/
      cta_alt:
        label: ERC-StG-NASA
        url: project/erc-nasa/

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

  # 3. Activities (news posts with category "Activities")
  - block: collection
    content:
      title: Activities
      subtitle: Papers, grants, conferences, visits
      count: 5
      filters:
        folders:
          - post
        category: Activities
      order: desc
    design:
      view: compact
      columns: '2'

  # 4. Updates (news posts with category "Updates")
  - block: collection
    content:
      title: Updates
      subtitle: Arrivals, defences, awards
      count: 5
      filters:
        folders:
          - post
        category: Updates
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
        European Research Council — [ERC-StG-NASA](https://cordis.europa.eu/project/id/101077954/results) (grant agreement 101077954) · CNRS · Le Mans Université
    design:
      columns: '2'
---
