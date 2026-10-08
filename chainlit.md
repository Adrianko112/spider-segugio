# spider_segugio

Ciao! Sono **spider_segugio**, un assistente che fa ricerche sul web al posto tuo. Gli dai un argomento e lui si mette sulle tracce delle informazioni, le legge e te le restituisce in un riassunto chiaro, senza che tu debba aprire decine di pagine.

## Cosa faccio

Scrivimi un argomento e io:

1. **Preparo la query**: trasformo la tua richiesta in una query di ricerca più efficace e ti spiego su quale aspetto mi concentro e perché.
2. **Cerco sul web**: raccolgo le fonti più rilevanti con Tavily e ti mostro quelle che ho trovato.
3. **Riassumo**: sintetizzo il contenuto delle fonti in un riassunto chiaro e coerente, senza ripetizioni.
4. **Approfondisco**: individuo cosa manca nel riassunto e formulo una nuova domanda, che diventa la query del giro successivo.

Ripeto questo giro per 4 cicli. A ogni ciclo il riassunto non riparte da zero: viene esteso con le informazioni nuove, così alla fine hai una panoramica sempre più completa.

## Come si usa

Scrivi nella chat l'argomento che ti interessa, per esempio *"novità sulle auto elettriche"*, e aspetta qualche istante. Durante il lavoro i messaggi di `system_assistant` ti mostrano ogni passaggio:

- la query ottimizzata e il motivo della scelta
- le fonti trovate
- il riassunto aggiornato
- la prossima ricerca e la lacuna che ho individuato

L'ultimo riassunto che ricevi è quello più completo.

## Qualche consiglio

- Più l'argomento è specifico, più le ricerche saranno mirate.
- Ogni ciclo richiede qualche secondo, quindi la risposta completa non è immediata.
- Le informazioni arrivano dal web: se una cosa è importante, controlla sempre le fonti.

## Tecnologie

Chainlit per l'interfaccia, OpenAI per query, riassunti e riflessioni, Tavily per la ricerca web.
