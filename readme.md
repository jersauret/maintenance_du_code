# Maintenance du code par NEBOUT et SAURET

Le projet est développé en python et il vise à améliorier la qualité du code en le rendant plus lisible. Le but est que l'application soit plus facilement maintenable dans le temps.

## Analyse de gravité

Tout d'abord, nous avons identifié plusieurs défis dans le code:
- Incohérences dans les noms de fichiers 
- Incohérence dans les noms de variables
- Utilisation de constantes magiques sans explication claire
- Utilisation de méthodes complexes avec des boucles imbriquées
- Logique métier incompréhensible

## Justification des priorités

Nos choix ont été influencés par:
Le besoin réel, que nous avons identifié comme:
- Une app relativement basique
- Pas de fort risque de sécurité 
- Peu de problématiques de charge. 

Les projections sur l’avenir:
- Maintien des fonctionnalités suite aux améliorations apportées.
- Intégration du multilingue	

Nous allons donc choisir de nous focaliser sur:
- Les smells faciles à cueillir et facilement atteignables pour la partie junior de la team qui les réaliseront en pair: ceci permettra de propager la connaissance des standards nommage par exemple.
- Les thématiques structurantes dont la résolution pourrait rencontrer des écueils seront adressées, en mob programming, avec les seniors au manettes. Ceci nous permettra de propager un petit peu la connaissance des thématiques complexes


Ces problèmes, bien que de gravités variables, affectent la lisibilité, la maintenabilité et la robustesse du code. Par conséquent, nous avons accordé la priorité à leur résolution pour établir une base solide pour le développement ultérieur.

## Golden Master

Une fois terminé
Comment je me sers du golden master pour garantir le contrat d'origine
il casse et il reveint au vert quand on a modifié