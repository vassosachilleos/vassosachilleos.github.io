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
        <p class="mb-2">Chargé de recherche – CNRS <img src="/img/cnrs-logo.png" alt="CNRS" class="hero-cnrs"></p>
        <p class="text-muted mb-4" style="font-size:0.58em; line-height:1.55;">Audible acoustics · acoustic waveguides · nonlinear acoustics &amp; sound absorption · non&#8209;Hermitian and active wave physics · non&#8209;Hermitian skin effect</p>
      portrait:
        src: img/portrait.jpg
        alt: Vassos Achilleos
      cta:
        label: Research themes
        url: research/
      cta_alt:
        label: ERC-StG-NASA
        url: project/erc-nasa/
      side_logo:
        src: img/laum-logo.png
        url: https://laum.univ-lemans.fr/fr/index.html
        alt: LAUM – Laboratoire d'Acoustique de l'Université du Mans
    design:
      css_class: hero-waves

  # 1b. Short text bio (plain text with the full name helps search engines identify the page)
  - block: markdown
    content:
      title: About
      text: |
        **Vassos Achilleos** is a CNRS researcher (*Chargé de recherche*) at the [Laboratoire d'Acoustique de l'Université du Mans (LAUM, UMR 6613)](https://laum.univ-lemans.fr), CNRS / Le Mans Université, in Le Mans, France. He works on wave physics in acoustics: acoustic waveguides and networks, nonlinear acoustics and sound absorption, and non-Hermitian and active wave systems, including the non-Hermitian skin effect, nonreciprocal lattices and exceptional points.

        He is the principal investigator of the [ERC Starting Grant NASA](project/erc-nasa/) (*Nonlinear and Active Sound Absorption*, 2023–2028), funded by the European Research Council, and a member of the scientific committee of the GDR PhyTop. He received his PhD in 2015. [Selected publications](publications/) · [Google Scholar](https://scholar.google.com/citations?user=agupRD8AAAAJ)

        *Vassos Achilleos est chargé de recherche CNRS au Laboratoire d'Acoustique de l'Université du Mans (LAUM). Ses travaux portent sur la physique des ondes en acoustique — guides d'ondes, acoustique non linéaire, absorption du son, systèmes non hermitiens et actifs — et il est porteur du projet ERC Starting Grant NASA.*
    design:
      columns: '1'

  # 2. Activities (news posts with category "Activities")
  - block: collection
    content:
      title: Activities
      count: 5
      filters:
        folders:
          - post
        category: Activities
      order: desc
    design:
      view: compact
      columns: '2'

  # 3. Updates (news posts with category "Updates")
  - block: collection
    content:
      title: Updates
      count: 5
      filters:
        folders:
          - post
        category: Updates
      order: desc
    design:
      view: compact
      columns: '2'

  # 4. Research themes (figure cards — the modern version of "Recent Works")
  - block: collection
    content:
      title: Research Themes
      count: 6
      filters:
        folders:
          - research
      order: desc
    design:
      view: theme
      columns: '1'

  # 5. Projects I participate in now (any project page tagged "current")
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

#  # 6. Latest publications (imported from BibTeX / HAL)
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

  # 7. Funding, as on the CAPS homepage
  - block: markdown
    content:
      title: Funding
      text: |
        <img src="/img/eu-erc-logo.png" alt="European Union — European Research Council" style="height:44px; width:auto; opacity:.85;" class="mb-3"><br>
        European Research Council — [ERC-StG-NASA](https://cordis.europa.eu/project/id/101077954/results) (grant agreement 101077954) · CNRS · Le Mans Université
    design:
      columns: '2'
---
