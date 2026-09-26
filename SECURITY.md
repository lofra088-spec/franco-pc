# Sicurezza

Non salvare chiavi API, token, password o dati personali nei commit. Usa `.env` locale e mantieni aggiornato `.env.example` senza valori segreti.

OpenRouter è il provider configurato per il percorso principale. Se una chiave è stata pubblicata in chat o in un file, revocala e creane una nuova dal pannello del provider.

Le funzioni che eseguono comandi di sistema sono disabilitate per impostazione predefinita. Abilita esplicitamente `FRANCO_ALLOW_SHELL=1` solo in un ambiente locale controllato.

Prima di esporre il bridge mobile su una rete, imposta `FRANCO_MOBILE_API_KEY`, limita il firewall alla rete necessaria e usa HTTPS tramite un reverse proxy.
