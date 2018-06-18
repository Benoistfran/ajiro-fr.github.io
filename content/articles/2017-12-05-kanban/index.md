---
date: 2017-12-05
title: "Sensibilisation à Kanban"
lang: fr
draft: false
authors:
  - retiere_samuel
tags:
  - Kanban
  - KitMoaAgile
categories:
  - craft
illustration:
  name: kanban
  source: https://flic.kr/p/bMk2Dk
description: |
  Kanban est une approche peu prescriptive avec un focus fort sur l’adaptation au contexte. Si elle est souvent assimilée à de la gestion de taches sur un tableau, c’est beaucoup plus un framework d’amélioration continue.
---
La question de savoir si « Kanban pour l’IT » prend sa source dans le Lean ou dans l’Agile importe peu, cette méthode peut être utilisée dans le cadre du développement produit. C’est une approche peu prescriptive avec un focus fort sur l’adaptation au contexte. Si elle est souvent assimilée à de la gestion de taches sur un tableau, c’est beaucoup plus un framework d’amélioration continue. Il repose pour beaucoup sur de la systémique, je vois l’équipe comme un système qui peut évoluer. Avec Kanban, on intègre toutes les personnes qui contribuent au développement produit. Pour rappel, on considère que nous sommes dans un système quand toutes les parties ensemble produisent un effet différent de toutes les parties prises séparément. Je parle d'ailleurs d'un système où ma capacité à produire est inférieure à la demande. Ca tombe bien, je ne connais que des systèmes dans ce genre dans le monde du travail.

## Impacts attendus
{{< img name="naturalPower" legend="Natural Power" source="https://flic.kr/p/nZcK7x" >}}
Si je présente Kanban en utilisant kanban thinking de Karl Scotland, je dirais que Kanban vise trois impacts :<br>
- Ecouler le plus efficacement possible le flux de demandes traitées<br>
- Maximiser la valeur délivrée<br>
- Développer les personnes pour augmenter le potentiel du système

Pour la suite, je décris une mise en place classique de Kanban.

## Comprendre
{{< img name="weddingTime" legend="Wedding time" source="https://flic.kr/p/nJjJw9" >}}
Le point de départ d’une utilisation de Kanban est de prendre le système tel qu’il est. Il n’y a donc pas de rôle prescrit tel que le Product Owner ou le Scrum Master. Si l’équipe en ressent le besoin, elle pourra en créer. Pour comprendre ce que le système produit, je vais détailler les types de demandes qui rentre, puis quelles sont les étapes à l'intérieur système et ensuite définir ce qui en sort. Pour faire cela, je vais prendre une demande type et la suivre de bout en bout. Cela ressemble souvent à ça : Demande - Etude - Specifications - Dev - Tests - Production.

## Visualiser
{{< img name="iconoclasta" legend="Iconoclasta" source="https://flic.kr/p/oN8juu" >}}
Le but est de créer une compréhension commune de ce qui se passe. Pour cela, je vais créer les « célèbres » tableaux Kanban avec toutes les demandes qui passent de A début du process à Z fin du process. Les colonnes représentent les étapes de mon process (A faire, Etude, Spécifications, Développement, ...) .  Les lignes sont un regroupement qui doit m’aider à mieux comprendre ce qui se passe. A cette étape, vous devez avoir compris que le focus de Kanban est vraiment sur ce que délivre une équipe (le système) et pas sur chaque partie (dev d'un côté et moa de l'autre) ou sous partie (les personnes). Il s’agit de favoriser un optimum global (et pas local) et d’être focalisé sur la génération de valeur.

## Gérer
{{< img name="vitaDaCirco" legend="Vita da circo" source="https://flic.kr/p/kb2z71" >}}
Une fois que je comprends ce qui se passe dans mon système, je vais essayer de le piloter le mieux possible pour que le flux soit le plus efficace. Comme pour une rivière, un canal, … , je vais essayer d’avoir le flux le plus laminaire possible. Je vais chercher à limiter les goulets d’étranglement et les soubresauts. Pour cela, il est intéressant de :<br>
- Limiter le travail en cours. C’est souvent contre-intuitif, mais moins je traite de de demandes en parallèle plus mon système est efficace. Vous pouvez le voir sur le débit de demandes sur une période de temps donné.<br>
- Rendre explicite les passages de relais. Je diminue les sources d’incompréhension en explicitant ce qui permet de dire qu’une demande peut passer dans l’étape suivante.<br>
- Je gère mon flux en ne mélangeant pas tous les types demandes. Je peux créer des classes de service avec des comportements différents. Il s’agit principalement d’avoir des délais de réponse différent, l’exemple typique concerne les urgences.<br>
- Je suis en flux tiré. Je vais arrêter de commencer pour commencer à finir. Cela a un impact sur les points de synchronisation. La priorité de l’équipe est de faire sortir ce qui est à la fin du process. Cela tire la polyvalence avec je me répète un focus sur l'ensemble.<br>

Au niveau de l’alimentation du système en nouvelle demande, Kanban n’est pas prescriptif. Cela peut être fait avec une liste ordonnée dans laquelle on vient piocher ou par l’utilisation d’une cadence d’injection (comme pour Scrum avec ses sprints).

## Ressentir
{{< img name="weddingTime2" legend="Wedding Time" source="https://flic.kr/p/kydKkT" >}}
C’est un des points importants de Kanban. Je commence avec mon état initial, mais en ayant bien en tête que je vais l’améliorer au fur et à mesure. Je vais récupérer des mesures qui vont m’aider à mieux comprendre mon système pour le faire évoluer. Je vais par exemple regarder le temps que prend une demande à passer du début à la fin, voir le temps de passage par étape, mesurer les temps d’attente dans les files d’attente,… Je me donne les moyens de faire évoluer mon système.

## Améliorer
{{< img name="VitaDaCirco2" legend="Vita da circo" source="https://flic.kr/p/niw7Lm" >}}
Qu’est-ce que j’améliore ? Et bien un peu tout ce que je peux. Il n’y a pas de raison de limiter son approche. Cela peut donc être au niveau d’une personne, d’un groupe, d’une équipe, d’une organisation,… Au niveau temporel, cela peut être sous la forme d’une rétrospective tous les x semaines. Cela peut aussi se faire au fil de l’eau en améliorant au fur et à mesure ce qui peut l’être. Il s’agit d’adapter l'expérimentation à la temporalité des boucles de feedback. Je suis de plus en plus dans l’idée que l’amélioration peut être faite à n’importe quel moment et que cela est bénéfique car le changement devient permanent et donc sans à coup.

{{< img name="voyage" legend="Il commissario Nasta" source="https://flic.kr/p/di95Ra" >}}

Et quand est ce que l’on s’arrête ? Et bien jamais. Bon voyage.
