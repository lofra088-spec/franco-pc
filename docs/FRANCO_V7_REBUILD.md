# Franco V7 — ricostruzione pulita

Franco V7 viene riscritto senza dipendere da `franco._monolith`. Il vecchio
runtime resta temporaneamente nel repository solo come archivio e riferimento
per estrarre una funzione alla volta dopo averla verificata.

## Funzioni che entrano nella nuova base

- Trascrizione parziale: prepara intento ed entità mentre l'utente parla; esegue
  soltanto sulla trascrizione finale.
- Comandi locali immediati: apertura app e ricerca web non chiamano il modello.
- Conversazione: OpenRouter/Kimi tramite un'interfaccia sostituibile, risposte
  concrete, memoria breve e nessuna falsa dichiarazione di azioni eseguite.
- Franco Code: obiettivi persistenti, avanzamento verificabile, pausa e stop.
- Computer Use: osserva lo schermo a ogni passo, usa un insieme limitato di
  azioni e richiede conferma per effetti esterni o irreversibili.
- Automazioni: regole salvate e attivate da frasi naturali.
- Canvas: testo, schemi, aritmetica, geometria e disegno da richieste naturali.
- Voce: Edge TTS come base affidabile. XTTS resta un modulo opzionale e isolato,
  perché le DLL locali possono essere bloccate dai criteri di Windows.
- Modalità stream: OBS avviato dalla cartella corretta, Discord e dashboard
  configurabili; nessun avvio di Steam o Streamlabs.
- Accesso iPhone: bridge autenticato verso il PC; le funzioni che richiedono il
  PC non fingono di funzionare quando il PC è spento.

## Parti escluse

- Dispatcher gigantesco con routing basato su centinaia di condizioni.
- Moduli offensivi, listener e funzioni non necessarie all'assistente personale.
- Auto-miglioramento che modifica codice senza una proposta e una conferma.
- Fallback lenti a catena e messaggi che dichiarano successi non verificati.
- Dipendenze da file esterni al repository.

## Regole della nuova architettura

1. Ogni azione ha un modulo, un contratto e test propri.
2. Il modello linguistico comprende e pianifica; il codice esegue e verifica.
3. Una trascrizione provvisoria non produce mai effetti sul computer.
4. Ogni azione esterna o irreversibile mostra l'azione precisa prima della conferma.
5. Se una capacità manca, Franco lo dice subito e può preparare una patch testata;
   l'applicazione della patch richiede conferma.
6. Una funzione entra nella V7 solo quando ha un test utile e un esito osservabile.

