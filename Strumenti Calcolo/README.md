# Strumenti Calcolo

Questo breve progetto mostra come calcolare derivate simboliche in Python
fissando esplicitamente le variabili indipendenti e dichiarando la dipendenza
funzionale delle grandezze coinvolte.

## Libreria scelta

La libreria usata e' **SymPy**, perche' e' il modulo Python standard per il
calcolo simbolico. Permette di definire simboli indipendenti con `symbols()`,
funzioni non specificate con `Function()`, e derivate simboliche con `diff()`.

Alternative come NumPy o SciPy sono eccellenti per calcolo numerico, ma non
sono pensate per manipolare derivate formali di funzioni non specificate come
`f(x)`, `g(x, y)` o `V(q(t))`.

## Installazione

```bash
python3 -m pip install sympy
```

## Esecuzione

Dalla cartella del progetto:

```bash
python3 symbolic_derivatives.py
```

Oppure dalla root `Codex`:

```bash
python3 "Strumenti Calcolo/symbolic_derivatives.py"
```

## Esempi inclusi

1. `f = f(x)`: calcolo di `df/dx` e `d^2f/dx^2`.
2. `g = g(x, y)`: calcolo di `dg/dx`, `dg/dy` e della derivata mista.
3. `V = V(q(t))`: derivata totale rispetto a `t`, con regola della catena.
4. `L = L(q(t), dq/dt, t)`: termini simbolici dell'equazione di
   Eulero-Lagrange:

```text
d/dt(dL/dqdot) - dL/dq = 0
```

Il file e' scritto per essere modificato facilmente: cambia simboli, funzioni
o dipendenze nei singoli esempi per adattarlo ad altri problemi.
