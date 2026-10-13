# Installation opérateur

Seul `manda/skills/` est distribuable. Ne jamais installer les skills upstream.

1. Via `ssh meckia-vps`, vérifier qu'aucun job vidéo ni tâche Codex n'est actif.
2. Construire le paquet hors du dépôt, depuis le commit choisi ; noter commit et
   SHA-256 de l'archive dans le compte rendu de déploiement.
3. Transférer dans `/srv/dev/artifacts/`. Vérifier le SHA-256, extraire dans un
   staging neuf non découvert par Codex, puis comparer chaque fichier au
   manifeste. Refuser chemins absolus, traversées et liens.
4. Sauvegarder les trois dossiers existants de
   `/home/codex-dev/.codex/skills/` sous artifacts. Noter les dossiers absents.
5. Installer uniquement ces dossiers validés, propriétaire codex-dev,
   répertoires 750 et fichiers 640. Revérifier toutes les empreintes.
6. Vérifier une nouvelle connexion SSH privée, la santé du contrôle et du MCP,
   les services concernés, l'exposition firewall et les webapps.

Aucun redémarrage : les nouvelles sessions lisent les skills. Ne pas remplacer
tout `~/.codex/skills`, ni modifier les sessions en cours ou les secrets.

Rollback, sans tâche active : déplacer les dossiers installés en quarantaine,
restaurer uniquement les dossiers précédemment présents depuis la sauvegarde,
vérifier propriétaire et empreintes. Conserver preuves, jobs et caches.

## Parcours attendu

Sans référence, demander une référence ou proposer une direction. Pour un film
complet sans acceptation, produire `qa/creative-gate.json` et arrêter avant le
rendu. Une empreinte d'aperçu modifiée invalide l'acceptation. Après accord,
l'opérateur fournit les fichiers et la trace du message à la tâche complète.
Réutiliser les voix en cache. La publication Metricool reste distincte.

Le runtime 0.2.0 doit ?tre d?ploy? avec ces skills : il expose les outils
get_video_preview, approve_video_preview et request_video_revision. La validation
est persist?e dans le job et v?rifi?e avant commande de composition compl?te.
La cr?ation d'un film se suspend automatiquement en awaiting_approval.
Le contr?le statique du paquet ne prouve pas la qualit? artistique : un vrai
aper?u avec r?f?rence et ?coute reste n?cessaire.
