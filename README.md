# Manda video agent skills

Adaptation pour Codex sur le VPS Manda : références, aperçu de cinq secondes,
production HyperFrames, voix Orus fournie par le service existant, contrôle
indépendant et livraison Drive. Metricool reste piloté par ChatGPT Work.

## Paquet installé

Seul `manda/skills/` est distribué :

- `manda-video-reference` : analyse visuelle/sonore, critères et aperçu comparatif.
- `manda-hyperframes-production` : composition, son et preuves du rendu.
- `manda-hyperframes-review` : contrôle indépendant, distinct de l'acceptation créative.

`skills/` contient les sources originales pour comparaison : ne pas les
installer avec une commande globale `skills add`. Remotion et Treg ne font
pas partie de notre adaptation.

## Validation

```text
python manda/scripts/release.py --check
python manda/scripts/release.py --output <dossier-hors-du-depot>
```

Le script ne contacte aucun service et n'exécute aucun fichier upstream.
Il vérifie l'allowlist et les liens locaux, construit une archive avec manifeste
SHA-256 et copie la licence MIT. [Installation opérateur](manda/OPERATIONS.md).

## Limites

L'aperçu et l'acceptation sont des consignes aux agents. Le MCP existant n'a
pas encore de commande dédiée d'approbation : l'opérateur prépare l'aperçu
séparément et transmet l'accord à la tâche complète. Un job complet sans
acceptation doit s'arrêter (`blocked`). Ce paquet ne modifie pas le runtime.
Aucune référence vidéo n'est embarquée. La qualité doit être démontrée par un
vrai essai et acceptée par Manda, pas par un score auto-attribué.

## Origine

Fork de [Melvynx/video-agent-skills](https://github.com/Melvynx/video-agent-skills),
version auditée `3c897e82fa8992ebd09ffcc3c65c5d22b0de2edd`.
La méthode de référence adapte `video-steal` et ses retours d'expérience.
Production/review proviennent du pipeline Manda, adaptés le 13 octobre 2026.
[Licence MIT](LICENSE) et attribution originales conservées.
[Documentation originale](UPSTREAM-README.md).
Mises à jour upstream examinées par diff, jamais installées automatiquement.
