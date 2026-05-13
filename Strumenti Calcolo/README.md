# Strumenti Calcolo

`Strumenti Calcolo` e' una raccolta di piccoli script Python dedicati al
calcolo simbolico e al supporto di esercizi di fisica e matematica.

Il progetto nasce con uno script per le derivate simboliche, ma e' pensato per
crescere: in futuro potranno essere aggiunti nuovi file per altri strumenti di
calcolo simbolico, per esempio equazioni differenziali, algebra lineare
simbolica, serie, trasformate, sistemi lagrangiani o manipolazioni di formule.

## Strumenti disponibili

| File | Scopo |
| --- | --- |
| `symbolic_derivatives.py` | Esempi guidati di derivate simboliche, derivate parziali, funzioni composte e termini dell'equazione di Eulero-Lagrange. |

## Requisiti

Il progetto usa principalmente **SymPy**, la libreria Python piu' adatta per il
calcolo simbolico.

Installazione consigliata:

```bash
python3 -m pip install sympy
```

Se lavori dentro un ambiente virtuale:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install sympy
```

## Come eseguire gli script

Dalla cartella `Strumenti Calcolo`:

```bash
python3 symbolic_derivatives.py
```

Dalla cartella superiore del repository:

```bash
python3 "Strumenti Calcolo/symbolic_derivatives.py"
```

## Documentazione dei singoli strumenti

Per i dettagli dello script attuale:

- [`README_symbolic_derivatives.md`](README_symbolic_derivatives.md)

Quando verranno aggiunti nuovi script, ciascuno potra' avere una breve
documentazione dedicata con scopo, dipendenze, comando di esecuzione ed esempi
principali.

## Organizzazione prevista

L'idea e' mantenere ogni strumento semplice, leggibile e modificabile:

- un file Python per ogni argomento principale;
- commenti didattici nei passaggi matematicamente importanti;
- esempi gia' pronti, senza input interattivo obbligatorio;
- README generale aggiornato con l'elenco degli strumenti disponibili;
- eventuale README specifico per gli script piu' importanti.
